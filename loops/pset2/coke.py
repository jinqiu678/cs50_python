total_amount = 50
while total_amount > 0:
    print(f"Amount Due {total_amount}")
    inserted_amount = int(input("Insert Coin: "))
    total_amount = total_amount- inserted_amount

print(f"Changed Owed {abs(total_amount)}")
