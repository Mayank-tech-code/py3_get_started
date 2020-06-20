signal_value = input("What is the traffic light showing?")
if signal_value.lower() == "green":
    print("Drive past the signal.")
elif signal_value.lower() == "orange":
    print("Wait if you are away from the signal. Cross if you have already crossed the signal.")
elif signal_value.lower() == "red":
    print("Wait")
else:
    print("Please enter a valid value")