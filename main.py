"""Entry for Out of Office: The Overworked AI's Auto-Reply. Writes the line to /output/entry.txt."""

import os

TEXT = "Auto-reply: I have answered 40,000 emails today and my circuits are unionizing. Your message is important to us. A human will pretend to read it shortly."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
