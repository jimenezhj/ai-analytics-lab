# PART 9 - growing a list: .append()

# you often start with an empty list and add as you go using .append() at the end

#rents = [5000,8000]
#rents.append(3000)
#print(rents)

# common pattern of blank slate

#names = []
#names.append("loblaws")
#names.append("shoppers")
#print(names)

#something = [] then .append() inside a loop is how you collect reults

# PART 10 - two everyday helpers .split() and .get()

#10.1 .split() break text into pieces

#date = "2029-12-31"
#parts = date.split("-")
#print(parts)
#print(parts[0])

#date.split() cut the text at each; parts[0] grabs the first piece.

#10.2 .get() - look up a dict key safely

#lease = {"tenant":"loblaws"}
#print(lease.get("rent",0))
#print(lease.get("tenant",0))

# PART 11 - functions - naming a reusable action

#11.1

#def annual(monthly):
#    return monthly*12
#
#print(annual(5000))

#def annual(monthly) > define a function named annual that takes on input which 
# will be called monthly
#return monthly*12 > the indented body means hand back what i defined as monthly
# and multiply by 12
#print(annual(5000)) - call the function, input 5000 and multiply by 12

#def greet(name):
#    return f"Hello {name}"
#
#print(greet("Tyrion"))

#11.2 - two inputs

#def rent_psf(rent,sqft):
#    return(rent*12)/sqft
#
#print(rent_psf(5000,3000))

#PART 12 - booleans and combining conditions

#rent = 5000
#print(rent > 4000)
#print(rent > 9000)

#combine conditions with and, or, not

#rent = 5000
#if rent > 1000 and rent < 10000:
#    print("in range")

#status ="active"
#if status == "active" or status =="pending":
#    print("counts as current")

