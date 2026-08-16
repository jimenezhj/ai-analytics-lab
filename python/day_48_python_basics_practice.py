# PART 17 - loading extra tools: import

#import math
#print(math.sqrt(16))

#from collections import defaultdict
#totals = defaultdict(float)
#totals["loblaw"] += 5000
#totals["loblaw"] += 3000
#print(totals["loblaw"])

#defaultdict is a dict that auto creates a starting value the first time you touch a key
#this skips the "if key not in totals:totals [key]=0"

# PART 18 - list comprehensions - a compact loop

# a list comprehension builds a new list in one line. 

#doubled =[]
#
#for n in [1,2,3]:
#    doubled.append(n*2)
#print(doubled)
#
#doubled2 = [n*2 for n in [1,2,3]]
#print(doubled2)
#
#big = [n for n in [1,2,3,4] if n>2]
#print(big)

# PART 19 - reading

#def annual(monthly):
#    return monthly * 12
#
#leases = [
#    {"tenant":"loblaws", "rent":5000, "status":"active"},
#    {"tenant":"lcbo", "rent":3000, "status":"expired"},
#    {"tenant":"shoppers", "rent":8000, "status":"active"},
#]
#
#total = 0
#for l in leases:
#    if l["status"] == "active":
#        total += annual(l["rent"])
#print(f"total active annual rentL ${total}")