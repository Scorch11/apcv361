def load_cows(a1_cow_data.txt):

file = open(a1_cow_data.txt, 'r')

cows_dict = {}

for line in file:

name, weight = line.split(',')

cows_dict[name] = int(weight)

file.close()

return cows_dict
