

def compound_interest(prin,rate,year):
    if year<=0:

        return prin
    else:
        return compound_interest(prin+prin*rate/100,rate,year-1)
prin=int(input("enter amount:"))
rate=int(input("enter the rate:"))
year=int(input("enter the years:"))
amount=compound_interest(prin,rate,year)
print(amount)
