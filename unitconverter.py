#creating functions
def length(value,from_unit,to_unit):
    conversion_factor={
        'meter':1,
        'kilometer':0.001,
        'inches': 39.3701,
        'feet': 3.28084,
    }
    if from_unit not in conversion_factor or to_unit not in conversion_factor:
        return "Invalid unit, Please enter valid unit..."
    
    convert_value_to_meters = value / conversion_factor[from_unit]
    result = convert_value_to_meters * conversion_factor[to_unit]

    return result

def temperature(value,from_unit,to_unit):
    if from_unit == 'celsius' and to_unit == 'farenheit':
        return (value* 9/5)+32
    elif from_unit == 'farenheit' and to_unit =='celsius':
        return (value - 32) * 5/9
    else:
        return "Invalid unit!"
    

while(True):
    def converter():
        print("Choose conversion type:")
        print("1: Length\n2: Temperature")
        choice=int(input("Enter your choice:-"))
        if choice == 1:
            value = float(input("Enter value to convert: "))
            from_unit= input("Convert from (meter,kilometer,inches,feet):").lower()
            to_unit=input("Convert to (meter,kilometer,inches,feet):").lower()
            result = length(value,from_unit,to_unit)
            print(f"Converted value:{result}{to_unit}")
    
        elif choice==2:
            value = float(input("Enter value to convert: "))
            from_unit= input("Convert from (celsius,farenheit):").lower()
            to_unit=input("Convert to (celsius,farenheit):").lower()
            result = temperature(value,from_unit,to_unit)
            print(f"Converted value:{result}{to_unit}")
    
        else:
            print("Invalid choice! Please select 1 or 2.")


    converter()

    for_continue = input("Do you want to continue(yes/no)...").lower()
    if for_continue == 'yes':
        continue
    else:
        break