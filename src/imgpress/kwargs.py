def kwargs_used(args):
    """Generate dictionary with used kwargs from argparse."""

    kwargs = ["optimize", "lossless", "quality", "progressive", "method"]

    kwargs_dict = {}
    for kwarg in kwargs:
        if eval("args." + kwarg):
            kwargs_dict.update({kwarg: eval("args." + kwarg)})

    return kwargs_dict
