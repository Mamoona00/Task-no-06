#Task no 06
#Variables

a = 12
print(a)
name = "Hooria"
print(name)

#expression
x = 4
y = x * 3
print(y)

x = 4
y = 9
z = x + y
print(z)
z = x * y
print(z)

#condition
a = 20
b = 10
if  a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")

#functions
n = "Mamoona"
def name():
    print("My name is: ", n)
name()

marks = 5 
def fp():
    if marks > 30:
        print("pass")
    else:
        print("fail")
fp()


#maximum possible value of int
n = 11111112345444768855998000
print(type(n))
import sys

print(sys.maxsize)
print(type(sys.maxsize))

#global and local variables in python
def lv():
    local_var = 'Python'
    print(local_var)
lv()

global_var = 10

def gl():
    print(global_var)
gl()
print(global_var)

#packing ad unpacking arguments 

def pack(*arg):
    print(arg)         #packing for list
     
pack(8,9,10)

# for dictionary
def pack(**kwarg):
    print(kwarg)         
     
pack = {'a': 8 ,'b': 9 , 'c': 10}

#upacking for list
def unpack(a,h,z,n):
    print(a,h,z,n)                          

tuple(1,2,3,4)
unpack(*list)             

 #for dictionary
dict = {'a': 'Amina' , 'h': 'Hamza' , 'z': 'Zain', 'n': 'Namra'}       
unpack(**dict) 

#type conversion in python

a = 7.5
a = int(7.5)           #float to int
print(a)
print(type(a))

n = 45
n = str(24)
print(n)             #int to string
print(type(n))

c = "75"
c = int("75")            #string to int
print(type(c))

a = (1,2,3,4)             
print(type(a))
a = [1,2,3,4]            #tuple to list
print(type(a))

#Byte object vs string
s = "Hey! How are You?"
print(type(s))
b = b"Hello world"
print(type(b))
s = b.decode('utf-8')                   #converting byte to string
print(s)

b = s.encode('utf-8')                    #coverting string to byte
print(b)






#print single and multiple variable
 #print() function
a = 'Haala'
print(a)     #single                  

name , age  , salary = 'Mahnoor' , 23 , 30000
print(name ,age ,salary)                     #multiple

#concatenation
a = "Haala"
print("Name is: " , a)           #single

a = 'moon'
b = 'artwork'
print("My store name:" , a,b)       #multiple


name = "Haala"
print(f"My name is: {name}")         #f-string


#swap variables
a = 'juice'
b = 'cold drink'
temp = a                    #with temp variable
a = b
b = temp
print("After swapping: ",  a , b)

x = 4
y = 7
x,y = y,x                          #with tuple unpacking
print(x)
print(y) 

m = 40
n = 50
m = m ^ n                  #XOR
n = m ^ n
m = m ^ n
print(m,n)

#__name__ variable
import name
def sv():
    print("name.special_var")

print(__name__)






