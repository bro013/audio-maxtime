import os
from mutagen.mp3 import MP3

MAX_LENGTH_SECONDS = 10

def processAudioFile(audio_file):
    audio = MP3(audio_file)
    nbytes = int((MAX_LENGTH_SECONDS * audio.info.bitrate) / 8)
    output_dir = 'output'
    output_file = '{0}/{1}'.format(output_dir, audio_file)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(audio_file, 'rb') as in_file:
        data = in_file.read()

    with open(output_file, 'wb') as out_file:
        if audio.info.length > MAX_LENGTH_SECONDS:
            out_file.write(data[:nbytes])
        else:
            out_file.write(data)


if __name__ == '__main__':
    audio_file = r'mc-hammer-u-cant-touch-this.mp3'
    processAudioFile(audio_file)