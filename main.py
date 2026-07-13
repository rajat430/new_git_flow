import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--value", required=True, help="Input value")

args = parser.parse_args()

print(args.value)
try:
  with open(args.value,"w") as f:
    f.write("hello world")
except Exception as error:
  print(f"there is some issue: {error}")
