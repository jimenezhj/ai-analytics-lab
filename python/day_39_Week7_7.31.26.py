# Creating list
#properties = ["Northgate", "Riverside Commons", "Parkview", "Lakeshore Village", "Highland Crossing"]
#monthly_rents = [12500, 22500, 8500, 15000, 18750]
#years_built = [1974, 1973, 1976, 1985, 2004]
#
## Mixed types
#mixed = ["Northgate", 12500, 1974, True]

# # Length
# print(len(properties))
# print(len(monthly_rents))
# 
# # Indexing
# print(properties[0])
# print(properties[1])
# print(properties[-1])
# print(properties[-2])
# 
# # Slicing
# print(properties[0:2])
# print(properties[2:])
# print(properties[:2])
# 
# # Iteration
# print("All Properties:")
# for property_name in properties:
#     print(f" - {property_name}")
# 
# # Iteration with index
# for i, property_name in enumerate(properties):
#     print(f"{i}: {property_name}")
# 
#     # Aggregations on numeric lists
# print(f"Total monthl rent: ${sum(monthly_rents):,}")
# print(f"Average rent: ${sum(monthly_rents) / len(monthly_rents):,.2f}")
# print(f"Max: ${max(monthly_rents):,}")
# print(f"Min: ${min(monthly_rents):,}")
# 
# # Adding to a list
# properties.append("Pickering")
# print(properties)
# 
# # Removing
# properties.remove("Parkview")
# print(properties)
# 
# # Sorting
# sorted_rents = sorted(monthly_rents)
# print(sorted_rents)
# sorted_rents_desc = sorted(monthly_rents, reverse=True)
# print(sorted_rents_desc)
# 
# # membership test
# print("Lakeshore Village" in properties)
# print("Fairmont" in properties)

# Iteration with condition
# filtering with a for loop and if
#rents = [12500, 22500, 8500, 15000, 18750, 32000]

#high_rents = []
#for r in rents:
#    if r > 15000:
#        high_rents.append(r)
#print(sorted(high_rents))

## list comprehension
#high_rents_compact = [r for r in rents if r > 15000]
#print(high_rents_compact)

## list comprehension with transformation
#annualized = [r * 12 for r in rents]
#print(annualized)

## combined
#big_annual = [r * 12 for r in rents if r > 15000]
#print(big_annual)

#leases = [
#    ["Acme Logistics", 12500, 4500],
#    ["Northwind Distribution", 18750, 8200],
#    ["Loblaw", 95000, 28000],
#]

## access by row and column
#print(leases[0])
#print(leases[0][0])
#print(leases[0][2])

#for lease in leases:
#    name, rent, sqft = lease
#    rent_per_sqft = (rent*12) / sqft
#    print(f"{name}: ${rent_per_sqft:.2f}/ sqft annual")

#1. Given `square_feet = [285000, 225000, 175000, 145000, 195000]`, compute and print: total, average, max, and min.
#square_feet = [285000, 225000, 175000, 145000, 195000]
#print(f"Total: ${sum(square_feet):,}")
#print(f"Avg: ${sum(square_feet) / len(square_feet):,.2f} ")
#print(f"Max: {max(square_feet):,.2f}")
#print(f"Min: {min(square_feet):,.2f}")


#2. Given the same list, use a list comprehension to produce a new list with only properties over 200,000 sq ft.
#prop_over_200K = []
#for s in square_feet:
#    if s > 200000:
#        prop_over_200K.append(s)
#print(sorted(prop_over_200K))

#3. Given `years = [1974, 1985, 2004, 1969, 1995]`, use a list comprehension to compute a new list of "age in 2026" for each (i.e., `2026 - year`).
#years = [1974, 1985, 2004, 1969, 1995]
#age_in_2026 = [2026-y for y in years]
#print(age_in_2026)
#

#4. Given two parallel lists:
#   ```python
#   tenants = ["Acme", "Northwind", "Loblaw", "Bell"]
#   rents = [12500, 18750, 95000, 22000]
#   ```
#   Write a loop that prints `"Tenant <name> pays $<rent>/month"` for each pair. (Hint: use `enumerate()` or zip — try with `zip(tenants, rents)`.)
#tenants = ["Acme", "Northwind", "Loblaw", "Bell"]
#rents = [12500, 18750, 95000, 22000]

# for i, property_name in enumerate(properties):
#     print(f"{i}: {property_name}")

#tenant_rents = zip(tenants,rents)
#for tr, tenant_monthly_rent in enumerate(tenant_rents):
#    print(f"Tenant {tenant_monthly_rent[0]} pays ${tenant_monthly_rent[1]:,.2f}/month")

#5. Sort `monthly_rents = [12500, 22500, 8500, 15000, 18750]` from highest to lowest, and print only the top 3.
#monthly_rents = [12500, 22500, 8500, 15000, 18750]
#sorted_rents = sorted(monthly_rents, reverse=True)
#
#top_3 = []
#for t, top_3 in enumerate(sorted_rents):
#        if t < 3:
#            print(f"{t}: {top_3}")


#6. Given:
#   ```python
leases = [
    ["Acme", 12500, "Active"],
    ["Northwind", 18750, "Expired"],
    ["Loblaw", 95000, "Active"],
    ["Bell", 22000, "Active"],
]
# Write a loop that prints just the names of active leases.
#for l in leases:
#    name, sqft, status = l
#    if status == "Active":
#        print(f"{name}")
#   

#
#7. Bonus: write the same logic from #6 as a list comprehension. (Hint: `[lease[0] for lease in leases if lease[2] == "Active"]`)

## list comprehension
#high_rents_compact = [r for r in rents if r > 15000]
#print(high_rents_compact)

#active_leases = [lease[0] for lease in leases if lease[2] == "Active"]
#print(active_leases)

for l in leases:
    if l[2] == "Active":
        print(l[0])
