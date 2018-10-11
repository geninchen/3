#ex.13

from sys import argvscript, first, second, third = argvprint "The script is called:", scriptprint "Your first variable is:", firstprint "Your second variable is:", secondprint "Your third variable is:", third

#ex.17from sys import argvfrom os.path import existsscript, from_file, to_file = argvprint "Copying from %s to %s" % (from_file, to_file)in_file = open(from_file)indata = in_file.read()print "The input file is %d bytes long" % len(indata)print "Does the output file exist? %r" % exists(to_file)print "Ready, hit RETURN to continue, CTRL- C to abort."raw_input()out_file = open(to_file, 'w')out_file.write(indata)print "Alright, all done."out_file.close()in_file.close()

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
def cheese_and_crackers(cheese_count, boxes_of_crackers):	print "You have %d cheeses!" % cheese_count	print "You have %d boxes of crackers!" % boxes_of_crackers	print "Man that's enough for a party!"	print "Get a blanket.\n"print "We can just give the function numbers directly:"cheese_and_crackers(20, 30)print "OR, we can use variables from our script:"amount_of_cheese = 10amount_of_crackers = 50cheese_and_crackers(amount_of_cheese, amount_of_crackers)print "We can even do math inside too:"cheese_and_crackers(10 + 20, 5 + 6)print "And we can combine the two, variables and math:"cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)

#ex.19
def cheese_and_crackers(cheese_count, boxes_of_crackers):    print ("You have %d cheeses!" % cheese_count)    print ("You have %d boxes of crackers!" % boxes_of_crackers)    print ("Man that's enough for a party!")    print ("Get a blanket.\n")    print ("We can just give the function numbers directly:")cheese_and_crackers(20, 30)    print ("OR, we can use variables from our script:")amount_of_cheese = 10amount_of_crackers = 50    cheese_and_crackers(amount_of_cheese, amount_of_crackers)    print ("We can even do math inside too:")cheese_and_crackers(10 + 20, 5 + 6)    print ("And we can combine the two, variables and math:")cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)