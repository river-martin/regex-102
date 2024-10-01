def parse_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("regex", type=str, help="The pattern")
    parser.add_argument("text", type=str, help="The text to search")
    parser.add_argument(
        "engine",
        type=str,
        choices=["re2", "pcre2", "bru", "java8"],
        help="The regex engine to use",
    )
    parser.add_argument(
        "--engine-args",
        type=str,
        default="",
        help="The command line arguments for the regex engine (provided as a single string)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    import subprocess
    import os

    engines_dir = os.path.abspath(os.path.dirname(__file__)) + "/../engines"
    match args.engine:
        case "re2":
            cmd = f'python3 {engines_dir}/re2-runner/src/re2_runner.py "{args.regex}" "{args.text}" {args.engine_args}'
        case "pcre2":
            cmd = f'{engines_dir}/pcre2-runner/pcre2_runner "{args.regex}" "{args.text}" {args.engine_args}'
        case "bru":
            cmd = f'{engines_dir}/bru/bin/bru match "{args.regex}" "{args.text}" {args.engine_args} --whole-match-capture'
        case "java8":
            cmd = f'java -classpath {engines_dir}/java8-runner/ Java8Runner "{args.regex}" "{args.text}" {args.engine_args}'
        case _:
            raise ValueError(f"Unknown engine: {args.engine}")
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    main()
