# regex-102

A command line utility similar to [regex101.com](regex101.com).

Match information is output in [TOML](https://toml.io/en/) syntax as follows:

```toml
[match_1]

# The zeroth group captures the whole match.
[match_1.group_0]
span = [0, 1] # the start and end positions of the substring matched
str = """the substring matched"""

[match_1.group_1]
span = [2, 3] # the start and end positions of the substring captured by the first group
str = """the substring captured by the first group"""

[match_1.group_2]
span = [4, 5] # the start and end positions of the substring captured by the second group
str = """the substring captured by the second group"""
```

## Installation

```Bash
git submodule update --init --recursive
```

Follow the instructions given in the git submodules to install the dependencies of each runner (engine). Then, build the engines and install the utility with the commands below.

```Bash
make engines
python3 -m venv env
source env/bin/activate
pip install -e .
```

## Usage

```Bash
regex-102 -h
```
