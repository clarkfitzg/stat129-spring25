def head(stream, size=10):
    """
    Return the first elements of stream as a list.
    """
    # There are more elegant/efficient ways to do this in Python,
    # but this implementation is more clear, and closely related to
    # reservoir sampling.
    output = []
    n = 0
    for x in stream:
        if n < size:
            output.append(x)
            n = n + 1
    return output


if __name__ == "__main__":
    import sys

    import argparse
    # Import the module from the standard library
    # You could use sys.argv rather than argparse, 
    # but argparse is a more sophisticated and robust
    # way to build command line programs.

    parser = argparse.ArgumentParser(description = "output the first part of stdin")
    # Create an argument parser, an object to take the
    # text input passed from the command line and convert it into
    # arguments that Python understands.
    # description shows up when you access the help from the command line:
    # $ python3 head.py --help

    # You can add as many arguments as you like.
    parser.add_argument("-n",   # usage: $ python3 head.py -n 5
        "--lines",              # usage: $ python3 head.py --lines=5
        default=10,             # default to 10 lines
        help="print the first NUM lines",   # access with $ python3 head.py --help
        type=int)   # Convert to integer rather than string

    # The parser is now ready to go, so we can parse the actual arguments.
    args = parser.parse_args()
    
    s = head(sys.stdin, args.lines)
    # Call the head() function defined above, passing in sys.stdin for
    # the stream, and the parsed number of lines.

    # Print out the selected elements to stdout.
    for x in s:
        print(x, end="")  # end="" prevents blank lines
