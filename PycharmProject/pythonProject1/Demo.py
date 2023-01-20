"""
name=input("Enter your name:")
print("your name is "+name)

age=input("enter your age:")
occupation=input("Enter your occupation:")
education=input("Enter your Education:")
experience=input("Enter your Experience:")
print("My name is "+name,"Iam "+age,"years old and I studied "+education, "as a "+occupation,"i have "+experience,"years of experience")
#print('this is your age ',age + 'this is your age ',name )


x= int(input("X amount:"))
y=int(input("Y amount:"))
z=int(input("Z amount:"))
k=x+y+z
print(k)
print('x amount is {} y amount is {} z amount is {} and the total is {}'.format(x,y,z,k))
"""
# creating quiz




score=0
def scorefun():
    global score
    score+=1
    # print(score)

print("Hi,You are here to take a quick quiz \n Good luck")
print("What is the India's largest city in population ? \n 1.Delhi \n 2.Mumbai \n 3.Chennai \n 4.Pune")

Answer1=input("Answer :")
if Answer1=="Mumbai":
  scorefun()
else :
    print(score)

print("Which animal is known as the 'Ship of the Desert'? \n 1.Camel \n 2.Cheeta \n 3.Zeebra \n 4.Dog")
Answer2=input("Answer:")
if Answer2=="Camel":
    scorefun()
else :
    print(score)
print("Does Dolphins sleep with one eye open? \n 1.Yes \n 2.No")
Answer3=input("Answer:")
if Answer3=="Yes":
    scorefun()
else :
    print(score)
print("Who invented cotton candy? \n 1.Scientist \n 2.Chef \n 3.Dentist \n 4.Police")
Answer4=input("Answer:")
if Answer4=="Dentist":
    scorefun()
else :
    print(score)
print("How many hearts does the Octopuses have? \n 1.2 \n 2.3 \n 3.1 \n 4.5")
Answer5=input("Answer:")
if Answer5=="3":
    scorefun()
else :
    print(score)

print("And,your score is ",score)
print("Thank your for your valuable time")










