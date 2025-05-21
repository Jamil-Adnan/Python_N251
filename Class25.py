# json module()
# import json
from openpyxl import workbook, load_workbook 
myfile = load_workbook("myfile.xlsx")
sheet = myfile.active
print (sheet.title)
print (sheet['A1'].value, sheet['B1'].value, sheet ['C1'].value, sheet ['D1'].value, )