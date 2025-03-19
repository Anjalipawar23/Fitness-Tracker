# Health Management System
# 3 clients - Harry, Rohan and Hammad

# def getdate():
#     import datetime
#     return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client
import datetime
def getdate():
    return datetime.datetime.now()
def take(t):
    if t ==1:
        c= int(input("Enter 1 for exercise or 2 for diet:"))
        if c == 1:
            value = input("\n Type here:")
            with open("harry-ex.txt", "a") as op:
                op.write(str([str(getdate())])+": "+value+ "\n")
            print("Successfully Written:")
        elif c == 2:
            value = input("Type here:\n")
            with open("harry-di.txt", "a") as op:
                op.write(str([str(getdate())])+": " + value+ "\n")
            print("Successfully Written:")
    elif t == 2:
        c= int(input("Enter 1 for exercise or 2 for diet:"))
        if c ==1:
            value= input("Type here: \n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully Written")
        elif c == 2:
            value= input("Type here: \n")
            with open("rohan-di.txt", "a") as op:
                op.write(str([str(getdate())])+":"+value+"\n")
            print("Successfully Written")
    elif t == 3:
        c= int(input("Enter 1 for exercise or 2 for diet:"))
        if c == 1:
            value= input("Type here: \n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully Written")
        elif c == 2:
            value= input("Type here: \n")
            with open("hammad-di.txt", "a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully Written")
    else:
        print("Invalid Input!!!")
def give(t):
    if t == 1:
        c = int(input("Enter the values 1 for exercise or 2 for diet:"))
        if c == 1:
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c == 2:
            with open("harry-di.txt") as op:
                for i in op:
                    print(i, end="")
    elif t == 2:
        c = int(input("Enter the values 1 for exercise or 2 for diet:"))
        if c == 1:
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("rohan-di.txt") as op:
                for i in op:
                    print(i,end="")
    elif t ==3:
        c =int(input("Enter the values 1 for exercise or 2 for diet:"))
        if c == 1:
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("you have entered wrong input!!!")


c=int(input("Enter the 1 for log the value and 2 for retrieve:"))
if c ==1:
   b=int(input("Enter the values: 1(Harry), 2(Rohan), 3(Hammad):-"))
   take(b)
else:
    b=int(input("Enter the values: 1(Harry), 2(Rohan), 3(Hammad):-"))
    give(b)