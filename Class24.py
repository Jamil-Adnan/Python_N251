#Regular expression (RegEx)
import re

# text = "My name is adnan."
# sp = text.split("a")
# print (sp)
# testText = "Abul Hashem 3 Abul Kalam"
# splitttedText = ("[0-9]")

testText= "Khulna Metro GHA 12-1024"

pattern = r'[a-zA-Z]+ [a-zA-Z]+ [A-Z]+ \d{2}[-]\d{4}$'

sp = re.findall(pattern, testText)
print (sp)