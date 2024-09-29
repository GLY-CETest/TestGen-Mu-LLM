# TestGen-Mu-LLM


可直接运行main.py，其输入为多个被测项目所在的basedir。

AST、CFG分析基于CodeParse，于项目[CodeParseForTestGen](https://github.com/GLY-CETest/CodeParseForTestGen)实现，并利用PIT
为被测项目生成mutants。

本项目通过分析器生成的AST、CFG，读取所生成的mutants，结合LLM模型，生成测试用例。
