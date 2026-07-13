import argparse

# Create parser
parser = argparse.ArgumentParser(description="Take one input value")

# Add argument
parser.add_argument("value", help="Input value")

# Parse arguments
args = parser.parse_args()

# Print the value
print(f"You entered: {args.value}")
