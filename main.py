import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--value", required=True, help="Input value")

args = parser.parse_args()

print(args.value)
