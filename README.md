# noxBot

## Beschreibung
Da all die 'rr' Programme nur mit torrents funktinoieren (siehe [Radarr](https://radarr.video/), [Sonarr](https://sonarr.tv/)), muss eine alternative für deutsche ddl's hin. Ich habe mich für die Seite von nox entschieden. Da Nox auf anfrage keine API anbietet wird es mit Selenium gelöst.


## Requirements
- [Nox](https://nox.to/)-Konto
- [my.jdownloader](https://my.jdownloader.org)-Konto
- Python3
- Jdownloader
- Selenium
- Chrome
- Chromedriver
- prettytable
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
