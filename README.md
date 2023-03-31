# Transkriptions-Tool für Podcasts
Dieses Python-Skript ist ein einfaches Tool zum Transkribieren von Podcasts. Es verwendet die speech_recognition, pydub, os, shutil, datetime, time und psutil-Bibliotheken, um Audio-Dateien in Chunks zu teilen, diese transkribieren und die Ergebnisse in einer Textdatei speichern.

## Installation
Um das Skript auszuführen, benötigen Sie Python 3 und die folgenden Bibliotheken:

speech_recognition
pydub
psutil
Sie können die Bibliotheken mit pip installieren:

pip install speech_recognition pydub psutil

## Verwendung
Platzieren Sie Ihre Podcast-Datei im selben Verzeichnis wie das transcribe_podcast.py-Skript.

Öffnen Sie eine Terminal-Shell und navigieren Sie zum Verzeichnis mit dem Skript.

Geben Sie folgenden Befehl ein und drücken Sie die Enter-Taste:

python transcribe_podcast.py <input_file> <output_file>

<input_file> ist der Name der Podcast-Datei, die Sie transkribieren möchten. Der Dateiname sollte den vollständigen Pfad zur Datei enthalten, falls sich die Datei nicht im selben Verzeichnis wie das Skript befindet.

<output_file> ist der Name der Transkriptionsdatei, die vom Skript generiert werden soll. Der Dateiname kann beliebig gewählt werden, muss jedoch mit der Erweiterung ".txt" enden.

Das Skript wird die Podcast-Datei in Chunks aufteilen, jeden Chunk transkribieren und die Ergebnisse in der angegebenen Ausgabedatei speichern.

## Beschränkungen
Das Skript ist derzeit nur für Audio-Dateien im WAV- oder MP3-Format konzipiert. Es wurde auf einem Mac-Computer getestet und ist möglicherweise nicht kompatibel mit anderen Betriebssystemen.
