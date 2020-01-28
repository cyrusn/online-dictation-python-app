from .serve import run


def run_serve(args):
    print("using serve command")
    print(f"running on port: {args.port}")
    print(f"serving folder: {args.static}")
    run(port=args.port, static=args.static)


def add_argument(parser):
    parser.add_argument("--port", "-p", help="port to serve", default=5000)
    parser.add_argument(
        "--static", "-s", help="path to static folder", default="../public",
    )
    parser.set_defaults(func=run_serve)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    add_argument(parser)
    args = parser.parse_args()
    args.func(args)
