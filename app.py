import csv 
data=[]
with open("dataset_2.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
headers=data[0]
planet_data=data[1:]

#Converting all planet name to lower case
for data_point in planet_data:
    data_point[2]=data_point[2].lower()

#Sorting planet name in alphabetical order
planet_data.sort(key=lambda planet_data:planet_data[2])

with open("planet_dataset_2_sorted.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
