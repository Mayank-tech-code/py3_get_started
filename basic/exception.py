try:

    result = 1/0
    #result = 1/1
    
except Exception as ex:
    print(ex)

else:
    print("No exception...")

finally:
    print("Finally block...")

