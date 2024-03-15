import pyaudio
import numpy as np
import queue
import threading
import wave
from vosk import Model, KaldiRecognizer
from vosk import SetLogLevel
from translate import Translator
import whisper

# Constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
SECONDS_OF_SILENCE = 1
MODEL_PATH = 'whisper'  # Replace with the path to your Whisper model

# Global variables
audio_queue = queue.Queue()
record_stream = None
should_record = False


def audio_callback(in_data, frame_count, time_info, status):
    audio_queue.put(in_data)
    return None, pyaudio.paContinue


def record_audio():
    global record_stream, should_record

    audio = pyaudio.PyAudio()
    record_stream = audio.open(format=FORMAT,
                               channels=CHANNELS,
                               rate=RATE,
                               input=True,
                               frames_per_buffer=CHUNK,
                               stream_callback=audio_callback)

    while should_record:
        pass

    record_stream.stop_stream()
    record_stream.close()
    audio.terminate()


def save_audio_segment(segment, filename):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(record_stream.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(segment)
    wf.close()


def process_audio_segment(segment):
    # Load the Whisper model
    model = Model(whisper)
    SetLogLevel(-1)  # Disable model logging (optional)

    # Initialize the Whisper recognizer
    recognizer = KaldiRecognizer(model, RATE)

    # Perform speech recognition on the audio segment
    recognizer.AcceptWaveform(segment)
    result = recognizer.Result()

    # Extract the recognized text
    text = result["text"]

    # Perform translation from Spanish to English
    translator = Translator(from_lang='spanish', to_lang='english')
    translation = translator.translate(text)

    # Print the recognized text and translation
    print("Recognized Text:", text)
    print("Translation:", translation)


def main():
    global should_record

    audio = pyaudio.PyAudio()
    record_stream = audio.open(format=FORMAT,
                               channels=CHANNELS,
                               rate=RATE,
                               input=True,
                               frames_per_buffer=CHUNK,
                               stream_callback=audio_callback)

    while True:
        user_input = input().lower()

        if user_input == 's':
            should_record = True
            threading.Thread(target=record_audio).start()
        elif user_input == 'q':
            should_record = False
            break

    record_stream.stop_stream()
    record_stream.close()
    audio.terminate()


if __name__ == '__main__':
    main()
