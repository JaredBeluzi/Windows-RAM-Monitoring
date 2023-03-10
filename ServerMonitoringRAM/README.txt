1. START.bat

Wird jeden Tag um 06:00 gestartet.
Startet die logging.bat

2. logging.bat

Schreibt jede Minute einmal alle Benutzer mit laufenden Prozessen und deren RAM Nutzung in eine logging.csv.
Das wird bis 20:00 gemacht. Dann wird Prozess gestoppt und data_transformation.py gestartet.

3. data_transformation.py

Lädt logging.csv in python, korrigiert einige Fehler in den Daten und aggregiert die Werte sinnvoll um etwas Speicher zu sparen.
Danach werden die Daten in die logging_hist.csv hinzugefügt.