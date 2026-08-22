#rents = [5000, 8000, 3000]
#print(rents[0])
#print(len(rents))
#print(sum(rents))
#print(max(rents))
#for r in rents:
#    print(r)

#rents = []
#rents.append(5000)
#print(rents)

#rents = [5000, 8000, 3000]
#total = 0
#for r in rents:
#    total += r
#print(total)

#PRACTICE

#properties = ["northgate", "riverside commons", "parkview", 
#              "larkshore village", "highland cross"]
#monthly = [12500, 22500, 8500, 15000, 18750]
#years = [1974, 1973, 1976, 1985, 2004]
#
#mixed = ["Northgate", 12500, 1974, True]

#print(len(properties))
#print(len(monthly))

#print(properties[0])
#print(properties[1])
#print(properties[-1])
#print(properties[-2])
#print(properties[0:2])
#print(properties[2:])
#print(properties[:2])

#print("all properties:")
#for p in properties:
#    print(f"    - {p}")
#
#for i, p in enumerate(properties):
#    print(f"{i}: {p}")

#print(f"total monthly rent: ${sum(monthly):,}")
#print(f"average: ${sum(monthly) / len(monthly):,.2f}")
#print(f"max rent: ${max(monthly):,}")
#print(f"min rent: ${min(monthly):,}")
#
#properties.append("pickering")
#print(properties)
#
#properties.remove("pickering")
#print(properties)

#sortedrents = sorted(monthly)
#print(sortedrents)
#sorteddesc = sorted(monthly, reverse=True)
#print(sorteddesc)

#monthly.sort(reverse=True)
#print(monthly)

#print("larkshore village" in properties)
#print("fairmount" in properties)

rents = [12500, 22500, 8500, 15000, 18750, 32000]
#
#high_rents = []
#for r in rents:
#    if r > 15000:
#        high_rents.append(r)
#print(high_rents)
#
#high_rents_compact = [r for r in rents if r > 15000]
#print(high_rents_compact)

#annual = [r * 12 for r in rents if r > 15000]
#print(annual)

#leases = [
#    ["Acme Logistics", 12500, 4500],
#    ["Northwind Distribution", 18750, 8200],
#    ["Loblaw", 95000, 28000],
#]

#print(leases[0])
#print(leases[0][2])
#print(leases[1][1])

#for l in leases:
#    name, rent, sqft = l
#    rent_per_sqft = rent*12 / sqft
#    print(f"{name}: ${rent_per_sqft:.2f}/sqft annual")

#cities = ["Toronto", "Mississauga", "Toronto", "Ottawa", "Toronto"]
#
#unique = set(cities)
#print(unique)
#
#print(len(set(cities)))
#
#distinct_sort = sorted(set(cities))
#print(distinct_sort)
#

#1. Given `square_feet = [285000, 225000, 175000, 145000, 195000]`, 
# compute and print: total, average, max, and min.
square_feet = [285000, 225000, 175000, 145000, 195000]

#print(max(square_feet))
#print(sum(square_feet))
#print(min(square_feet))
#total = sum(square_feet)
#num = len(square_feet)
#print(f"{total/num:.2f}")

#2. Given the same list, use a list comprehension to produce a 
# new list with only properties over 200,000 sq ft.
#big_prop = [s for s in square_feet if s > 200000]
#print(big_prop)
#
#3. Given `years = [1974, 1985, 2004, 1969, 1995]`, 
# use a list comprehension to compute a new list of "age in 2026" for each 
# (i.e., `2026 - year`).
#years = [1974, 1985, 2004, 1969, 1995]
#agein2026 = [2026-y for y in years]
#print(agein2026)

#
#4. Given two parallel lists:
#   ```python
#tenants = ["Acme", "Northwind", "Loblaw", "Bell"]
#rents = [12500, 18750, 95000, 22000]
#   ```
#   Write a loop that prints `"Tenant <name> pays $<rent>/month"` for each pair. 
# (Hint: use `enumerate()` or zip — try with `zip(tenants, rents)`.)

#for i, t in enumerate(tenants):
#    print(f"Tenant: {t} pays ${rents[i]}")

#for t, r in zip(tenants,rents):
#    print(f"Tenant {t} pays ${r} rents")

#5. Sort `monthly_rents = [12500, 22500, 8500, 15000, 18750]` 
# from highest to lowest, and print only the top 3.
#monthly_rents = [12500, 22500, 8500, 15000, 18750]
#sortedrent = sorted(monthly_rents, reverse=True)
#print(sortedrent[0:3])

#
#6. Given:
#   ```python
leases = [
    ["Acme", 12500, "Active"],
    ["Northwind", 18750, "Expired"],
    ["Loblaw", 95000, "Active"],
    ["Bell", 22000, "Active"],
]

#   Write a loop that prints just the names of active leases.
for l in leases:
    name, rent, status = l
    if status == "Active":
        print(name)

active_tenants1 = []
for l in leases:
    if l[2] == "Active":
        active_tenants1.append(l[0])
print(active_tenants1)

#
#7. Bonus: write the same logic from #6 as a list comprehension.
#  (Hint: `[lease[0] for lease in leases if lease[2] == "Active"]`)

active_tenants = [l[0] for l in leases if l[2] == "Active"]
print(active_tenants)

#
#8. Given `cities = ["Toronto", "Ottawa", "Toronto", "Mississauga", "Ottawa", 
# "Toronto"]`, print (a) the list of distinct cities sorted alphabetically, 
# and (b) how many distinct cities there are. 
# (Hint: `set()` for distinct, `len(set())` to count them — this is 
# `COUNT(DISTINCT)`.)

cities = ["Toronto", "Ottawa", "Toronto", "Mississauga", "Ottawa", 
"Toronto"]

dcities = sorted(set(cities))
countdcities = len(dcities)
print(dcities)
print(countdcities)
