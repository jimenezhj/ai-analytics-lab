#property = {
#    "name": "Northgate Centre",
#    "city": "Toronto",
#    "asset_class": "Mixed-use",
#    "year_built": 1974,
#    "square_feet": 285000,
#
#}

#print(property["name"])
#print(property["square_feet"])

#property["province"] = "ON"
#property["square_feet"] = 290000
#
#print(property.get("name"))
#print(property.get("rent"))
#print(property.get("rent", 0))
#print(property.get("square_feet"))
#print(property.get("province"))
#
#print("name" in property)
#print("rent" in property)
#
#del property["province"]
#print(property)
#
#print(list(property.keys()))
#print(list(property.values()))
#print(list(property.items()))
#
#
#print("\nProperty details:")
#for key, value in property.items():
#    print(f" {key}: {value}")

#portfolio = {
#    "northgate":{
#        "name": "northgate centre",
#        "city": "toronto",
#        "square_feet": 285000,
#    },
#    "riverside":{
#        "name": "riverside commons",
#        "city": 'mississauga',
#        "square_feet": 225000,
#    },
#}
#
#print(portfolio["northgate"]["city"])
#
#for key, prop_details in portfolio.items():
#    print(f"{key}: {prop_details["name"]} in {prop_details["city"]}")

#point = (10, 20)
#coordinates = 10, 20
#print(point[0])
#
#name, rent, sqft = ("Acme", 12500, 4500)
#print(name)
#print(rent)
#
#tenants = [
#    {"id": 1, "name": "loblaw", "industry": "grocery", "anchor": True},
#    {"id": 2, "name": "canadian tire", "industry": "retail", "anchor": True},
#    {"id": 3, "name": "starbucks", "industry": "food service", "anchor": False},
#]
#
#for t in tenants:
#    print(f"{t["name"]} ({t["industry"]}) - Anchor: {t["anchor"]}")

#anchors = [t for t in tenants if t["anchor"]]
#print(anchors)

#names = [t["name"] for t in tenants]
#print(names)

#anchor_names = [t["name"] for t in tenants if t["anchor"]]
# print(anchor_names)

#1. Create a dict representing a single lease with keys: `tenant_name`, `property_name`, `monthly_rent`, 
# `square_feet`, `start_date` (string), `end_date` (string). Print each field with a label.
#tenant = {
#    'tenant_name': 'nike',
#    'property_name': 'northside centre',
#    'monthly_rent': 25000,
#    'square_feet': 10000,
#    'start_date': '2026-07-01',
#    'end_date': '2031-06-30'
#}


#2. Compute and print rent-per-square-foot annually for that lease.

#rent_per_squarefoot = tenant['monthly_rent'] * 12 / tenant['square_feet']
#print(rent_per_squarefoot)

#3. Create a list of 4 lease dicts (different tenants/properties/rents). Then:
#   - Use a list comprehension to get all tenant names
#   - Use a list comprehension to filter to only leases with monthly rent > 15000
#   - Compute total monthly rent across all leases (hint: list comprehension that extracts rent, then `sum()`)


#leases = [
#    {   "id": 1,
#        "tenant_name": "nike",
#        "property_name": "southgate sc",
#        "monthly_rent": 25000,
#        "square_feet": 10000,
#        "start_date": '2026-07-01',
#        "end_date": '2031-06-30'
#    },
#    {   "id": 2,
#        "tenant_name": "adidas",
#        "property_name": "northgate sc",
#        "monthly_rent": 15000,
#        "square_feet": 7500,
#        "start_date": '2026-07-01',
#        "end_date": '2031-06-30'
#    },
#    {   "id": 3,
#        "tenant_name": "footlocker",
#        "property_name": "eastgate sc",
#        "monthly_rent": 10000,
#        "square_feet": 5000,
#        "start_date": '2026-07-01',
#        "end_date": '2031-06-30'
#    },
#    {   "id": 4,
#        "tenant_name": "champs",
#        "property_name": "westgate sc",
#        "monthly_rent": 10000,
#        "square_feet": 5000,
#        "start_date": '2026-07-01',
#        "end_date": '2031-06-30'
#    },
#]

#for l in leases:
#    print(l["tenant_name"])

#major_tenants = [l for l in leases if l["monthly_rent"]>=15000]
#print(major_tenants)
 
#total_monthly_rent =  [l["monthly_rent"] for l in leases]
#rint(sum(total_monthly_rent))


#4. Iterate the list of leases and print a one-line summary for each: `"<TenantName> at <PropertyName>: $<MonthlyRent>/mo"`.
#for l in leases:
#    print(f"{l["tenant_name"]} at {l["property_name"]}: ${l["monthly_rent"]}/mo")


#5. Given two dicts:
#   ```python
#property1 = {"name": "Northgate", "city": "Toronto"}
#property2 = {"name": "Northgate", "city": "Toronto"}
#   ```
#   Predict: `property1 == property2` — True or False? Run it. Write 1 sentence about why. True. because every element matches
#property1 == property2
#6. Given:
#   ```python
#leases = [
#    {"tenant": "Acme", "rent": 12500},
#    {"tenant": "Bell", "rent": 22000},
#   ]
#   ```
#   Add a third lease using `.append({...})`. Then write a loop that adds a new key `"annual_rent"` to each lease, computed as `rent * 12`. 
# Print the final list.

#leases.append({"tenant": "Rogers", "rent": 15000})
#print(leases)

#for l in leases:
#    l["annual_rent"] =  l["rent"] * 12
#
#
#print(leases)
