print("hello from the portfolio")
property_name = "North Gate Centre"
total_square_feet = 285000
year_built = 1974
asset_class = "Mixed Use"

print(property_name)
print(total_square_feet)

print("Property:" + property_name + ", built in " + str(year_built))
print("Property:", property_name, "built in", year_built)
print(f"Property: {property_name} built in {year_built}")
print(f"Total Area: {total_square_feet:,} sq ft")

print(type(property_name))
print(type(total_square_feet))
print(type(3.14))
print(type(True))

monthly_rent = 12500
annual_rent = monthly_rent * 12
print(f"Annual Rent: ${annual_rent:,}")

print(15/4)
print(15//4)
print(15%4)
print(2**10)

tenant_name = "Acme Logistics" 
print(tenant_name.upper())
print(tenant_name.lower())
print(len(tenant_name))
print(tenant_name.replace("Acme","Acme Inc"))

