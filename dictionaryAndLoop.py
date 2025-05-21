"""Create a Python function count_vowels_in_string(s) that counts the number of vowels in a given string. Use a dictionary to store the counts of each vowel. The function should stop counting once it has found all 5 vowels (a, e, i, o, u) using a break statement.
"""
    
def countVowelsInString(mixString):
    dict = {"a":0, "e":0, "i":0, "o":0, "u":0}
    found = set()
    
    for item in mixString:
        if item == "a":
            dict["a"] +=1
            found.add(item)
        elif item == "e":
            dict["e"] +=1
            found.add(item)
        elif item == "i":
            dict["i"] +=1
            found.add(item)
        elif item == "o":
            dict["o"] +=1
            found.add(item)
        elif item == "u":
            dict["u"] +=1
            found.add(item)
        if len(found) == 5:
            break
        
    print (dict)
        
myString = (input ("Please insert anything: ")).lower()
countVowelsInString(myString)