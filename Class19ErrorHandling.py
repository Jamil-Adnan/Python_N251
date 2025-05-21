while True:
    try:
        number = int(input("Insert a number: "))
        if number == 0 :
            number = number / 0
        else:
            print (number)
            break  
    
    except ValueError:
        print ("Eror! Please insert an integer")
    except ZeroDivisionError:
        print ("Error! Can not divide by Zero")
        

