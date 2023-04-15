# bounce.py
#
# Exercise 1.5
num_of_bounces = 0
current_height = 100


while num_of_bounces < 10 and current_height > 0:
    num_of_bounces = num_of_bounces + 1
    current_height = current_height * (3/5)
    print("Bounces:", round(num_of_bounces, 4))
    print("Height:",round(current_height,4))
