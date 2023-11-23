# Musikinfo

Musikinformatik Repo von Nico Friedmann und Lukas Fey

## Aktueller stand
Aktuell macht advscript theoretisch das was es soll, aber schlechter als der librosa approach. Trotzdem ist das erstmal unsere basis.\
audioanalysis macht an sich nichts zum sound trennen, das erstellt nur grafiken, mit werten die wir für othercustomextraction verwenden können. Othercustomextraction extracted den drum part nicht selbst dynamisch, sondern mit manuellen parametern.\
Als files sollten wir immer eine file mit dem grundalgorithmus haben.\
Eine mit algorithmus mit custom parameters\
Ene wav\
eine Readme\ 
und eine gitignore.\
alles was mehr ist, bitte in old approaches rein schieben oder in die gitignore packen.

## Erwünschtes Verhalten.
Bei start des Projekts ein mal pullen, vor push eines updates, ein mal pullen.\
Ich hab keinen bock auf merge conflicts. Ansonsten können wir auch einen test branch erstellen.
## File management
Wenn du eine datei hast, die ungefähr das macht was wir wollen, nur mit einem schlechten ergebnis, nicht löschen sonder in old_approaches verschieben, dann können wir uns später nochmal angucken was funktioniert hat.

## Temporäre files
Falls temporäre files durch ausführen des codes generiert werden, diese files bitte ins gitignore packen. Die erstellten dateien existieren nur zum lokalen testen und sind nicht teil des Projekts.

## Setup von Environment und packages
(In anaconda prompt, oder wenn aufgesetzt in CMD)\
conda create -n musikenv python=3.11\
conda activate musikenv\
pip install librosa\
pip install soundfile\
pip install matplotlib\
pip install datetime\
pip install IPython\
pip install numpy\
pip install jupyterlab\
pip install notebook\
(Soundfile sollte eigentlich bei librosa dabei sein, ich mach das nur sicherheitshalber)\
(falls ich pip installs vergessen habe, gerne hinzufügen)\
(wenn pip install nicht funktioniert, dann pip3 install)\
(andere python versionen können funktionieren, aber ich weiß nicht welche. 3.11 funktioniert bei mir, wie das environment heißt ist egal, habs halt so genannt damit ich es zuordnen kann.)

## Optionales setup von vscode für weniger arbeit
mit strg + shift + p \
Terminal: select default profile command prompt auswählen (weil powershell kein python kann)\
dann wieder strg + shift + p\
python: select interpreter\
und da dein environment auswählen.\
Dann musst du das nicht immer manuell starten

