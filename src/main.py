def parse_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("regex", type=str, help="The pattern")
    parser.add_argument("text", type=str, help="The text to search")
    parser.add_argument(
        "engine",
        type=str,
        choices=["re2", "pcre2", "bru"],
        help="The regex engine to use",
    )
    parser.add_argument(
        "--engine-args",
        type=str,
        default="",
        help="The command line arguments for the regex engine (provided as a single string)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    import subprocess

    match args.engine:
        case "re2":
            cmd = f"python engines/re2-runner/src/re2_runner.py {args.regex} {args.text} {args.engine_args}"
        case "pcre2":
            cmd = f"./engines/pcre2-runner/pcre2_runner {args.regex} {args.text} {args.engine_args}"
        case "bru":
            cmd = f"./engines/bru/bin/bru {args.regex} {args.text} {args.engine_args} --whole-match-capture"
        case _:
            raise ValueError(f"Unknown engine: {args.engine}")
    subprocess.run(cmd, shell=True)
