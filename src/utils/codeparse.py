import subprocess
import sys
import os


def run_CodeParse_jar(projects_base: str, jar_path=r'..\dependencies\CodeParseForTestGen-1.0-SNAPSHOT.jar'):
    # current_path = os.getcwd()
    # print(current_path)
    run_dir = r'C:\YGL\Projects\pythonProject\TestGen-Mu-LLM\dependencies'
    cmd = ['java', '-jar', jar_path, projects_base]
    result = subprocess.run(cmd,
                            # capture_output=True,
                            shell=True,
                            # text=True,
                            cwd=run_dir,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,)
    # print(result)


# cmd = ['java', '-jar', 'src/CodeParse-1.0-SNAPSHOT-jar-with-dependencies.jar']


if __name__ == '__main__':
    # jar_path = r'..\dependencies\CodeParseForTestGen-1.0-SNAPSHOT.jar'
    projects_base_dir = r'C:\Users\dell\Desktop\projects'
    run_CodeParse_jar(projects_base_dir)



