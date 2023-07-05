x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

# print formated numbers ex: 1000 to 1,000
print (f"{z:,}")

# print 2 decimal places
print (f"{z:.2f}")