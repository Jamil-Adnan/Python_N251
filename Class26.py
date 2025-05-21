import re
pattern = (r'[a-z|A-Z]+[0-9]*_*\.*[a-z|A-Z]*[0-9]*@[a-z|A-Z]+[0-9]*\.[a-z|A-Z]+$')
email = input ("Please insert your email adress: ")
validate = re.findall(pattern, email)
print(validate)



"""
import open write and save an excel file
"""


from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment   
myfile = load_workbook("myfile.xlsx")
sheet = myfile.active
sheet['A8'] = "Arham"
sheet['A9'] = "Arfa"

sheet['B8'] = 15
sheet['B8'].alignment = Alignment(horizontal='center', vertical = 'center')

sheet['B9'] = 13
sheet['B9'].alignment = Alignment(horizontal = 'center', vertical = 'center')

myfile.save("myfile.xlsx")
myfile.close()
