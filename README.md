# IITG_Download
To Download Large Files in IITG

Requirments: Python3 in /usr/local/bin/ folder!
( Download Python3 if you don't have it! )

Instructions to Use:
    Download the Script
    Go to the Downloaded Folder!
    Execute: sudo cp download_file.py /usr/local/bin/dwnfile
    Execute: sudo chmod 755 /usr/local/bin/dwnfile
    
This script basically downloads the files in parts! IITG doesn't allow downloads of file more than 300MB so bydefault size of each part is 300MB, You can manually change the part size by giving the flag --partsize and you can remove the downloaded parts by using --rmparts!

Usage: dwnfile -o filename [--partsize (partsizeinMB) ] url [--rmparts]

PS: This script may have a lot of flaws! Please tell me if you find any :)
