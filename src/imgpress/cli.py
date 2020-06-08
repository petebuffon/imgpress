def main():
    """Encode and compress images for the web."""
    from imgpress import resize, rename, kwargs, parser
    from PIL import Image

    args = parser.create_parser()
    kwargs = kwargs.kwargs_used(args)

    try:
        with Image.open(args.infile) as im:

            try:
                if args.width and args.height:
                    im = resize.resize_image(im, args.width, args.height)
            except AttributeError:
                pass

            if not args.outfile or args.infile == args.outfile:
                args.outfile = rename.rename(args.infile, args.format)

            im.save(args.outfile, args.format, **kwargs)

    except IOError as e:
        print(e)
