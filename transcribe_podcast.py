import os
import shutil
import datetime
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import psutil
import time


def transcribe_audio_file(file_path, language="de-DE"):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(file_path)
    transcript = ""

    with audio_file as source:
        audio = recognizer.record(source)

    try:
        transcript = recognizer.recognize_google(audio, language=language)
    except sr.RequestError:
        print("API-Anfrage fehlgeschlagen")
    except sr.UnknownValueError:
        print("Spracherkennung konnte den Inhalt nicht verstehen")

    return transcript

def convert_mp3_to_wav(mp3_file_path):
    sound = AudioSegment.from_file(mp3_file_path, format="mp3")
    wav_file_path = mp3_file_path.replace(".mp3", ".wav")
    sound.export(wav_file_path, format="wav")
    return wav_file_path

def split_audio_by_silence(file_path, min_silence_len=500, silence_thresh=-40, chunk_folder="audio_chunks_temp"):
    if not os.path.exists(chunk_folder):
        os.makedirs(chunk_folder)
    else:
        shutil.rmtree(chunk_folder)
        os.makedirs(chunk_folder)

    audio = AudioSegment.from_file(file_path, "wav")
    audio_chunks = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    for i, chunk in enumerate(audio_chunks):
        chunk.export(f"{chunk_folder}/temp_chunk_{i}.wav", format="wav")

    return audio_chunks

def transcribe_podcast(file_path, output_file, language="de-DE"):
    start_time = time.time()
    if file_path.endswith(".mp3"):
        file_path = convert_mp3_to_wav(file_path)

    chunk_folder = "audio_chunks_temp"
    audio_chunks = split_audio_by_silence(file_path, chunk_folder=chunk_folder)
    total_duration = sum([chunk.duration_seconds for chunk in audio_chunks])
    processed_duration = 0.0
    transcript = ""

    for i, chunk in enumerate(audio_chunks):
        chunk_transcript = transcribe_audio_file(f"{chunk_folder}/temp_chunk_{i}.wav", language)
        timestamp = str(datetime.timedelta(milliseconds=chunk.duration_seconds * 1000))
        transcript += f"[{timestamp}] {chunk_transcript}\n"
        processed_duration += chunk.duration_seconds
        progress_percent = round(processed_duration / total_duration * 100, 2)
        print(f"Fortschritt: {progress_percent}% abgeschlossen", end="\r")

    with open(output_file, "w") as f:
        f.write(transcript)

    shutil.rmtree(chunk_folder)
    elapsed_time = time.time() - start_time
    print(f"Transkription abgeschlossen in {round(elapsed_time, 2)} Sekunden.")
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    print(f"Notwendige Rechenleistung: CPU {cpu_percent}%, RAM {memory_percent}%")

if __name__ == "__main__":
    input_file = "/Users/dorianzwanzig/Desktop/py_scripts/transscriptions/Audio/gag350.mp3"
    output_file = "transcription_" + input_file
    transcribe_podcast(input_file, output_file)