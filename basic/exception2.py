try:

    f = open(r"T:\abc.txt","r")
    
except Exception as ex:
    print(ex)

else:
    print("No exception...")

finally:
    print("Finally block...")

