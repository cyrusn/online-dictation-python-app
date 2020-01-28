def run_import(args):
    print("using import command")
    print(f"importing from file: {args.file}")


def add_argument(parser):
    parser.add_argument(
        "--file", "-f", help="json file to import", default="./data/user.json"
    )
    parser.set_defaults(func=run_import)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    add_argument(parser)
    args = parser.parse_args()
    args.func(args)
