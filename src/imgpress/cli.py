from argparse import Action, ArgumentParser

class ResizeAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        width, height= values
        namespace.width = width
        namespace.height = height

def create_parser():
    parser = ArgumentParser(description="""
    Encode and compress images for the web.
    """)
    parser.add_argument("infile", help="")
    parser.add_argument("-f", "--format", help="outfile file format (JPEG, PNG, WEBP)", required=True)
    parser.add_argument("-q", "--quality", type=int, help="image quality, on a scale from 0 (worst) to 95 (best)")
    parser.add_argument("-r", "--resize",
        help="resize image to width and height values; if one value is zero, aspect ratio of original image is maintained",
        nargs=2,
        metavar=("WIDTH", "HEIGHT"),
        action=ResizeAction)
    parser.add_argument("-o", "--outfile", help="Outfile file name.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--optimize", action="store_true", help="make an extra pass over the image in order to select optimal encoder settings.")
    group.add_argument("--lossless", action="store_true", help="lossless compression for WEBP.")

    return parser

def main():
    from imgpress import resize, rename
    from PIL import Image

    args = create_parser().parse_args()

    if not args.outfile:
        args.outfile = rename.rename(args.infile, args.format)

    kargs = {}
    if args.optimize:
        kargs.update( {"optimize": args.optimize} )
    if args.lossless:
        kargs.update( {"lossless": args.lossless} )
    if args.quality:
        kargs.update( {"quality": args.quality} )

    try:
        with Image.open(args.infile) as im:
            try:
                im = resize.resize_image(im, args.width, args.height)
            except:
                pass

            im.save(args.outfile, args.format, **kargs)

    except IOError as e:
        print(e)
        print("cannot convert", args.infile)
