import os.path

from utils import parse_result_process
from utils import file_utils
from utils.log import logger

from src.test_generation.test_gen import gen_tests_for_all_mutants_from_llm
from src.utils.codeparse import run_CodeParse_jar


"""
"""


def main(projects_base: str):
    # Parse ast and calls for all the projects under the base folder
    print("=======================================\n"
          "Start Parsing\n"
          "=======================================\n")
    run_CodeParse_jar(projects_base)

    #  combine ast and call relations for all projects in the base folder
    print("=======================================\n"
          "Start Combining\n"
          "=======================================\n")
    logger.info("=======================================Start Combining=======================================")
    projects_dir = file_utils.search_pros_in_folder(projects_base)
    print("projects_dir: ", projects_dir)
    for project_dir in projects_dir:
        print("Combining ast and calls for project {}".format(os.path.split(project_dir)[1]))
        logger.info("Combining ast and calls for project {}".format(os.path.split(project_dir)[1]))
        parse_result_process.combine_ast_calls_for_all(project_dir)

    #  generate tests based on mutants
    print("=======================================\n"
          "Start Generating Tests\n"
          "=======================================\n")
    logger.info("=======================================Start Generating Tests=======================================")
    for project_dir in projects_dir:
        gen_tests_for_all_mutants_from_llm(project_dir)


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.abspath(__file__))
    print(current_path)
    projects_base_dir = r"C:\YGL\Projects\pythonProject\TestGen-Mu-LLM\projUT"
    main(projects_base_dir)


