rent = int(input("enter the room rent: "))
food = int(input("enter the food order: "))
electricty = float(input("enter the total electricty unit: "))
charj_unit = float(input("enter the charj pr unit:= "))
person =float(input("enter the roop rent per person:= "))

totalbill = electricty *  charj_unit
output=(food + rent + totalbill)/person
print("each person pay will be ", output)

