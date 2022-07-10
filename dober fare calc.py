ride_type = "Ferrari"
credits = 50

ride_price = 0
final_price = 0

if ride_type == "Lambourghini":
    ride_price = 40
if ride_type == "Ferrari":
    ride_price = 25
else:
    ride_price = 10

if credits >= ride_price:
    Remaining_Credits = credits - ride_price
    print(f"Transaction successfull, You have {Remaining_Credits} remaining credits.")
else:
    left_over = ride_price - credits
    print(f"You do not have enough credits to pay for this ride. You need {left_over} more")
