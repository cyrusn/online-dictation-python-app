from serve.serve import run as run_serve


def run(args):
    run_serve(port=args.port, static=args.static,
              dsn=args.dsn, dbName=args.db_name)


def add_argument(parser, config=None):
    parser.add_argument("--port", help='port is port', type=int)
    parser.add_argument("--static", help='static file', type=str)
    parser.add_argument("--dsn", '-d', help='dsn of mongodb', type=str)
    parser.add_argument("--db_name", '-n',
                        help='datbase name of mongodb', type=str)
    parser.set_defaults(
        **{k: v for (k, v) in config.items() if k in ['port', 'static', 'dsn', 'db_name']}
    )
    parser.set_defaults(func=run)
