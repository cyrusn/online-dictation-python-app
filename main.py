from argparse import ArgumentParser
from serve.command import add_argument as add_serve_argument
from importcmd.command import add_argument as add_import_argument


parser = ArgumentParser(prog="Online Dictation System")
parsers = parser.add_subparsers(title="sub-commands", dest="command")
parser.set_defaults(func=lambda args: parser.print_help())


serve_parser = parsers.add_parser("serve", help="start online dictation system")
add_serve_argument(serve_parser)

import_parser = parsers.add_parser("import", help="import users from a file")
add_import_argument(import_parser)


if __name__ == "__main__":
    args = parser.parse_args()
    args.func(args)
