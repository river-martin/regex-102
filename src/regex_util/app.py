from .util import run


def parse_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "regex_file_path",
        type=str,
        help="A path to the file containing the regex pattern",
    )
    parser.add_argument(
        "input_file_path",
        type=str,
        help="A path to a file containing the text to search",
    )
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
    output = run(
        args.engine, args.regex_file_path, args.input_file_path, args.engine_args
    )
    print(output)


if __name__ == "__main__":
    main()
