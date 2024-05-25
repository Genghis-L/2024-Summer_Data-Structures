import pickle as pk
from Worksheet_3_Employee_Management_System import *
f = open('employees.pkl','rb')
info = pk.load(f)
print(info)