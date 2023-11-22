# musikinfo
Musikinformatik Repo von Nico Friedmann und Lukas Fey

Damit python keine (allzu schweren) Probleme macht,

conda create -n musikenv python=3.11

conda activate musikenv
pip install librosa
pip install soundfile
(Soundfile sollte eigentlich bei librosa dabei sein, ich mach das nur sicherheitshalber)

dann in vscode mit strg + shift + p 
Terminal: select default profile command prompt auswählen (weil powershell kein python kann)
dann wieder strg + shift + p
python: select interpreter
und da dein environment auswählen.
Dann musst du das nicht immer manuell starten
