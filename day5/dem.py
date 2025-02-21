def divide_amount(amount):
    rupee_denominations=[10,5,1]
    result=[]

    for value in rupee_denominations:
        count=amount//value
        amount%=value
        result.append((value,count))
    
    return result

amount=int(input("Enter the amount: "))
divided_amount=divide_amount(amount)

for value,count in divided_amount:
    if count>0:
        print(f"{value} rupee(s): {count}")
