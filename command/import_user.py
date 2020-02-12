def run(args):
    print(f"runing import_user command with argument:\n{args}")


def add_argument(parser, config=None):
    parser.add_argument(
        "file", help='path of user json file')
    parser.add_argument("--dsn", '-d', help='dsn of mongodb')
    parser.set_defaults(
        **{k: v for (k, v) in config.items() if k in ["dsn"]}
    )
    parser.set_defaults(func=run)
