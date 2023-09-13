# noxBot

# ❗An diesem Projekt wird nicht mehr weitergearbeitet. Das neue Projekt heisst Plexer.❗


## Description
Da all die 'rr' Programme nur mit torrents funktionieren (siehe [Radarr](https://radarr.video/), [Sonarr](https://sonarr.tv/)), muss eine alternative für deutsche ddl's hin. Ich habe mich für die Seite von nox entschieden. Da Nox auf anfrage keine API anbietet wird es mit Selenium gelöst. Mithilde der TMDB API werden die Filme anschliessend umbenennt. HandBrake hilft beim konvertieren (mkv -> mp4, german forced sub, german & english) zu mp4 um Platz zu sparen und die Filme ohne Transkodierung abspielen zu können. Anschliessend werden die Dateien in einen Ordner verschoben. Dieser kann dann im Emby, Plex oder Jellyfin als Bibliotheke hinzugefügt werden. Bei Fehler vom Skript erhaltest Du eine Email und es wird im Log ('log_convert_rename_move.txt') vermerkt.


![Donwload](https://i.imgur.com/5e235hS.gif)

## Requirements
- [TMDB API KEY](https://www.themoviedb.org/settings/api?language=de-CH) (Konto erstellen und auf der Kontoseite kopieren)
- [Nox](https://nox.to/)-Konto
- [my.jdownloader](https://my.jdownloader.org)-Konto
- [Chromedriver](https://chromedriver.chromium.org/) (in PATH) (muss mit der Version von Chrome übereinstimmen)
- [HandbrakeCLI](https://handbrake.fr/downloads2.php) (in PATH)
- Python3 (in PATH)
- Jdownloader2 (Unter Einstellungen angemeldet -> my.jdownloader)
- Chrome
- [Selenium](https://pypi.org/project/selenium/)
- [prettytable](https://pypi.org/project/prettytable/)
- Im Jdownloader muss der Augabe-Pfad auf `C:\space\downloaded\` geändert werden.
- MultiHoster Konto zum downloaden der Dateien (z.B. [Linksnappy](https://linksnappy.com/?ref=354818)(Abo) oder [Premium.to](http://premium.to/?ref=GY2TCMBQ)(Prepaid))
- MultiHoster-konto muss im JDownloader aktiviert sein
- Auf dem zu benutzenden my.jdownloader-Konto darf nur ein Computer angemeldet sein
- Im get_movie_CLI.py müssen `noxusername`, `noxpassword`, `myjdownloaderusername` und `myjdownloaderpassword` mit Deinen angaben ausgefüllt werden.




## Installation
```
#Herunterladen der Repo
git clone https://github.com/2223sam/noxBot.git

#Navigieren in das noxBot Verzeichnis
cd noxBot

#Erstellen der Aufgabenplanung (diese Sorgt dafür, dass alle 5 Minuten überprüft wird ob neue Dateien zu Managen sind)
#Passwort wird gebraucht um den Task zu installieren
clear
echo "Bitte gib Dein passwort ein um den Task zum umbenennen und konvertieren der Filme ein:"
schtasks /create /xml ".\convert_rename_move-task_schedule.xml" /tn "convert_rename_move" /ru $env:UserName /rp *

#Erstellen der Ordner
mkdir C:\space
mkdir C:\space\tools
mkdir C:\space\media
mkdir C:\space\downloaded
mkdir C:\space\converted
mkdir C:\space\renamed

#Kopieren der Dateien ins Zielverzeichniss
cp ".\convert_rename_move.ps1" "C:\space\tools\"
cp ".\lowmoviesbyelias.json" "C:\space\tools\"
cp ".\get_movie_CLI.py" "C:\space\tools\"

#Passe die Angaben an (sind praktisch ganz oben): 'noxusername', 'noxpassword', 'myjdownloaderusername' und 'myjdownloaderpassword'
notepad "C:\space\tools\get_movie_CLI.py"

#Passe die Angaben an (sind ganz oben): '$tmdb_API_KEY', '$gmail_sender_address', '$gmail_sender_password' und '$reciver_address'
notepad "C:\space\tools\convert_rename_move.ps1"

#Lösche den noxBot-ordner welcher nicht mehr gebraucht wird:
cd ..; rm -Recurse -Force noxBot\
clear
echo "Installation abgeschlossen"

```


## Usage
Zum starten des ganzen öffne die PowerShell und füge folgenes ein:
```
python C:\space\tools\get_movie_CLI.py
```
Du wirst nun nach dem Filmname und der Verfügbaren Qualität gefragt. Soabld dies getan ist wird der Film heruntergeladen. 
Den fertigen Film findest Du unter `C:\space\media\movies\`



## Ordnerstruktur
Hier ist zu sehen wie die Ordnerstruktur aussehen sollte.
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




## ToDo
- [x] Wähle zwischen den Verschiedenen Uploads
- [x] my.jdownloader Integration
- [x] CLI-Version
- [x] Automatisches umbenennen, verschieben und konvertieren der Dateien (siehe move [convert_rename_move](#))
- [x] Ersetze von Windows nicht erlaubte Zeichen für Dateien (:)->( - ) & (')->()
- [x] Automatisieren mithilfe der Aufgabenplanung
- [ ] GUI-Version von 'get_movie_CLI.py'
- [ ] Kalender mit automatischem Download nach release auf nox
- [ ] Telegram-Integrierung

