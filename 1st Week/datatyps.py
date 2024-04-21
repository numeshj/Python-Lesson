x = "Python{}"
y = '\n Hello World----'


z = """\n Hello World
this we call doc strings
we can put paragraphs"""

# print(x)

# Checked the type

# print(type(x))


# print(type(x),x)

# print(x,y,z)

# print(x[4])
# print(x[-2])

a = "eliphant"

# print(type(a))

# print(x.format(a))

# print(x+y+str(a))

# print(f"Numesh {a}")

b=0.0

# print(type(b))

# print("Gifthub Configer")

# List

l1 = [1,2,3,4,"Numesh",0.0]

# print(l1)

# print(l1[0:4])

# print(len(l1))

# tuple 

tuple = (1,2,3,4,)

# print(tuple)

is_created = False
is_failed = True

# print(is_created,type(is_created))

if 2 >0:
    is_created=True
    
# print(is_created)

set1 = set([1,2,3,3,"Numesh", "Numesh"])

# print (set1)

dict={}
dict1={
    "Name":"Numesh",
    "Age" : 34,
    "Add" : "Galle"   
}

dict2 ={
        "Name":"Janith",
    "Age" : 30,
    "Add" : "Unawatuna"   
}


# print(dict1["Age"])
list = []

list.append(dict1)
list.append(dict2)
# print(list)

import pandas as pd

df = pd.DataFrame(list)
print(df.head())
print(type(df))