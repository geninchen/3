#ex.13

from sys import argv

#ex.17

#ex.18
def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
     
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
     
def print_one(arg1):
    print ("arg1: %r" % arg1)
     
def print_none():
    print ("I got nothin'.")
     
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
  File "<input>", line 5
    def print_two_again(arg1, arg2):
        
#ex.19
def cheese_and_crackers(cheese_count, boxes_of_crackers):

#ex.19
def cheese_and_crackers(cheese_count, boxes_of_crackers):