F_Name = input("Please enter your first name :")
L_Name = input("Please enter your last name :")
age = int(input("Please enter your age :"))
birth = int(input("Please enter your date of year :"))

mylist=[F_Name, L_Name, age, birth]

for i in range(0, len(mylist)):
 print(mylist[i])

if age < 18:
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")