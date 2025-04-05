from art import logo
print(logo)
dico = {}
while True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    dico[name] = price
    new_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 100)
    if new_bids == "no":
        break
winner, highest_bid = max(dico.items(), key=lambda x: x[1])
print(f"The winner is {winner} with a bid of ${highest_bid}!")
