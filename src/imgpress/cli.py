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
    parser.add_argument("-f", "--format", choices=["JPEG", "PNG", "WEBP"], help="outfile format", required=True)
    parser.add_argument("-q", "--quality", type=int, help="image quality, on a scale from 0 (worst) to 95 (best)")
    parser.add_argument("-r", "--resize",
        help="image is resized to width and height pixel values; if one value is zero, aspect ratio of original image is maintained",
        nargs=2,
        metavar=("WIDTH", "HEIGHT"),
        action=ResizeAction)
    parser.add_argument("-o", "--outfile", help="outfile name")
    parser.add_argument("--optimize", action="store_true", help="make an extra pass over image in order to select optimal encoder settings (JPEG, PNG)")
    parser.add_argument("--lossless", action="store_true", help="lossless compression for WEBP files")
    parser.add_argument("--progressive", action="store_true", help="store image as a progressive JPEG file")
    parser.add_argument("--method", type=int, help="quality/speed trade-off for WEBP files (0=fast, 6=slower-better)")
    
    args = parser.parse_args()

    if args.format == "WEBP" and args.optimize:
        parser.error("--optimize requires either JPEG or PNG")

    if args.format != "WEBP" and args.lossless:
        parser.error("--lossless requires WEBP")

    if args.format != "JPEG" and args.progressive:
        parser.error("--progressive requires JPEG")
    
    if args.format != "WEBP" and args.method:
        parser.error("--method requires WEBP")

    return args

def main():
    from imgpress import resize, rename
    from PIL import Image

    args = create_parser()

    kargs = {}
    if args.optimize:
        kargs.update( {"optimize": args.optimize} )
    if args.lossless:
        kargs.update( {"lossless": args.lossless} )
    if args.quality:
        kargs.update( {"quality": args.quality} )
    if args.progressive:
        kargs.update( {"progressive": args.progressive} )
    if args.method:
        kargs.update( {"method": args.method} )

    try:
        with Image.open(args.infile) as im:
            try:
                im = resize.resize_image(im, args.width, args.height)
            except:
                pass

            if not args.outfile or args.infile == args.outfile:
                args.outfile = rename.rename(args.infile, args.format)

            im.save(args.outfile, args.format, **kargs)

    except IOError as e:
        print(e)
