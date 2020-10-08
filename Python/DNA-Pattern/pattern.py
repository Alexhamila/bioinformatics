
import sys

def main():
    """Code to be executed"""
    sequence = input("Please enter a sequence: ").upper()
    pattern = input("Please enter a pattern: ").upper()

    if pattern not in sequence:
        print("Pattern is not in sequence.")
        sys.exit()

    pattern_start = sequence.index(pattern)

    print(sequence)
    print(" " * pattern_start + "|" * len(pattern))
    print(" " * pattern_start + pattern)

main()
