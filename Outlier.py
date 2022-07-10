upper_bound = 100
lower_bound = 0
number = -5
outlier = False

if number > 100:
    outlier = True
if number < 0:
    outlier = True
else:
    print(f"{number} is not an outlier.")
if outlier == True:
    print(f"{number} is an outlier.")