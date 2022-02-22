import csv
from textwrap import indent
import pandas as pd
import os
import glob
import json
import csv

def Excel_to_csv_converter():
    excel_list = glob.glob(os.path.join('*.xlsx'))
    excel_list.sort()
    converted_file_prefix = 'file'
    index=0
    for file in excel_list:
        df = pd.read_excel(file)
        df.to_csv(converted_file_prefix+str(index)+".csv")
        index+=1

for i in range(2):
    csv_file = f"file{i}.csv"
    with open(csv_file,"r") as f:
        reader=csv.reader(f)
        next(reader)
        data={}
        for row in reader:
            data[row[1]] = row[2]
    if i==0:
        age=data
    elif i==1:
        gender = data
    

with open("file2.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    data={}
    i=1
    for row in reader:
        data[i] = {
            "id": row[1],
            "Name":row[2],
            "Age":row[3],
            "Gender":row[4]
        }
        i+=1
    parent = data

result = []
for p in parent:
    values = parent[p]
    data={
        "Id": values['id'],
        "Name":values["Name"]
    }
    if 0<=int(values['Age'])<=25:
        age_range = '0-25'
    elif 26<=int(values['Age'])<=50:
        age_range='26-50'
    elif 51<=int(values['Age'])<=75:
        age_range='51-75'
    else:
        age_range = '76-100'
    aconc = int(float(age[age_range])*100)
    gconc = int(float(gender[values["Gender"]])*100)
    tconc = aconc+gconc
    data['TotalConcession'] = str(tconc)
    result.append(data)
print(result)

with open("Output_json.json","w") as f:
    json.dump(result,f,indent=4)