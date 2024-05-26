import pickle as pk
from Worksheet_3_Employee_Management_System import *
f = open('/Users/kehanluo/Documents/GitHub/2024_Summer_Data-Structures/2. OOP/employees.pkl','rb')
info = pk.load(f)
print(info)
