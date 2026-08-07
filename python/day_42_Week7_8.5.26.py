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







    
 