#import csv
#
##open the file and read it as a list of dicts
#with open("leases.csv", mode="r", encoding="utf-8") as file:
#    reader = csv.DictReader(file)
#    leases = list(reader)
#
## inspect - should be a list of 10 items, each a dict
##print(f"Number of leases: {len(leases)}")
##print(f"First lease: {leases[0]}")
#
## each leases is a dict with the csv column names as keys
##for l in leases[:3]:
##    print(l)
#
## all values come back as string
##print(type(leases[0]["MonthlyRent"]))
##print(leases[0]["MonthlyRent"] + 1000)
#
## convert numeric 
#for l in leases:
#    l["MonthlyRent"] = float(l["MonthlyRent"])
#    l["SquareFeet"] = int(l["SquareFeet"])
#    l["LeaseID"] = int(l["LeaseID"])
#
## total rent calculation
#total_monthly_rent = sum(l["MonthlyRent"] for l in leases)
#print(f"Total monthly rent: ${total_monthly_rent:,.2f}")
#print(f"Annual rent: ${total_monthly_rent*12:,.2f}")
#
## filter active leases
#active_leases = [l for l in leases if l["Status"] == "Active"]
#print(f"Active leases: {len(active_leases)}")
#
## active total rent
#active_total_rent = sum(l["MonthlyRent"] for l in active_leases)
#print(f"Active monthly rent: ${active_total_rent:,.2f}")
#
##group by property (no pandas)

#rent_by_property = {}
#for l in active_leases:
#    prop = l["PropertyName"]
#    if prop not in rent_by_property:
#        rent_by_property[prop] = 0
#    rent_by_property[prop] += l["MonthlyRent"]
#print("\nMonthly rent by property:")
#for prop, rent in rent_by_property.items():
#    print(f" {prop}: ${rent:,.2f}")
#
## or using defaultdict
#from collections import defaultdict
#rent_by_propertyv2 = defaultdict(float)
#for l in active_leases:
#    rent_by_propertyv2[l["PropertyName"]] += l["MonthlyRent"]
#
#print("\nMonthly Rent by property v2:")
#for prop, rent in rent_by_propertyv2.items():
#    print(f" {prop}: ${rent:,.2f}")
#
#sorted_props = sorted(rent_by_propertyv2.items(), key=lambda item: item[1], reverse=True)
#print("\nProperties by rent (descending):")
#for prop, rent in sorted_props:
#    print(f" {prop}: ${rent:,.2f}")


#import pandas as pd
#
##read csv directly into dataframe
#df = pd.read_csv("leases.csv")
#
##inspect
##print(df.head())
##print(df.dtypes)
##print(df.shape)
#
#active = df[df["Status"] == "Active"]
##print(active)
##print(df)
#
#result = active.groupby("PropertyName")["MonthlyRent"].sum().sort_values(ascending=False)
#print(result)

#**🧠 AI-free zone — Self-test (20 min):** No AI:
#
#1. Read `leases.csv`. Print only the leases where `MonthlyRent > 20000`. Show TenantName and MonthlyRent.
#import pandas as pd
#df = pd.read_csv("leases.csv")

#MonthlyRent20K = df[df["MonthlyRent"] > 20000]
#result = MonthlyRent20K.groupby("TenantName")["MonthlyRent"].sum().sort_values(ascending=False)
#print(result)


#2. Count how many leases each property has (group by property, count rows). Print sorted by count descending.
#Numberofleases = df.groupby("PropertyName")["TenantName"].count().sort_values(ascending=False)
#print(Numberofleases)
#
##3. For each lease, compute "AnnualRent" (MonthlyRent × 12) and "RentPerSqFt" (AnnualRent / SquareFeet). 
## Add these as new keys to each dict. Print the first 3 leases to verify.
#import csv
#
##open the file and read it as a list of dicts
#with open("leases.csv", mode="r", encoding="utf-8") as file:
#    reader = csv.DictReader(file)
#    leases = list(reader)
#
#for l in leases:
#    l["MonthlyRent"] = float(l["MonthlyRent"])
#    l["SquareFeet"] = int(l["SquareFeet"])
#    l["AnnualRent"] = l["MonthlyRent"]*12
#    l["RentPerSqft"] = f"{l["AnnualRent"] / (l["SquareFeet"]):,.2f}"
#
#print(leases)
#
##4. Find the lease with the highest rent. Print all of its details.
#from collections import defaultdict
#rent_by_tenant = defaultdict(float)
#for l in leases:
#    rent_by_tenant[l["TenantName"] +" "+ l["PropertyName"]] += l["MonthlyRent"]
#    
#
#sorted_tenant_by_rent = sorted(rent_by_tenant.items(), key=lambda item: item[1], reverse=True)
#
##top_1 = []
##for t, top_1 in enumerate(sorted_tenant_by_rent):
##        if t == 0:
##            print(f"{t}: {top_1}")
#
#
##5. Sort all leases by MonthlyRent descending. Print the top 5 with TenantName, PropertyName, MonthlyRent.
##print(sorted_tenant_by_rent)
#
#top_5 = []
#for t, top_5 in enumerate(sorted_tenant_by_rent):
#        if t < 5:
#            print(f"{t}: {top_5}")
#
##6. Filter to only leases in 'Northgate'. Compute the total monthly rent for that property.
#Northgate = [l for l in leases if l["PropertyName"] =="Northgate"]
#Rent_ng = f"{sum(l["MonthlyRent"] for l in Northgate):,.2f}"
#print(Rent_ng)
##7. Bonus: Try the pandas version of question 2 above. Use `pd.read_csv()`, then `groupby` and `value_counts()` or `size()`. 
# If it works, you have a head start on Week 8.
#
#import pandas as pd
#df = pd.read_csv("leases.csv")
#Numberofleases = df.groupby("PropertyName")["TenantName"].size().sort_values(ascending=False)
#Numberofleases2 = df.groupby("PropertyName")["TenantName"].value_counts().sort_values(ascending=False)
#print(Numberofleases)
#print(Numberofleases2)