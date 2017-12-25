# -*- coding: UTF-8 -*-
import csv

def get_key_pair(discription="test"):
    f=open('API_list.csv','r')
    reader=csv.reader(f)
    result=[]
    for row in reader:
        if row[9]==discription:
            result= [row[7],row[8],row[3]]
    f.close()
    return result

class Account:
    def __init__(self, description="test"):
        key_pair=get_key_pair(description)
        self.api_key=key_pair[0]
        self.secret_key=key_pair[1]
        self.description=description
        self.name=key_pair[2]


