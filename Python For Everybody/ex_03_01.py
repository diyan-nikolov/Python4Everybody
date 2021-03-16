

hrs = input("Enter Hours:")
hrs = float(hrs)
pph = input("Enter Rate:")
pph = float(pph)

if hrs<= 40 :
    print(hrs * pph)
else : 
    print(((hrs-40)*1.5*pph) + (40*pph))
    print("Done")