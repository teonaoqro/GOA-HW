# 3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაითვალეთ მომხმარებლის შემოტანილ რიცხვამდე რიცხვების საშუალო არითმეტიკული

num=int(input("enter number"))
number= 0
for i in range(num):
    number = number + i
    number = number / num
print(number)