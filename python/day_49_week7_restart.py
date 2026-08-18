#DAY 1 restart

#print("hello") 
#name = "Herbert"
#print(name)
#rent = 5000
#print(rent*12)
#print(f"The annual rent is: {rent*12:,.2f}")

#DAY 1 - practice

#print("hello from the portfolio")
#
#property_name = "northgate centre"
#total_sqft = 285000
#year_built = 1974
#asset_class = "mixed use"

#print(property_name)
#print(total_sqft)
#
#print("Property:" + property_name + ", built in: " + str(year_built)) #if using + which is concatenate, need to convert everything to string
#print("Property:", property_name, "built:", year_built)

#this is the preferred way
#print(f"Property name: {property_name}, built: {year_built}")
#print(f"total area: {total_sqft:,.2f} sqft")
#print(type(property_name))
#print(type(total_sqft))
#print(type(year_built))
#print(type(asset_class))
#print(type(3.14))
#print(type(True))

#arithmetic
#monthly_rent = 12500
#annual_rent = monthly_rent * 12
#print(f"annual rent: ${annual_rent:,.2f}")
#print(15 / 4)
#print(15 // 4)
#print(15 % 4)
#print( 2**10 )

#tenant_name = "acme"
#print(tenant_name.upper())
#print(tenant_name.lower())
#print(len(tenant_name))
#print(tenant_name.replace("acme", "acme inc."))

#SELF TEST

#1. Define variables for: a property name (string), its square footage (int), 
# its monthly rent (int or float), and the year it was acquired (int).

#property_name = "Test Property"
#sqft = 500000
#monthlyrent = 5000
#acquired = 2025

#2. Print a sentence using an f-string that says: `"<PropertyName> 
# is <SqFt> sq ft, with monthly rent of $<Rent>, acquired in <Year>."` 
# — using comma separators on the square footage and rent.

#print(f"{property_name} is {sqft:,} sqft, with monthly rent of ${monthlyrent:,}, acquired in {acquired}")

#3. Calculate and print the annual rent (monthly × 12).

#annual_rent = monthlyrent*12
#print(f"${annual_rent:,.2f}")

#4. Calculate and print the years owned (2026 minus acquisition year).

#years_owned = 2026-acquired
#print(f"Years owned: {years_owned:,.2f}")


