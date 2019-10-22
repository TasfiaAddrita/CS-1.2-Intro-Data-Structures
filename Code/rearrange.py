import sys
import random

def random_params(params_list):
    return random.sample(params_list, k=len(params_list))

params = sys.argv[1:]
# print(params)

ran_params = random_params(params)
ran_params_string = ""
for param in ran_params:
    ran_params_string += param + " "
print(ran_params_string)