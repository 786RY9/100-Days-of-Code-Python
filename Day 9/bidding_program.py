from art import logo
print(logo)

bidder_left = 'yes'
bids = {}
maximum_bidder = ''
maximum_bid = 0
while bidder_left=='yes':

    name = input("What's your name? ")
    if not name.isalpha():
        print('Please enter a valid name.')
        continue
    amount = float(input("Enter your bid amount: $"))
    if amount>=maximum_bid:
        maximum_bid = amount
        maximum_bidder = name
    bids[name] = amount
    
    bidder_left = input('Is someone left after you. "yes" or "no": ')
    
# maximum_bidder = ''
# maximum_bid = 0
# for name,amount in bids.items():
#     if amount>=maximum_bid:
#         maximum_bid = amount
#         maximum_bidder = name
# print(max(bids,key=bids.get)) 
print(f"{maximum_bidder} win with bid of ${maximum_bid}")