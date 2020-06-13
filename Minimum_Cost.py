def min_cost(rope_list):
    cost_list = []
    while len(rope_list) > 1:
       min1 = min(rope_list)
       rope_list.remove(min(rope_list))
       min2 = min(rope_list)
       rope_list.remove(min(rope_list))
       rope_list.append(min1 + min2)
       cost_list.append(min1 + min2)
    return sum(cost_list)

if __name__  ==  "__main__":
	rope_list = [int(x) for x in input("Enter length of all pieces of rope by giving space every time: ").split()] 
	Total_cost = min_cost(rope_list)
	print (f"The minimum cost of tieing rope is {Total_cost}")
