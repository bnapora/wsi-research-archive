## Workflow Order
1. Identify Accession with desired slides [postgresql]
2. Generate CSV list of slides with GUID for Access [postgresql]
3. Copy slides from Wasabi to Anonymization folder [python script]
    - change filename to desired destination format (eg. BodyPart_Block_GUID)
    Run: `python rclone-moveslide.py`
4. Run svs-deidentifier application
5. Upload images to CAT Server

### Create venv

python3.8 -m venv /workspace/.virtualenvs/wsi-repository


### Misc Scripts to Run RClone

Mount Drive
rclone mount wasabi:library-research-images/ M:
rclone mount wasabi:archive-poplar/ X:

Launch rclone GUI
rclone rcd --rc-web-gui

List buckets in S3 Storage
rclone lsd wasabi:/archive-poplar

List all contents under path:
rclone lsl wasabi:archive-bioref/
rclone lsl wasabi:archive-bioref/FFFF6B37-EC69-472E-B860-733CB8774D40/

rclone lsl wasabi:archive-poplar/013FBA78-3741-4A29-A788-253C981FBCE8/

Copy file from source to destination
rclone copy wasabi:archive-bioref/FFFF6B37-EC69-472E-B860-733CB8774D40/FFFF6B37-EC69-472E-B860-733CB8774D40.svs D:/Temp

gsclone.py -m check -s wasabi:archive-bioref/FFFF6B37-EC69-472E-B860-733CB8774D40/ -d D:/Temp

    command = ([RCLONE, 'move', '--log-file=rclone_upload.log', '--transfers', RCLONE_TRANSFERS, '--drive-chunk-size=16M', '--exclude', 'filepart', LOCAL_DIR + dir + '/', REMOTE_NAME  + REMOTE_DIR + dir + '/'])
    result = subprocess.Popen(command)
    result.communicate()

import subprocess 
process = subprocess.Popen(["rclone", "listremotes"], shell=True, stdin=subprocess.PIPE)
output = process.communicate()
print(output)


process = subprocess.Popen(["rclone", "lsl", "wasabi:archive-bioref/FFFF6B37-EC69-472E-B860-733CB8774D40/"], shell=True, 


