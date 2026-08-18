# Strings, numbers, operators and conditionals

#rent = 40000
#
#if rent > 50000:
#    tier = "anchor"
#elif rent > 10000:
#    tier = "major"
#else:
#    tier = "standard"
#
#print(f"Rent is ${rent}; tier = {tier}")

#print(10 / 3)
#print(10 // 3)
#print(10 % 3)

#print("5" + "5")
#print(5+5)

#print(int("5")+5)

#rent = 5000
#if rent > 4000:
#    print("high")
#else:
#    print("low")

#comparison operators
#print(5>3)
#print(5==5)
#print(5 != 4 )
#print("acme" == "Acme")

#logical operators

#print(True and False)
#print(True or False)
#print(not True)

#examples
#rent = 15000
#status = "active"
#print(rent > 10000 and status == "active")

#conditional statements
#monthly_rent = 22500
#
#if monthly_rent >= 50000:
#    tier = "ach"
#elif monthly_rent >= 15000:
#    tier = "maj"
#elif monthly_rent >= 5000:
#    tier = "standard"
#else:
#    tier = "small"
#
#print(f"rent of {monthly_rent:,} is in the {tier} tier")

#nested conditions
#months_remaining = 30
#status = "active"
#
#if status == "active":
#    if months_remaining <= 6:
#        urgency = "critical"
#    elif months_remaining <=12:
#        urgency = "urgent"
#    else:
#        urgency = "normal"
#else:
#    urgency = "n/a"
#
#print(f"Urgency: {urgency}")

#combined conditions
#lease = "loblaws"
#status = "active"
#expiry = 4
#
#if status == "active" and expiry <= 6:
#    print(f"this lease {lease} needs immediate attention!")

#string functions
#property = "    eglinton gate   "
#print(property.strip())
#print(property.strip().lower())
#print(property.strip().upper())
#print("eglinton" in property)
#print(property.strip().replace("gate", "towers"))

#splitting strings
#address = "2300 richmond ave, toronto, ON"
#parts = address.split(", ")
#print(parts)
#print(parts[0])

#number formatting in f-strings
#revenue = 1250000.5678
#rrevenue = round(revenue,2)
#print(f"Revenue: ${rrevenue:,.2f}")
#print(f"Revenue: ${rrevenue:,.0f}")

#type conversions
#year_text = "2024"
#year_numb = int(year_text)
#print(year_numb + 1)

#price_txt = "12500.75"
#price_num = float(price_txt)
#print(price_num*12)

#some_num = 42
#some_text = str(some_num)
#print("Answer is " + some_text)

#self test
#1. Write a script that defines a variable `
#months_remaining = X` (pick a number) and prints one of these messages:
#   - "Critical: <= 6 months"
#   - "Urgent: 7-12 months"
#   - "Upcoming: 13-24 months"
#   - "Future: > 24 months"

#months_remaining = 25
#
#if months_remaining <= 6:
#    print("critical")
#elif months_remaining <= 12:
#    print("urgent")
#elif months_remaining <= 24:
#    print("upcoming")
#else:
#    print("future")

#   Test by changing the value of `months_remaining` and re-running.
#All four branches should be reachable.

#2. Define `occupancy_pct = 87.5`. Write logic that prints:

#occupancy = 100
#
#if occupancy >= 95:
#    print("excellent")
#elif occupancy >= 90:
#    print("good")
#elif occupancy >= 80:
#    print("concerning")
#else:
#    print("critical")

#   - "Excellent" if >= 95
#   - "Good" if 90-94.99
#   - "Concerning" if 80-89.99
#   - "Critical" if < 80

#3. Given an address string `"100 King St W, Toronto, ON M5V 1A1"`,
#write code that:
#   - Splits on `, ` and prints the second part (city)
#   - Splits on `, ` and prints the last part (province + postal code combined)
#   - Checks whether `"Toronto"` is in the string

#address ="100 King St. West, Toronto, ON M5V 1A1"
#splitaddress = address.split(", ")
#print(splitaddress)
#print(splitaddress[1]) #city
#print(splitaddress[2]) #prov + postal
#print("Toronto" in address)

#4. Define `annual_rent = 187500`. 
#Print it formatted as `"Annual rent: $187,500.00"` using an f-string.

#annual_rent = 187500
#print(f"Annual Rent: ${annual_rent:,.2f}")

#5. Take this user-input simulation:
#   ```python
#   square_feet_text = "12500"
#   monthly_rent_text = "8200.50"
#   ```
#   Convert both to numbers, then compute and
#print rent-per-square-foot 
#(monthly rent × 12, divided by square feet), formatted to 2 decimal places.

#sqft_txt = "12500"
#rent_txt = "8200.50"
#
#numsftxt = int(sqft_txt)
#numsrtxt = float(rent_txt)
#rent_psf = (numsrtxt*12 / numsftxt)
#print(f"${rent_psf:,.2f}")

#6. Predict the output of this, then run it:
#   ```python
#   x = 5
#   y = "5"
#   print(x == y)
#   print(x == int(y))
#   ```
#   Write a 1-sentence explanation of what's happening.

#x=5
#y="5"
#print( x == y ) #this will be false - number vs. text
#print ( x == int(y)) #this will be true = number == number (same value)
#
##diff format causing different answers
