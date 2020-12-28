from argparse import ArgumentParser
from configparser import ConfigParser
from .import_quiz import add_argument as add_import_quiz_argument
from .serve import add_argument as add_serve_argument
from .download_audio import add_argument as add_download_audio_argument


def run():
    config_parser = ArgumentParser(add_help=False)
    config_parser.add_argument("--config")
    args, remaining_args = config_parser.parse_known_args()

    defaults_config = {
        "port": '5000',
        "static": './static',
        "dsn": "mongodb://localhost:27017/",
        "db_name": 'online_dictation_trial',
        "audio_path": '../public/data/audio'
    }

    if args.config is not None:
        config = ConfigParser()
        config.read(args.config)
        defaults_config.update(config.items("defaults"))

    parser = ArgumentParser(
        prog="Online Dictation System",
        parents=[config_parser],
    )

    sub_command = parser.add_subparsers(
        title='command', description='choose the following command', dest='command'
    )

    def get_config_with_keys(config, keys):
        return {k: v for (k, v) in config.items() if k in keys}

    commands = [{
        "key": "serve",
        "add_argument_func": add_serve_argument
    }, {
        "key": "import_quiz",
        "add_argument_func": add_import_quiz_argument
    }, {
        "key": 'download_audio',
        "add_argument_func": add_download_audio_argument
    }]

    for command in commands:
        sub_command_parser = sub_command.add_parser(command['key'])
        command['add_argument_func'](
            sub_command_parser, config=defaults_config
        )

    args = parser.parse_args(remaining_args, args)
    args.func(args)
