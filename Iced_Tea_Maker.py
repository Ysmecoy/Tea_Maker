# Open the input and output files.
input_file = open("ingredients.txt")
output_file = open("result.txt", 'w+')

# Read the 3 values in the input file into a list.
values = input_file.readlines()

# Convert the strings to integers to manipulate the data
values[0] = int(values[0])
values[1] = int(values[1])
values[2] = int(values[2])

# find the smallest number

num_bottle_w_tea_bags  = values[0]//3 # 3 tea bags are necessary to make 1 bottle of iced tea
num_bottle_w_sugar = values[1]//2 # 2 sugar packets are necessary to make 1 bottle of iced tea
num_bottle_w_water= values[2]//4 # 4 cups of water are necessary to make 1 bottle of iced tea


# present the result in a list to find the minimum with the help of min() 
list_result = [num_bottle_w_tea_bags, num_bottle_w_sugar, num_bottle_w_water] 

# the minimum number of the list_result represents the maximum amount of bottle of iced tea regarding the limiting ingredients.

output_file.write( str(min(list_result))) 


# Close the files.
input_file.close()
output_file.close()