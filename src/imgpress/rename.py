import os
import sys


def rename(infile, form):
    """Automatic naming of outfile with original overwrite protection."""
    f, e = os.path.splitext(infile)
    outfile = f + "." + form.lower()

    if outfile in os.listdir():
        num = 0
        while outfile in os.listdir():
            num += 1
            num_formatted = f"_{num:02d}."
            outfile = f + num_formatted + form.lower()

    return outfile
