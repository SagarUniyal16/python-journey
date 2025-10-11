def pure_chai(cups):
    return cups * 10

total_chai = 0

# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups


def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))



chai_types = ["light", "kadak", "ginger", "kadak"]


strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))

print(strong_chai)




def reverse_count(n,result):
    if(n==0):
        return result
    result.append(n)
    return reverse_count(n-1,result)


result=reverse_count(10,[])
print(result)
for res in result:
    print(res)


name="Sagar Uniyal"
ress=list(name)
print(ress)


names=["Sagar","Amit","Rohit","Dhruv","Sagar"]

filtered_name=list(filter(lambda n: n!="Sagar",names))
print(filtered_name)

nums=[1,2,3,4]

square=list(map(lambda n: n**2, nums))
print(square)



def factorial_recursive(n,result):
    if(n==0):
        return result
    result=result*n
    return factorial_recursive(n-1,result)

fact=factorial_recursive(3,1)
print(fact)

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

ans=factorial(4)
print(ans)