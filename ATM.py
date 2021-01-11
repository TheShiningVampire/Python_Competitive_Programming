amt,bal = input().split()
amt = float(amt)
bal = float(bal)

if (amt % 5 == 0) and (amt+0.50 <= bal):
    bal = bal - amt - 0.50

print(round(bal,2)) 
