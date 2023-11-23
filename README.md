# Musikinfo

Musikinformatik Repo von Nico Friedmann und Lukas Fey

## Erwünschtes Verhalten.
Bei start des Projekts ein mal pullen, vor push eines updates, ein mal pullen.\
Ich hab keinen bock auf merge conflicts.
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

