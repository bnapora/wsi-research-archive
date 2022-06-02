import subprocess
import datetime
import csv

# src_path = 'wasabi:archive-bioref/FFFF6B37-EC69-472E-B860-733CB8774D40/'
# src_path = 'wasabi:archive-bioref'
# src_path = 'wasabi:archive-poplar'
src_path = 'wasabi:library-research-images'
dest_path = 'D:/Temp'

# command = (['rclone', 'lsl', 'wasabi:archive-bioref/FFFF6B37-EC69-472E-B860-733CB8774D40/'])
# command = (['rclone', 'ls', src_path, '--separator "/"'])

# process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, error = process.communicate()

def rclone_call(src_path, dest_dir, cmd = 'ls', get_output=False):
    """ Function
       rclone calls
    """
    print('Start rclone method: ' + str(datetime.datetime.now()))
    if cmd == 'copy':
        command = (['rclone', 'copy', '--progress', src_path, dest_dir])
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

    print('End rclone method: ' + str(datetime.datetime.now()))

    return output, error

output, error = rclone_call(src_path, dest_path, 'ls', True)

# Split each converted byte string by \n delimiter
output_list = output.split('\n')
output_list_tmp = output_list
print('Output_list - after split: ' + str(len(output_list)))

# Clean raw list of values: remove duplicate files, remove non SVS files
duplicates_list = []
for i, item in enumerate(output_list):
    if '. (1)' in item:
        duplicates_list.append(item)
        output_list.pop(i)
print('Output_list - after remove dupes: ' + str(len(output_list)))

# csv_fields = ['Entry']
# with open('GFG', 'w') as f:
#     write = csv.writer(f)
#     write.writerow(csv_fields)
#     write.writerows(duplicates_list)

# Clean raw list of values: remove non SVS files
svs_list = []
for i, item in enumerate(output_list):
    if '.svs' in item:
        # print(i)
        # print(item)
        svs_list.append(item)
print('Output_list - after non-svs: ' + str(len(svs_list)))

# Split size and file values into lists
size_list = [] 
file_list = []
for item in svs_list:
    item = item.strip()
    if len(item) > 3:
        size, file = item.split(' ')
        size_list.append(size)
        file_list.append(file)
#
# svs_list = []
# for svs in file_list:
#     if '.svs' in svs:
#         svs_list.append(svs)

print('Count of SVS List: ' + str(len(file_list)))
# print(svs_list)


# print('Printing Output...')
# print(output)
# print('Printing Errors...')
# print(error)



