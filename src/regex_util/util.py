import subprocess
import os

ENGINES = ["re2", "pcre2", "bru", "java8"]


def run(engine: str, regex: str, input_file_path: str, engine_args: str) -> str:
    """
    Run the regex engine with the given arguments.

    :param engine: The regex engine to use (re2, pcre2, bru, or java8)
    :param regex: The regex pattern
    :param input_file_path: A path to the file containing the text to search
    :param engine_args: The command line arguments for the regex engine
    """
    engines_dir = os.path.abspath(os.path.dirname(__file__)) + "/../../engines"
    match engine:
        case "re2":
            cmd = f'python3 {engines_dir}/re2-runner/src/re2_runner.py "{regex}" {input_file_path} {engine_args}'
        case "pcre2":
            cmd = f'{engines_dir}/pcre2-runner/pcre2_runner "{regex}" {input_file_path} {engine_args}'
        case "bru":
            cmd = f'{engines_dir}/bru/bin/bru match "{regex}" {input_file_path} {engine_args} --whole-match-capture'
        case "java8":
            cmd = f'java8 -classpath {engines_dir}/java8-runner/ Java8Runner "{regex}" {input_file_path} {engine_args}'
        case _:
            raise ValueError(f"Unknown engine: {engine}")
    return subprocess.getoutput(cmd)
