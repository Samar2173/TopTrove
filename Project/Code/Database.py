'''
Student Database
Excel Uploader

'''
import csv
import pandas as pd

class Student():
    def __init__(self, id, name, institution, stream, event, ph):
        self.id = id
        self.name = name
        self.institution = institution
        self.stream = stream
        self.event = event
        self.phone = ph

    def csvWrite(self):
        infoList = [ self.id, self.name, self.institution, self.stream, self.event, self.phone]
        path = r'Files\student_info.csv'
        with open(path, 'a', newline = '') as csv_file:
            writer = csv.writer(csv_file)

            if csv_file.tell() == 0:
                writer.writerow(infoList)
            
            else:
                df = pd.read_csv(path)
                checkList = list(df['Student ID'])
                if self.id in checkList:
                    return "Data already exists"

            writer.writerow(infoList)
            return "Data Added Successfully!!!"

    def csvRead(self, id):
        path = r'Files\student_info.csv'
        df = pd.read_csv(path)
        checkList = list(df['Student ID'])
        if id in checkList:
            index = checkList.index(id)
            return list(df.iloc[index])
        
        return "ID not Found"
