import a as a

print('hello world')
a=10
a= float(a)   # convert int as float
b=8
print(type(b))
# To find which one is bigger
if a==b :
    print("equal")
print(a)
print(b)
if(a>b) :
    print('a is bigger')
if(b>a) :
    print('b is bigger')
y='vani'
print(type(y))
print(y)
"""
print a
print b
print y
"""
x= int(2)
y= str(6)
z= float(5)
print(x)
print(y)
print(z)
s,t=5,9
print('s is %d  ' % (s) ,'u is %d'%(t) )
y = u = 'apple'
print(y,u)
#collection
apple=['red','green']
x,y = apple
print(x,y)
#simple
fruit ='apple'
def fun():
    fruit = 'banana'  # cannot use outside of the func
    global f  # global variable can be use outside iof the function
    f='canberry'
    print("i dont like " + fruit)
fun()
print("i like " +fruit)
print(f)
range=range(6)
print(range)  # print range data type
para="""india is my country 
all INDIANS are my brothers and sisters
I love my country"""
print(para)
print(para[:4][:8])
print(len(para))  # length of the variable
print("brothers" in para)  # to check whether that particular letter present in the variable or not
print("girl" in para)  # to check whether that particular letter present in the variable or not
if "sisters" in para :
    print("yes")
if "donkey" not in para :
    print("no")
print(para[4:10])
print(para[:6])
print(para[:])
print(para.upper())  # to print the string in upper case
print(para.lower())   # to print the string in lower case
print(para.strip())
print(para.replace("sisters","sister"))
# format (to concatenate string and int
age=6
std=1
choclates=10
sentence = " iam vani,{} years old,studying in {} standard,I have {} choclates"
print(sentence.format(age,std,choclates))
# list
veg=["carrot","potato",99.99,"tomato"]
print(veg)
veg[2]="ginger"
print(veg)
veg.pop(0)  # to delete particular data
print(veg)
#veg.clear()  # to clear whole list

"""for y in "anaconda":
    print(y)  # seperated singla character in new line"""
veg=["carrot","potato","onion","tomato"]
for v in veg :
    print(v)
    print(len(v))


######################








