# PART 12 - Booleans and combining conditions

#boolean is a value that is either true or false.  every if test problems produces one

#rent = 5000
#print(rent > 4000)
#print(rent > 9000)

#combine conditions with and, or, not
# and > both must be true
# or > at least one must be true
# not > flips

#rent = 5000
#if rent > 1000 and rent < 10000:
#    print("in range")
#
#status ="active"
#if status == "active" or status == "pending":
#    print("counts as current")

# PART 13 - none - nothing here yet value

# none is pythons way of saying no value/empty/not set.  its not 0
# and not "" - it specifically means nothing

#best = None
#if best is None:
#    print("nothing yet")

# PART 14 - sorting and the key=lambda pattern

# 14.1 sorted() puts a list in order

#nums = [3,1,2]
#print(sorted(nums))
#print(sorted(nums,reverse=True))

#14.2 sorting by a specific field key = lambda

#when your list holds pairs or dicts, you must tell sorted what to sort by
#thats what key= does.  A lambda is a tiny thoraway function that says given one item heres the value to sort on

#pairs = [("loblaw", 30), ("shoppers",10), ("apple",20)]
#top = sorted(pairs, key=lambda x: x[1], reverse=True)
#print(top)

#reading: key=lambda x: x[1] > for each item call it x and sort by x[1] (the second element).
#lambda is just a mini function with no name. 

# PART 15 - every day tools

#15.1 - range()
#for i in range(3):
#    print(i)

#useful when you repeat something a number of times

#15.2 - enumerate()

#tenants = ["loblaw", "shoppers", "apple"]
#for i, name in enumerate(tenants):
#    print(i, name)

#enumerate hands you both the position i and the item name > tuple unpacking

# 15.3 set() - unique values only

#cities = ["toronto", "toronto", "ottawa"]
#print(set(cities))
#print(len(set(cities)))

# 15.4 while - repeat until a condition changes

#count = 0
#while count < 3:
#    print(count)
#    count += 1
#
#make sure something inside changes or it forever loops

# PART 16 - tuple unpacking: splitting several values at once

#pair = ("loblaw", 5000)
#name, rent = pair
#print(name)
#print(rent)
#print(pair)

#the number of names must match the number of values
