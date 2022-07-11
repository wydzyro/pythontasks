Restaurants = ["Mcdonalds", "Burger King", "Five Guys"]
Customers = ["Jimmy"]

Cash = 70

#mcdonalds menu
burger1 = 60
fries1 = 20
mcdonalds_price = burger1 + fries1 

#burger king menu
burger2 = 30
fries2 = 10
burger_king_price = burger2+fries2

#five guys menu
burger3 = 10
fries3 = 50
five_guys_price = burger3+ fries3

price_list = [mcdonalds_price, burger_king_price, five_guys_price]
minimum_price = min(price_list)
total_pay = Cash - minimum_price
print(f"Your leftover cash is {total_pay}")

