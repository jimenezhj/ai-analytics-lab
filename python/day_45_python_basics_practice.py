# PART 6 — Making decisions: `if`

#if runs code when something is true

#rent = 5000
#if rent > 4000:
#    print("Expensive")
#
#command ran because it met the criteria set by "if"

#rent = 2000
#if rent > 4000:
#    print("expensive")

# does not meet, does not print

## 6.2 == means is equal to

# = means put in the box (hold this value); == double when comparing to something, are they equal?

#status ="Active"
#if status == "Active":
#    print("this is active")

#leases = [
#    {"tenant":"loblaw", "status":"active"},
#    {"tenant":"lcbo", "status":"expired"}
#]
#
#for l in leases:
#    if l["status"] == "active":
#        print(l["tenant"])

#for each row, if its status equals active, print the tenant


## 6.3 elif and else - more than two paths

# if handles one condition, elif (else if) adds more, else catches everything left over
#
#rent = 5000
#if rent > 8000:
#    print("high")
#elif rent > 3000:
#    print("medium")
#else:
#    print("low")

#part 7 - converting types == text to numbers

#7.1 - int() and float()

#int() converts to whole number
#float() converts to decimals

#print("100"+"50")
#print(int("100")+int("50"))

#rent_text = "5000"
#rent_number = float(rent_text)
#print(rent_number*12)

#7.2 str() turns numbers into text
#
#count = 5
#count_text = str(count)
#print("Count:" + count_text)

#part 8 f-strings - putting values into text cleanly

#f string lets you drop variables straight into text, put an f before the opening quote
#wrap anyvariable in {}

#tenant = "loblaw"
#rent = 5000
#print(f"{tenant} pays {rent}")

#rent = 5000
#print(f"annual rent is {rent*12}")

#format money to 2 decimeals with :.2f

#rent = 1234.5
#print(f"${rent:.2f}")
#
#.2f means show this number with 2 decimals