import subprocess
import datetime
import csv
import pandas as pd

# Test rclone call
# rclone copy wasabi:archive-poplar/1B42DE76-C206-4BC2-A6D2-B0B4B9CB6BC8/1B42DE76-C206-4BC2-A6D2-B0B4B9CB6BC8.svs D:\Temp\wasabi_copy\
# rclone copyto wasabi:archive-poplar/1B42DE76-C206-4BC2-A6D2-B0B4B9CB6BC8/1B42DE76-C206-4BC2-A6D2-B0B4B9CB6BC8.svs D:\Temp\wasabi_copy\test01.svs
# rclone ls wasabi:archive-poplar/1B42DE76-C206-4BC2-A6D2-B0B4B9CB6BC8/1B42DE76-C206-4BC2-A6D2-B0B4B9CB6BC8.svs

source_csv = './SlideMoveCSV/TGJ22-0238-0001189_042522.csv'
# source_csv = './SlideMoveCSV/Test1.csv'
src_path = 'wasabi:archive-poplar'
# src_path = 'wasabi:library-research-images'
dest_path = 'D:\\Temp\\wasabi_copy'


def rclone_call(src_path, dest_dir, cmd = 'ls', get_output=False):
    output_msg = 'No file copied'
    print('Start rclone method: ' + str(datetime.datetime.now()))
    if cmd == 'copy':
        command = (['rclone', 'copy', '--progress', src_path, dest_dir])
        output_msg = ' Copied-' + src_path
    elif cmd == 'copyto':
        command = (['rclone', 'copyto', '--progress', src_path, dest_dir])
        output_msg = ' Copied-' + src_path
    elif cmd == 'ls':
        command = (['rclone', 'ls', src_path])
    elif cmd == 'check':
        command = (['rclone', 'check', src_path, dest_dir])

    if get_output:
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        result = subprocess.Popen(command, stderr=subprocess.PIPE)
    output, error = result.communicate()
    output, error = output.decode(), error.decode()

    print('End rclone method: ' + str(datetime.datetime.now()) + ' - ' + output_msg )

    return output, error

# Load Source List of Files CSV
data = pd.read_csv (source_csv)
df = pd.DataFrame(data, columns=['accession', 'imageGuid', 'label', 'block', 'slideNumber', 'case_specimen_description', 'createdAt'])
print('Dataframe record cnt: ' + str(len(df)))


# Loop to parse through each slide in CSV
for idx, row in df.iterrows():
    imageGuid = row['imageGuid']
    specimen_desc = row['case_specimen_description'].strip().replace(' ', '-')
    imageName = str(row['label']) + str(row['block']) + '-' + str(row['slideNumber']) + '_' + specimen_desc + '_' + imageGuid[0:13:1]
    # print(imageName)
    image_src_path = src_path + '/' + imageGuid + '/' + imageGuid + '.svs'
    image_dest_path = dest_path + '/' + imageName + '.svs'

    output, error = rclone_call(image_src_path, image_dest_path, 'copyto', True)
