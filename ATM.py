amt,bal=input().split()
amt=int(amt)
bal=float(bal)
if amt<=bal-0.5 and amt%5 == 0:
    print("{:.2f}".format(bal-amt-0.50))
else:
    print("{:.2f}".format(bal))