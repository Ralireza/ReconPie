import argparse

parser = argparse.ArgumentParser(description='Process some inputs.')
parser.add_argument('--number', type=int, help='process a number')
parser.add_argument('--text', type=str, help='process some text')
parser.add_argument('--flag', action='store_true', default=False,
                    help='set a flag')
parser.add_argument('files', nargs='*', help='process one or more files')

args = parser.parse_args()

if args.number is not None:
    print(f"Processing number: {args.number}")
if args.text is not None:
    print(f"Processing text: {args.text}")
if args.flag:
    print("Flag is set")
if args.files:
    print(f"Processing {len(args.files)} file(s): {', '.join(args.files)}")

# $ python args-example.py --number 42
# Processing number: 42

# $ python args-example.py --text "Hello, world!"
# Processing text: Hello, world!

# $ python args-example.py --flag
# Flag is set

# $ python args-example.py file1.txt file2.txt
# Processing 2 file(s): file1.txt, file2.txt

# $ python args-example.py --text "Hello" file.txt
# Processing text: Hello
# Processing 1 file(s): file.txt
