import glob
import re
import os
from openai import OpenAI

api_key = 'sk-zcXsnDoHQwPMY9mK3485D81299C0430aB97e234471EcBfFc'
api_base = "https://hk.xty.app/v1"
client = OpenAI(api_key=api_key, base_url=api_base)


def get_test_methods(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    method_declarations = re.findall(r'(@Test\s*(?:\(.*?\))?\s*public void (\w+)\(\))', content)

    test_methods = []
    print("find method count", len(method_declarations))
    for method_declaration in method_declarations:
        method_body = method_declaration[0]
        print("find method:", method_body)
        origin_index = content.index(method_body)
        start_index = origin_index + len(method_body)
        # 继续向前查找，直到找到第一个 {
        while content[start_index] != '{':
            start_index += 1
        brace_count = 1  # 已经找到了一个 {
        for i in range(start_index + 1, len(content)):
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
            if brace_count == 0:
                # 找到了完整的方法体
                method_body = content[origin_index:i + 1]
                test_methods.append((method_body, method_declaration[1]))
                break

    # 移除不包含断言的方法
    filtered_test_methods = [(method_name, method_body) for method_body, method_name in test_methods if
                             re.search(r'\b(?:assert\w*|assertTrue|assertFalse)\s*\(', method_body)]
    for (name, body) in filtered_test_methods:
        print("find:", name, body)
    return filtered_test_methods


def split_assertions(test_methods):
    new_test_methods = []
    for method_name, method_body in test_methods:
        # 使用OpenAI对方法体进行拆分
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user",
                     "content": f"""
        你是一个拆分代码的AI助手，你的任务是将一个junit代码方法拆分成若干个独立可运行的junit测试单元方法。要求：
        1.一个测试单元只能有一个断言
        2.如果原代码只有一个断言，不用拆分
        3.你的输入是一个完整的方法
        4.输出该方法被拆分后的若干个方法
        5.输出不需要其他提示词
        方法体:
        \n\n{method_body}\n\n"""}
                ],
                # response_format={ "type": "json_object" }
            )
            new_body = response.choices[0].message.content
            new_test_methods.append((method_name, new_body))
            print(f"Method '{method_name}' was successfully split into separate test units.")
        except Exception as e:
            print(f"Failed to split method '{method_name}'. Error: {str(e)}")
    return new_test_methods


def write_new_file(file_path, origin_test_methods, new_test_methods):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 创建一个字典，将方法名映射到新的方法体
    new_methods_dict = {name: body for name, body in new_test_methods}

    # 替换原始文件中的测试方法体
    for method_name, old_body in origin_test_methods:
        if method_name in new_methods_dict:
            print("be replace", method_name)
            new_body = new_methods_dict[method_name]
            print("old-------------", old_body)
            print("new-------------", new_body)
            content = content.replace(old_body, new_body)

    # 将更改后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def process_directory(directory):
    test_files = glob.glob(os.path.join(directory, r'src\test\java\*\*\*.java'), recursive=True)
    print(test_files)
    for file_path in test_files:
        test_methods = get_test_methods(file_path)
        if test_methods:
            new_test_methods = split_assertions(test_methods)
            write_new_file(file_path, test_methods, new_test_methods)


# 指定要扫描的目录
directory_to_scan = r'C:\Users\dell\Desktop\BPlusTree\BPlusTree1\BPlusTree_1509180700625'
process_directory(directory_to_scan)

# if __name__ == '__main__':
#     directory = r'C:\Users\dell\Desktop\BPlusTree\BPlusTree1\BPlusTree_1509180700625'
#     print(os.path.join(directory, r'src\test\java\net\mooctest\*.java'))
#     test_files = glob.glob(os.path.join(directory, r'src\test\java\*\*\*.java'), recursive=True)
#     print(test_files)
