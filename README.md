# noxBot

## Beschreibung
Da all die 'rr' Programme nur mit torrents funktionieren (siehe [Radarr](https://radarr.video/), [Sonarr](https://sonarr.tv/)), muss eine alternative für deutsche ddl's hin. Ich habe mich für die Seite von nox entschieden. Da Nox auf anfrage keine API anbietet wird es mit Selenium gelöst. Mithilde der TMDB API werden die Filme anschliessend umbenennt. HandBrake hilft beim konvertieren zu mp4 um Platz zu sparen und die Filme ohne Transkodierung abspielen zu können.


## Requirements
- [HandbrakeCLI](https://handbrake.fr/downloads2.php) (in PATH)
- [Nox](https://nox.to/)-Konto
- [my.jdownloader](https://my.jdownloader.org)-Konto
- Python3
- Jdownloader
- [Selenium](https://pypi.org/project/selenium/)
- Chrome
- [Chromedriver](https://chromedriver.chromium.org/) (in PATH)
- [prettytable](https://pypi.org/project/prettytable/)
- Im Jdownloader muss der Augabe-Pfad auf `C:\space\downloaded\` geändert werden.
- MultiHoster Konto zum downloaden der Dateien (z.B. [Linksnappy](https://linksnappy.com/?ref=354818)(Abo) oder [Premium.to](http://premium.to/?ref=GY2TCMBQ)(Prepaid))
- MultiHoster-konto muss im JDownloader aktiviert sein
- Auf dem zu benutzenden my.jdownloader-Konto darf nur ein Computer angemeldet sein
- Im get_movie_CLI.py müssen `noxusername`, `noxpassword`, `myjdownloaderusername` und `myjdownloaderpassword` mit Deinen angaben ausgefüllt werden.

## HowTo
Herunterladen der Repo
```
https://github.com/eliasfrehner/noxBot.git
```
Navigieren in das noxBot Verzeichnis
```
cd noxBot/
```
Ausführen des Scriptes
```
python3 get_movie_CLI.py
```

- [x] Wähle zwischen den Verschiedenen Uploads
- [x] my.jdownloader Integration
- [x] CLI-Version
- [x] Automatisches umbenennen, verschieben und konvertieren der Dateien (siehe move [convert_rename_move](#))
- [ ] GUI-Version









# noxBot_moviemanager

## Beschreibung
Wurden die mit dem [noxBot](https://github.com/eliasfrehner/noxBot) automatisierten Downloads erstmal fertiggestellt werden diese mit der in dieser Repo enthaltenen Dateien automatisch umbenennt, konvertiert (mkv -> mp4, german forced sub, german & english) und verschoben.


## Requirements
- [HandbrakeCLI](https://handbrake.fr/downloads2.php) (in PATH)
- Im Jdownloader muss der Augabe-Pfad auf `C:\space\downloaded\` geändert werden.
- `convert_rename_move.ps1`, `log_convert_rename_move.txt`, `owmoviesbyelias.json` und `get_movie_CLI.py` müssen sich im Ordner `C:\space\tools\` befinden


## Ordnerstruktur
```
C:\space\
├── media\
│   ├── movies\
│   │   ├── 'Red Notice (2021).mp4'
│   │   └── 'Shang-Chi and the Legend of the Ten Rings (2021)'
│   │
│   └── tvshows\
│
├── tools\
│   ├── 'convert_rename_move.ps1'
│   ├── 'log_convert_rename_move.txt'
│   ├── 'lowmoviesbyelias.json'
│   └── 'get_movie_CLI.py'
│
├── downloaded\
│   ├── 'tt3758814_The Ice Road'
│   └── 'tt8110246_Dark Web: Cicada 3301'
│
├── renamed\
│   ├── 'The Ice Road (2021).mkv'
│   └── 'Dark Web - Cicada 3301 (2021).mkv'
│
└── converted\
    ├── 'The Ice Road (2021).mp4'
    └── 'Dark Web - Cicada 3301 (2021).mp4'
```


## Installation
Herunterladen der Repo
```
https://github.com/eliasfrehner/noxBot.git
```
Navigieren in das noxBot Verzeichnis
```
cd noxBot/
```
Kopieren, erstellen und löschen wichtiger Dateien
```
mkdir C:\space
mkdir C:\space\tools
mkdir C:\space\media
mkdir C:\space\downloaded
mkdir C:\space\converted
mkdir C:\space\renamed
cp "convert_rename_move.ps1" C:\space\tools\
cp "lowmoviesbyelias.json" C:\space\tools\
```

- [x] Ersetze von Windows nicht erlaubte Zeichen für Dateien (:)->( - ) & (')->()
- [x] Automatisieren mithilfe der Aufgabenplanung
- [ ] Log nach gewisser Zeit bereinigen

