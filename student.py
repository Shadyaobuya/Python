
class Student():
    school="AkiraChix"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self):
        return "hello my name is {}. I am {} years old. I love {}".format(self.name,self.age,self.school)

#To create a class in python use a class keyword
# Save your document/module using a py extensionclass name starts with a capital letter 
# No spaces
# Use a class to create objects or instances of that class


# Using list comprehension, find the squares of only 
# odd numbers and append them to an empty list. 

lisst=[1,2,3,4,5,6,7,8,9]
# oddsquares=[]
# for i in lisst:
#     if i%2!=0:
#         oddsquares.append(i**2)
# print(oddsquares)

# squares=[i**2 for i in lisst if i%2!=0]
# print(squares)
lisst.sort(reverse=True)
print(lisst)