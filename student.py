
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

