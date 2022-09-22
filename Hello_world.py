# full_name = "Emmanuel Joseph"
# age = 20
# status = "New Patient"
# print(full_name, age, status)
#
# Body = input("What is your weight: ")
# Bag = input("What is the Weight of your Bag: ")
# Total = float(Body) + float(Bag)
# print("Total Weight is :" + str(Total))

weight = float(input("What is your weight: "))
unit = input("Weight in (K)gs or (L)bs: ")
if unit.upper() == "K":
    converted = int(weight) / 0.45
    print("Weight in (L)bs is: " + str(converted))
else:
    converted = int(weight) * 0.45
    print ("Weight in (K)gs is: " + str(converted))