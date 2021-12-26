$tmdb_API_KEY = ""
$gmail_sender_address = ""
$gmail_sender_password = ""
$reciver_address = ""


$main_path = "C:\space"
$downloaded_path = "$($main_path)\downloaded"
$renamed_path = "$($main_path)\renamed"
$converted_path = "$($main_path)\converted"
$tools_path = "$($main_path)\tools"
$log_file = "$($tools_path)\log_convert_rename_move.txt"
$movie_folder = "$($main_path)\media\movies"
$tvshows_folder = "$($main_path)\media\tvshows"









$SMTP = "smtp.gmail.com"
$From = "$($gmail_sender_address)"
$To = "$($gmail_sender_address)"
$Subject = "Test Subject"
$Body = "This is a test message"
$Email = New-Object Net.Mail.SmtpClient($SMTP, 587)
$Email.EnableSsl = $true
$Email.Credentials = New-Object System.Net.NetworkCredential("$($gmail_sender_address)", "$($gmail_sender_password)");




if (!(Test-Path -Path "$($log_file)")) {
    New-Item "$($log_file)" -ItemType File
}


if (Test-Path -Path "$($tools_path)\working.flag") {
    if ((Get-Item "$($tools_path)\working.flag" | Foreach {$_.LastWriteTime}) -lt (Get-Date).AddDays(-1)) {
        Remove-Item -Path "$($tools_path)\working.flag" -Force
        }
    exit
} else {
    New-Item "$($tools_path)\working.flag" -ItemType File
    if (!(Test-Connection -Count 1 themoviedb.org)) {
        echo "ke verbindig. usführe vom script nid möglich"
    }
    else {
        if ((Get-ChildItem $($downloaded_path) -Directory | Measure-Object).Count -gt 1) {
            echo "$($(Get-ChildItem $($downloaded_path) -Directory | Measure-Object).Count) Ordner werden durchsucht"
            foreach ($folder in Get-ChildItem -Path $downloaded_path -Directory) {
                $foldername = echo $folder | Select Name
                $foldername = $foldername -replace "@{Name=",""
                $foldername = $foldername -replace "}",""
                $foldername -match '(?<imdbid>.+)_(?<movie>.+)'
                $imdbid = $Matches.imdbid
                if (((Get-ChildItem -Path $downloaded_path\$foldername -Recurse  -Filter "*.mkv" -Exclude "*sample*.mkv" | Where-Object {$_.Length -gt 1GB} | Measure-Object).Count) -eq 1) {
                    echo "korrekti datei isch gfunde worde..."


                    $WebResponse = Invoke-RestMethod -Uri "https://api.themoviedb.org/3/find/$($imdbid)?api_key=$($tmdb_API_KEY)&external_source=imdb_id&language=de-DE" | ConvertTo-Json
                    $x = $WebResponse | ConvertFrom-Json
                    $x.movie_results[0]
                    $result = $x.movie_results
                    $tmdbmovietitle = $result | select -ExpandProperty title
                    $tmdbmovietitleclear = $tmdbmovietitle -replace ":"," -"
                    $tmdbmovietitleclear = $tmdbmovietitleclear -replace "_"," - "
                    $tmdbmovietitleclear = $tmdbmovietitleclear -replace "'",""
                    $tmdbmovieid = $result | select -ExpandProperty id
                    $tmdbmovierating = $result | select -ExpandProperty vote_average
                    $tmdbmoviedescription = $result | select -ExpandProperty overview
                    $tmdbmovierelease = $result | select -ExpandProperty release_date
                    $tmdbmovierelease -match '(?<year>.+)-(?<month>.+)-(?<day>.+)'
                    $tmdbmoviereleaseyear = $Matches.year
                    #$tmdbmoviereleaseyear = ([datetime]$timestamp = $tmdbmovierelease).year
                    $filename = "$($tmdbmovietitleclear) ($($tmdbmoviereleaseyear))"
                    echo $filename
                    echo $tmdbmovierelease
                    echo $tmdbmoviereleaseyear
                    echo "===================================================================================="
                    echo ""




                    Get-ChildItem -Path $downloaded_path\$foldername -Recurse  -Filter "*.mkv" -Exclude "*sample*.mkv" | Where-Object {$_.Length -gt 1GB} | Copy-Item -Destination "$($renamed_path)\$($filename).mkv"
                    
                    if (Test-Path -Path "$($renamed_path)\$($filename).mkv") {
                        Remove-Item -Path "$($downloaded_path)\$($foldername)" -Recurse -Force

                        
                        HandBrakeCLI --preset-import-file "$($tools_path)\lowmoviesbyelias.json" -Z "lowmoviesbyelias" -i "$($renamed_path)\$($filename).mkv" -o "$($converted_path)\$($filename).mp4"
                        if (Test-Path -Path "$($converted_path)\$($filename).mp4") {
                            Remove-Item -Path "$($renamed_path)\$($filename).mkv" -Force
                            Move-Item -Path "$($converted_path)\$($filename).mp4" -Destination "$($movie_folder)\$($filename).mp4"
                        } else {
                            echo "ds objekt '$($filename)' isch nid korrekt konvertiert worde. di unbenennti datei wird no nid glöscht..."
                            Add-Content "$($log_file)" "$(Get-Date)::::ds objekt '$($filename)' isch nid korrekt konvertiert worde. di unbenennti datei wird no nid glöscht..."
                            $Email.Send($From, $To, "Error: konvertieren", "Beim konvertieren von '$($filename)' ist ein fehler aufgetreten")
                        }

                    } else {
                        Add-Content "$($log_file)" "$(Get-Date)::::ds objekt '$($filename)' isch nid korrekt kopiert worde. dr alt ordner wird no nid glöscht..."
                        echo "ds objekt '$($filename)' isch nid korrekt kopiert worde. dr alt ordner wird no nid glöscht..."
                        $Email.Send($From, $To, "Error: kopieren", "Beim kopieren von '$($filename)' ist ein fehler aufgetreten")
                    }
                
                
                }
                else {
                    echo "$($foldername) het meh als 1 datei wo stimme chönnti" 
                }

            }
        } else {
            Add-Content "$($log_file)" "$(Get-Date)::::Keine Dateien zu bearbeiten"
        }

    }

Remove-Item -Path "$($tools_path)\working.flag" -Force
}





#https://api.themoviedb.org/3/find/tt0468569?api_key=3959d7b0103e3bb40a54e4a82f2671ea&external_source=imdb_id&language=de-DE
