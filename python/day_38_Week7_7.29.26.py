### Comparison operators return bool (True or False)
##print(5 > 3)
##print(5 == 3)
##print(5 != 3)
##print("tyrion" == "tyrion")
##
### Logical operators
##print(True and False)
##print(True or False)
##print(not True)
##
### Conditional statements
##monthly_rent = 22500
##
##if monthly_rent >= 50000:
##    tier = "anchor"
##elif monthly_rent >= 15000:
##    tier = "major"
##elif monthly_rent >= 5000:
##    tier = "standard"
##else:
##    tier = "small"
##
##print(f"Rent ${monthly_rent:,} is in the {tier} tier")
##
### Nested conditions
##months_remaining = 8
##status = "active"
##
##if status == "active":
##    if months_remaining <= 6:
##        urgency = "critical"
##    elif months_remaining <= 12:
##        urgency = "urgent" 
##    else:
##        urgency = "normal"
##else:
##    urgency = "n/a - lease not active"
##
##print(f"Urgency: {urgency}")
##
### Combined conditions are cleaner with and/or
##lease_status = "active"
##months_to_expiry = 4
##
##if lease_status == "active" and months_to_expiry <= 6:
##    print("this lease needs immediate attention")  
##
### String methods come up constantly — practice
##property_name = "  Northgate Centre  "
##print(property_name.strip())
##print(property_name.strip().lower())
##print("North" in property_name)
##print(property_name.replace("North","South"))
##
### Splitting strings (useful for parsing data)
##address = "2300 Maple Ave, Toronto, ON"
##parts = address.split(", ")
##print(parts)
##print(parts[2])
##
### Number formatting in f-strings
##revenue = 1250000.5678
##print(f"revenue: ${revenue:,.2f}")
##print(f"revenue: ${revenue:,.0f}")
##
### Type conversions
##year_text = "2024"
##year_num = int(year_text)
##print(year_num + 1)
##
##price_text = "12500.75"
##price_num = float(price_text)
##print(price_num * 12)
##
##some_number = 42
##some_text = str(some_number)
##print("answer is" + " " +some_text)
##

##1. Write a script that defines a variable `months_remaining = X` (pick a number) and prints one of these messages:
##   - "Critical: <= 6 months"
##   - "Urgent: 7-12 months"
##   - "Upcoming: 13-24 months"
##   - "Future: > 24 months"
##   
##   Test by changing the value of `months_remaining` and re-running. All four branches should be reachable.
##
##months_remaining = 25
##
##if months_remaining <= 6:
##    status = "critical"
##elif months_remaining <= 12:
##    status = "urgent"
##elif months_remaining <= 24:
##    status = "upcoming"
##else:
##    status = "future"
##
##print(f"There are {months_remaining} months remaining, the status is {status}")

##2. Define `occupancy_pct = 87.5`. Write logic that prints:
##   - "Excellent" if >= 95
##   - "Good" if 90-94.99
##   - "Concerning" if 80-89.99
##   - "Critical" if < 80

##occupancy = 90
##
##if occupancy >= 95:
##    status = "excellent"
##elif occupancy >= 90:
##    status = "good"
##elif occupancy >= 80:
##    status = "concerning" 
##else:
##    status = "critical"
##
##print(f" The current occupancy rate is {occupancy}.  This property's current status is {status}")

##3. Given an address string `"100 King St W, Toronto, ON M5V 1A1"`, write code that:
##   - Splits on `, ` and prints the second part (city)
##   - Splits on `, ` and prints the last part (province + postal code combined)
##   - Checks whether `"Toronto"` is in the string
##

address = "100 king st w, toronto, on m5v 1a1"
address_split = address.split(", ")
print(address_split[1])
print(address_split[2])
print("toronto" in address)


##4. Define `annual_rent = 187500`. Print it formatted as `"Annual rent: $187,500.00"` using an f-string.
annual_rent = 187500

print(f"Annual Rent: {annual_rent:,.2f}" )


##5. Take this user-input simulation:
##   ```python
##   square_feet_text = "12500"
##   monthly_rent_text = "8200.50"
##   ```
##   Convert both to numbers, then compute and print rent-per-square-foot (monthly rent × 12, divided by square feet), formatted to 2 decimal places.
##
##6. Predict the output of this, then run it:
##   ```python
##   x = 5   x will be assigned integer 5
##   y = "5" y will be assigned text 5
##   print(x == y) will result in false
##   print(x == int(y)) will result in true
##   ```
##   Write a 1-sentence explanation of what's happening > different data types resulting in what I noted above - both types need to be the same for comparitive to work so it has to be converted

x = 5
y = "5"
print(x == y)
print(x == int(y))