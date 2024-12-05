import csv

def saveData(all_info):
    with open("newFile.csv","w") as myfile:
        csv_file=csv.writer(myfile)
        csv_file.writerows(all_info)