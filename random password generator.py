import random

lower_case = "abcdefghijklmnopqrstuvwxyz"

number = "1234567890"

symbols = "!@#$%^&*()_+"

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

pass_generator = lower_case + number + symbols + upper_case

length_for_pass = 10

password = "".join(random.sample(pass_generator,length_for_pass))

print(password)