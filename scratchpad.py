import subprocess
import datetime
import csv
import pandas as pd

# Load Source List of Files CSV
data = pd.read_csv (r'./SlideMoveCSV/Test1.csv')
df = pd.DataFrame(data, columns=['accession', 'imageGuid', 'label', 'block', 'slideNumber', 'case_specimen_description', 'createdAt'])

for idx, row in df.iterrows():
    imageGuid = row['imageGuid']
    print(imageGuid)