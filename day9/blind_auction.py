from art import logo
print(logo)
print("WELCOME TO BLIND AUCTION!")

continue_bid = True
auction={}
while continue_bid:
    p_name = input("What is your name?: ")
    p_bid = int(input("What is your bid?: $"))
    auction[p_name] = p_bid
    new_bid = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if new_bid == "no":
        highest_bid = 0
        for key in auction:
            bid_value = auction[key]
            if auction[key] > highest_bid:
                highest_bid = bid_value
                winner = key
        print("\n" * 50)
        print(f"The winner is {winner} with a bid of ${highest_bid}")
        continue_bid = False
    else:
        print("\n" * 50)
        continue