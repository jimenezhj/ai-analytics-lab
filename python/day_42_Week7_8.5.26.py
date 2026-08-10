#**Problem 1 — Read and inspect (15 min)**
#Read the CSV. Convert MonthlyRent to float and SquareFeet to int. 
# Print: total leases, count by Status, list of distinct properties.


import csv
with open("leases2.csv", encoding="utf-8") as l:
    leases = list(csv.DictReader(l))

for l in leases:
    (l["MonthlyRent"]) = float(l["MonthlyRent"])
    (l["SquareFeet"]) = int(l["SquareFeet"])

number_of_leases = len(leases)
print(f"Number of leases: {number_of_leases}")

status_leases = [l for l in leases]
count_by_status = {}
for l in status_leases:
    stats = l["Status"]
    if stats not in count_by_status:
        count_by_status[stats] = 0
    count_by_status[stats] += 1

print("\nCount by Status:")
for stats, count in count_by_status.items():
    print(f"{stats}:{count}")

count_by_prop = {}
for l in status_leases:
    prop = l["PropertyName"]
    if prop not in count_by_prop:
        count_by_prop[prop] = 1
    count_by_prop[prop] += 0

print(len(count_by_prop))

#**Problem 2 — Portfolio totals (15 min)**
#
#For active leases only:
#- Total monthly rent across the portfolio
#- Total annual rent
#- Average monthly rent
#- Total leased square footage
#- Average rent per square foot (annual)

total_monthly_rent = sum(l["MonthlyRent"] for l in leases if l["Status"] == "Active")
print(f"Total Monthly Rent: {total_monthly_rent:,.2f}")
total_annual_rent = sum(l["MonthlyRent"]*12 for l in leases if l["Status"] == "Active")    
print(f"Total Annual Rent: {total_annual_rent:,.2f}")

active_leases = [l for l in leases if l["Status"] == "Active"]
count_by_active_lease = {}
for l in active_leases:
    lease = l["TenantName"]
    if lease not in count_by_active_lease:
        count_by_active_lease[lease] = 0
    count_by_active_lease[lease] += 1   


average_rent = sum(l["MonthlyRent"] for l in leases if l["Status"] == "Active") / len(count_by_active_lease)
print(f"Average Rent: {average_rent:,.2f}")
total_sqft = sum(l["SquareFeet"] for l in leases if l["Status"] == "Active")
print(f"Total leased sqft: {total_sqft:,.2f}")
avg_annual = total_annual_rent / total_sqft
print(f"Average annual rent psf: {avg_annual:,.2f}")

#**Problem 3 — Top tenants by rent (20 min)**

#Find the top 5 tenants by total monthly rent 
# (across all their leases — some tenants like Loblaw and Shoppers appear at multiple properties).
# Output: tenant name + count of their leases + total monthly rent. Sort descending.
#(Hint: you'll need to aggregate by tenant name, which is a "GROUP BY tenant_name" 
# pattern done manually with a dict.)

top_tenants = {}
for l in status_leases:
    tenant = l["TenantName"]
    if tenant not in top_tenants:
        top_tenants[tenant] = 0
    top_tenants[tenant] += l["MonthlyRent"]

top_tenants2 = {}
for l in status_leases:
    count = l["TenantName"]
    if count not in top_tenants2:
        top_tenants2[count] = 0
    top_tenants2[count] += 1

#print(top_tenants2)    

top5 = sorted(top_tenants.items(), key=lambda item: item[1], reverse=True)
print("\nTop Tenants:")
for tenant, rent in top5[:5]:
    topcount = top_tenants2[tenant]
    print(f"{tenant}:{rent}:{topcount} ")


 #**Problem 4 — Property concentration (20 min)**

#For each property, compute: lease count, total monthly rent, 
# top tenant by rent at that property. 
# Print sorted by total monthly rent descending.

top_prop = {}
for l in status_leases:
    prop = l["PropertyName"]
    if prop not in top_prop:
        top_prop[prop] = 0
    top_prop[prop] += l["MonthlyRent"]

toppropsorted = sorted(top_prop.items(), key=lambda item: item[1], reverse=True)
numleasebyprop = {}

for l in status_leases:
    leasecount = l["PropertyName"]
    if leasecount not in numleasebyprop:
        numleasebyprop[leasecount] = 0
    numleasebyprop[leasecount] += 1

topleaseprop = {}

for l in status_leases:
    leasecountname = l["PropertyName"]
    if leasecountname not in topleaseprop:
        topleaseprop[leasecountname] = []
    topleaseprop[leasecountname].append((l["TenantName"], l["MonthlyRent"]))



print("\n Property Rents")
for prop, rent in toppropsorted:
    lcbp = numleasebyprop[prop]
    tlps = max(topleaseprop[prop], key=lambda item: item[1])
    print(f"Property Name: {prop}, Monthly Rent Total: {rent}, Number of leases: {lcbp} {tlps}")



