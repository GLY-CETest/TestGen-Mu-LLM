import subprocess
import sys
import os


def run_CodeParse_jar(projects_base: str, jar_path=r'..\dependencies\CodeParseForTestGen-1.0-SNAPSHOT.jar'):
    # subdirectories = [os.path.join(projects_base, d) for d in os.listdir(projects_base) if
    #                   os.path.isdir(os.path.join(projects_base, d))]
    # print("subdirectories: ", subdirectories)

    # current_path = os.getcwd()
    # print(current_path)
    run_dir = r'../dependencies'  # 由于执行脚本是的执行路径不同，如需直接执行该脚本，则此处路径应为'../../dependencies'，如从main
    # 脚本调用该函数，则此处路径应为'../dependencies'，
    # for dir in subdirectories:
    #     cmd = ['java', '-jar', jar_path, dir]
    #     result = subprocess.run(cmd,
    #                             # capture_output=True,
    #                             shell=True,
    #                             # text=True,
    #                             cwd=run_dir,
    #                             stdout=subprocess.PIPE,
    #                             stderr=subprocess.PIPE,)
    #     print("result.stderr: ", result.stderr)
    #     print("\nresult.stdout: ", result.stdout)

    cmd = ['java', '-jar', jar_path, projects_base]
    result = subprocess.run(cmd,
                            # capture_output=True,
                            shell=True,
                            # text=True,
                            cwd=run_dir,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,)
    # print("result.stderr: ", result.stderr)
    # print("\nresult.stdout: ", result.stdout)


# cmd = ['java', '-jar', 'src/CodeParse-1.0-SNAPSHOT-jar-with-dependencies.jar']


if __name__ == '__main__':
    # jar_path = r'..\dependencies\CodeParseForTestGen-1.0-SNAPSHOT.jar'
    # current_path = os.path.dirname(os.path.abspath(__file__))
    # print(current_path)
    projects_base_dir = r'C:\YGL\Projects\pythonProject\TestGen-Mu-LLM\projUT'
    run_CodeParse_jar(projects_base_dir)



