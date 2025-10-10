def generate_invoice(customer_name: str="Guest", *items: str, **charges: float) -> list[str]:
        result=[f"Invoice for {customer_name}:"]
        total=0.0
        
        if items:
            result.append("Items:")
            for item in items:
                result.append(f"-{item}")
        
        if charges:
            result.append("Charges:")
            for charge in charges:
                result.append(f"{charge.capitalize()}: {charges[charge]}")
                total+=charges[charge]
                
        result.append(f"Total Amount Due: {total}")
        return result

res=generate_invoice("John", "Pizza", "Coke")

if res:
    for ans in res:
        print(ans)