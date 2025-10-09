for token in range(1,11):
    print(f"Serving chai for Token: #{token}")
    

number=int(input("Enter a number: "))
result=[]
for i in range(1,11):
    result.append(f"{number} x {i} = {number*i}")

print(result)
    

employee=["Sagar","Tushar","Arun","Amit"]
bill=[100,200,300,400]

for  idx, item in enumerate(employee, start=1):
    print(f"Employee {idx}: {item}")


for name, amount in zip(employee,bill):
    print(f"Bill for employee {name} is {amount}")
    

temp=40

while(temp<=100):
    print(f"Current temperature is: {temp}")
    temp+=15


balance=100
withdrawals=[10,20,30,30,40,50]
result_new=[]
index=0
while(index<len(withdrawals)):
    if(balance>=withdrawals[index]):
        result_new.append(f"Withdrawn:{withdrawals[index]}")
        balance-=withdrawals[index]
    else:
        result_new.append(f"Insufficient funds for requested amount: {withdrawals[index]}")
    index+=1

result_new.append(f"Remaining Balance: {balance}")

print(result_new)


ice_cream=["Vanilla","Chocolate","Out of Stock","Butterscotch","Discontinued","Strawberry"]

for iter in ice_cream:
    if(iter == "Out of Stock"):
        continue
    if(iter == "Discontinued"):
        break
    print(f"item found: {iter}")

print("out of loop")


staff=[("Jade",16),("Adam",15),("John",17)]
for name, age in staff:
    if(age>=18):
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("no one is eligible to manage the staff")


for name, age in staff:
    if(age<=18):
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("no one is eligible to manage the staff")
    


# This function will be tested automatically.
# Do not change the function name or parameters.

def scan_parcels(parcel_codes: list[str]) -> list[str]:
    result = []
    
    for parcel in parcel_codes:
        if parcel == "DAMAGED":
            result.append("Skipped damaged parcel")
            continue
        elif parcel == "STOP":
            result.append("Critical error: Stopping scan")
            break
        else:
            result.append(f"Scanned parcel: {parcel}")
    else:
        # This executes only if the loop wasn't broken
        result.append("All parcels scanned successfully")
    
    return result

parcels = ["P123", "P124", "DAMAGED", "STOP", "P125", "P126", "P127"]

parcels_2 = ["P123", "P124", "DAMAGED", "P125", "P126", "P127"]

res=scan_parcels(parcels)
res2=scan_parcels(parcels_2)

for i in res:
    print(i)

print(res2)