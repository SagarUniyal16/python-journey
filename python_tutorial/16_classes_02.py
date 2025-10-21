class SmartDevice():
    brand="HomeTech"
    
    def __init__(self, device_name, power_status):
        self.device_name=device_name
        self.power_status=power_status
        self.brand = "CustomBrand"
    
    
    def get_status(self):
        if(self.power_status==True):
            return f"{self.device_name} is ON - {self.brand}"
        else:
            return f"{self.device_name} is OFF - {self.brand}"



AC=SmartDevice("AC",True)
status= AC.get_status()
print(status)