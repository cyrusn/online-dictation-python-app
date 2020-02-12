from gtts import gTTS
import io


def voice(title, speed=0.6):
    fp = io.BytesIO()
    tts = gTTS(title, lang='en')
    tts.speed = speed
    tts.write_to_fp(fp)
    fp.seek(0)
    return io.BytesIO(fp.read())


if __name__ == "__main__":

    print(voice('hello'))
