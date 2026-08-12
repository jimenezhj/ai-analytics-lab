## 3.2 — Reach into a list by position (starts at 0!)

#Each item has a position number. **Python counts from 0, not 1.** This trips up every single beginner — the first item is position 0.

#rents = [5000,8000,3000]
#print(rents[0])
#print(rents[1])
#print(rents[2])

#Shows `5000`, then `8000`, then `3000`.
#- `rents[0]` = first item (position zero)
#- `rents[1]` = second item
#- `rents[2]` = third item

## 3.3 — How many items? `len()`

#print(len(rents)) #shows 3. Len() means lenth - how may items are in the list

# PART 4 — The big one: loops (doing something to every item)
#This is for l in list 

## 4.1 — What a loop is, in plain English
#A loop does the same thing to every item in a list, one at a time, automatically
#Instead of writing the same line over and over, you write it once and python repeats for every item

## 4.2 — Your first loop
# 
#for r in rents:
#    print(r) 

#how to read?
# for > repeat the following for
# r > in this case means a temp box.  Each time around, python puts the next item into "r". 
# r > arbitrary - can be anything user chooses
# in rents > means each item in the list called "rents"
# : > means here comes what you need to repeat
# print(r) > the indented line in this scenario is what gets repeated.  Spaces matter.
# So for 'r in rents:' means go through 'rents' one at a time.  Each time, call that item 'r' and do the indented stuff that follows

#for r in rents:
#    print("This rent is:")
#    print(r)

## 4.3 — The indent is not decoration — it's the grammar

#The spaces in front of print(r) tells python that this line belongs to the loop.
#Indented = inside the loop(repeated). Not indented = outside the loop (run once).

#for r in rents:
#    print(r) #indented, runs for every item in the list
#print("All Done") # runs once

## 4.4 — Loops + `+=` = counting and summing (the payoff)

#combining the two concepts

#rents = [1000,2000,3000]
#total = 0
#
#for r in rents:
#    total += r
#print(total)

#total starts at 0
#for loop, first loop r = 1000, which meants total = total + 1000 
#2nd loop r = 2000, which means total(from the line before which is 1000), r is 2000:
#2nd loop now does total = total(1000) + r(2000) which is now 3000
#last loop representing 3rd r = 3000, total = total (3000) + r(3000) = 6000

#this is the SUM() built by hand, individually, += piles it into the running total for every item in the loop

#count = 0
#
#for r in rents:
#    count += 1
#print(count)

#this prints 3, your starting from zero and adding 1 for every item in the list

#test

#rents = [100,200,300,400]
#count = 0
#total = 0
#for r in rents:
#    count += 1
#    total += r
#print(f"Number of rents: {count} & total rent is: {total}")

# in the test above, there are 4 items in rents, so count will sum to 4
# for every loop, r equals each item in the list and adds them one at a time as a running total

#PART 5 - Dictionaries: Labeled storage

##5.1 - a dict stores things by name, not position

# a list finds things by position (rents[0]).  A dictionary(dict) finds things by a name
#the user chooses called a "Key".  You make one with curly braces {} as Key:value pairs.

#lease = {"tenant":"Loblaw", "rent": 5000}
#
#print(lease["tenant"])
#print(lease["rent"])

# lease["tenant"] means give me the value stored under "tenant"
# instead of remember tenant is at position 0, just call the name

## 5.2 — A list of dicts = a table

# putting several dicts in a list, youll have a row with named columns

#leases = [
#    {"tenant":"loblaw", "rent": 5000},
#    {"tenant":"Shoppers", "rent": 2000}
#]
#
#for l in leases:
#    print(l["tenant"])

#reading the loop: for every item in l (in this case 2 items = 2 dicts), print that item's
#"tenant" field.  leases is now a list of dicts, every time around, l is one item/row.
#now you are asking python for each item/row, find l["tenant"] key and print its value (row)

#total = 0
#count = 0
#
#for l in leases:
#    count += 1
#    total += l["rent"]
#print(f"There is/are {count} tenant/s with a total of {total} in rents")

## 5.3 - Grouping: a dict that accumulates

#here is the pattern to get total per group. You use a dict where the "key" is the group
# and value is that group's running total

leases = [
    {"tenant":"loblaw", "rent": 1000},
    {"tenant": "shoppers", "rent": 2000},
    {"tenant": "loblaw", "rent": 3000}
]

totals = {}

for l in leases: #counting 3 dicts, so should be 3 go arounds
    tenant = l["tenant"]
    if tenant not in totals:
        totals[tenant] = 0
    totals[tenant] += l["rent"]
print(totals)

