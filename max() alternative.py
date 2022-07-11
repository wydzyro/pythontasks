numbers = [10,20,30,40,50,60]
highest = numbers[0]

for x in numbers:
  if x > highest:
    highest = x

print(f"Highest score = {highest}")