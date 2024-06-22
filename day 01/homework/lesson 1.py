name ="teona"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "teona"არის ცვლადისთვის მნიშვნელობა

print(name)
surname = "oqropilashvili"
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი


name = "teona" #ეს არის str(string)ტიპის ცვლადი
age =31 #ეს არის int (integer)მთელი რიცხვი
height = 170.0 #ეს არის float ტიპის ცვლადი(ათწილადი)
#boolean (bool) ტიპის ცვლადი

knows_programming = True #true ან falce
is_ugly = False  #snakecase(უბრალოდ წერის სტილი სტანდარტულად)

isUgly = False # ჯავასკრიპტული camelcase

print(name + " " + surname)
#STRING არის ბრჭყალებში მოქცეული სიმბოლო
#PRINT(name + age)

#print(type(age))
#print(type(name))
#print(type(surname))
#print(type(height))
#print(type(knows_programming))

print(name + " " + str(age))
print(name + " " + surname + " " + str(age) + " " + str(height))