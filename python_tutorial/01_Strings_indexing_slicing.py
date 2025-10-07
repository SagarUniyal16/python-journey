customer_name='Sagar Uniyal'
customer_order='Butter Chicken'

print(f'Hello {customer_name}, your order is {customer_order}.')

print(f"First word : {customer_name[0:5]}")

print(f"First word : {customer_name[6:]}")

print(f"reversed name : {customer_name[::-1]}")

special_string = "Café naïve façade coöperate jalapeño résumé Pokémon"

encode_string=special_string.encode('utf-8')

print(f"Non encoded string : {special_string}")
print("ENCODED STRING:", encode_string)

decoded_string=encode_string.decode('utf-8')

print(f"Decoded string : {decoded_string}")