'''
Caching Expensive Calculations
You are optimizing performance for a system that frequently repeats the same heavy calculations 
(e.g., a backend system or a financial calculator).

Tasks:
Create a decorator called cache_results:
Use a dictionary to store past results based on arguments.
If the same arguments are passed again, return the cached result.
Otherwise, compute the result, cache it, and return the new value.

Apply it to a function multiply(a, b):
It simply returns the product of two integers.
The decorated function should:
Return "Computed: result" for new computations.
Return "From Cache: result" for repeated calls with the same arguments.
'''



# This function will be tested automatically.
# Do not change the function name or parameters.

from functools import wraps
def cache_results(func):
    # Write your code below this line
    past_result={}
    @wraps(func)
    def wrapper(a,b):
        key=(a,b)
        if(key in past_result):
            return f"From Cache: {key} : {past_result[key]}"
        else:
            result = func(a, b)
            past_result[key] = result
            return f"Computed: {result}"
    return wrapper

@cache_results
def multiply(a: int, b: int) -> int:
    return a * b

res=multiply(2,3)
res1=multiply(2,3)
print(res)
print(res1)