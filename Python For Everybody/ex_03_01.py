#User inputs the hours
hrs = input("Enter Hours:")

#We convert the input to float
hrs = float(hrs)

#Same procedures with the pay per hour
pph = input("Enter Rate:")
pph = float(pph)

#Conditional statements to calculate the pay, including the overtime
if hrs<= 40 :
    print(hrs * pph)
else : 
    print(((hrs-40)*1.5*pph) + (40*pph))
    print("That is all.")