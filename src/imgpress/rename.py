import os

def rename(infile, format):
    f, e = os.path.splitext(infile)
    if format == "JPEG":
        outfile_extension = ".jpeg"
    if format == "PNG":
        outfile_extension = ".png"
    if format == "WEBP":
        outfile_extension = ".webp"
    outfile = f + outfile_extension

    return outfile