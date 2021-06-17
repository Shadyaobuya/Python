
# Given list x = [100,110,120,130,140,150], use list comprehension to create another 
# list containing each number in the list multiplied by 5.  
x = [100,110,120,130,140,150]
y=[i*5 for i in x]
print(y)

# Write a function named divisible_by_three that accepts a number n and prints all 
# numbers from 1 to n that are divisible by 3. 

def divisible_by_three(n):
    for number in range(1,n+1):
        if number %3==0:
            print(number)

divisible_by_three(15)

# Given the nested list x = [[1,2],[3,4],[5,6]], 
# write a function that flattens the list and returns it as [1,2,3,4,5,6]

x = [[1,2],[3,4],[5,6]]


def flatten_list():
    # for num in z:
    #     for numb in num:
    #         print(numb,end='')
    a=[num for numb in x for num in numb]
    print(a)

flatten_list()


# Write a Python function named smallest that accepts a 
# list of unsorted integers and returns the smallest number in the list. Example:
# smallest([3,6,8,2,4,1,5,7]) returns 1

def smallest(all_numbers):
    minimum=min(all_numbers) 
    print(minimum)

smallest(all_numbers=[3,6,8,2,4,1,5,7])


# Write a function that accepts list x below and uses a set 
# to remove the duplicate letters and returns the list without duplicates
# m = ['a','b','a','e','d','b','c','e','f','g','h']
x= ['a','b','a','e','d','b','c','e','f','g','h']
def remove_duplicates(x):
    print(set(x))
remove_duplicates(x=x)

# Write a function named divisible_by_seven that; 
# using the range function and a for loop returns a list containing 
# all the numbers between 100 and 200 that are divisible by 7.

def divisible_by_seven():
    divisibility=[]
    for numbs in range(100,200):
        if numbs%7==0:
            divisibility.append(numbs)
    print(divisibility)

divisible_by_seven()

# Given this list of students containing age and name,  
# students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, 
# {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}], 
# write a function that greets each student and tells them the year they were born. 
# e.g Hello Eunice, you were born in the year 2002.

students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"},{"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
def greeting():
    for student in students:
        print("Hello {}, you were born in the year {}".format(student['name'],2021-student['age']))

greeting()



# Create a Class Rectangle with the following Attributes and Methods
# Attributes: The class has attributes width and length that represent the two sides of a rectangle 
# Methods:
#  Add a method named area which returns the area (A) of the rectangle using the formula A=width*length
# Add a method named perimeter which returns the perimeter (P) of the 
# rectangle using the formula P=2(length+width)

class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        A=self.width*self.length
        return A
    def perimeter(self):
        P=2*(self.length+self.width)
        return P


rectangle=Rectangle(4,6)
print(rectangle.area())
print(rectangle.perimeter())
