Function RutaHash512{
Get-ChildItem C:\users\alvar\onedrive\desktop\PIA -Recurse |
Get-FileHash -Algorithm SHA512 |
Export-Csv -Path C:\Users\alvar\OneDrive\Desktop\PIA\hashes.csv -NoTypeInformation
Import-Csv -Path C:\Users\alvar\OneDrive\Desktop\PIA\hashes.csv
}

RutaHash512