hello = '''                 ___                       
                 | | (_)            
  __ _ _   _  ___| |_ _  ___  _ __  
 / _` | | | |/ __| __| |/ _ \| '_ \ 
| (_| | |_| | (__| |_| | (_) | | | |
 \__,_|\__,_|\___|\__|_|\___/|_| |_|'''

print(hello)
print("Welcome to Secret Auction Program: ")
x = 0
auction = {}
while x != "no":
    print("HI")
    name = input("What is Your Name : ")
    price = int(input("Price at what you want's to bid in RS:"))
    auction[name] = price
    x = input("Is there any more bidder : ")

highest_bid = 0
winner = ""
for x in auction:
    current_bid = auction[x]
    # print(current_bid)
    if current_bid > highest_bid:
        highest_bid = current_bid
        winner = x
print(highest_bid)
print(winner)




