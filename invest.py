def invest(amount, rate, years):
    for year in range(1, years+1):
        amount+=amount*rate
        print(f'year{year}: ${amount:.2f}')
   
amount = float(input("Enter an initial amount: "))
rate = float(input("Enter an annual percentage rate: "))
years = int(input("Enter a number of years: "))

rate= rate/100
invest(amount, rate, years)