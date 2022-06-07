import subprocess
import datetime
import csv
import pandas as pd

# Set initial variables
source_csv = './SlideMoveCSV/pop-imagelist_060722.csv'
src_path = 'wasabi:archive-poplar/'
dest_path_root = '/host_Data/DataSets/wasabi_archive-pop/'

# Rclone Generic Function
def rclone_call(src_path, dest_dir, cmd = 'ls', get_output=False):
    output_msg = 'No file copied'
    print('Start rclone method: ' + cmd + '- ' + src_path + ' | ' + str(datetime.datetime.now()))
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

    print('End rclone method: ' + dest_dir + ' | ' + str(datetime.datetime.now()))

    return output, error

# Load Source List of Files CSV
data = pd.read_csv (source_csv)
df = pd.DataFrame(data, columns=['accession', 'imageGuid', 'label', 'block', 'slideNumber', 'case_specimen_description', 'createdAt'])
print('Dataframe record cnt: ' + str(len(df)))


# Loop to parse through each slide in CSV
for idx, row in df.iterrows():
    accession = row['accession']
    imageGuid = row['imageGuid']
    specimen_desc = row['case_specimen_description'].strip().replace(' ', '-')[0:21]
    imageName = str(row['label']) + str(row['block']) + '-' + str(row['slideNumber']) + '_' + specimen_desc + '_' + imageGuid.split('-')[4]
  
    image_src_path = src_path + imageGuid + '/' + imageGuid + '.svs'
    image_dest_path = dest_path_root + accession +'/' +  imageName + '.svs'

    output, error = rclone_call(image_src_path, image_dest_path, 'copyto', True)


