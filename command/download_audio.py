from database.quiz import Quiz
from gtts import gTTS
from os.path import exists


def run(args):
    quiz = Quiz(args.db_name, args.dsn)
    audio_path = args.audio_path
    print(f"Downloading audio files")
    for quiz_name in quiz.quiz_names:
      for id in quiz.find_ids_by_quiz_name(quiz_name):
        vocab = quiz.find_vocab_by_id(id)
        title = vocab['title']
        if not exists(f'{audio_path}/{id}.mp3'):
          tts = gTTS(f'{title}', lang='en')
          tts.speed = 0.8
          tts.save(f'{audio_path}/{id}.mp3')
          print(f'\x1b[2K{id}.mp3 ({title}) has been downloaded.', end='\r')

        else:
          print(f'\x1b[2K{id}.mp3 ({title})is already exist.', end='\r')

    print('\x1b[2KAll audio files are downloaded.')
          

def add_argument(parser, config=None):
    parser.add_argument("--dsn", '-d', help='dsn of mongodb')
    parser.add_argument("--db_name",  help='dbName of database in mongodb')
    parser.add_argument("--audio_path",  help='path of the audio files')
    parser.set_defaults(
        **{k: v for (k, v) in config.items() if k in ["dsn", "db_name", "audio_path"]}
    )
    parser.set_defaults(func=run)
