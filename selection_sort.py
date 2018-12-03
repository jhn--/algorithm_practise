from random import shuffle

def main():
	numofelements = input("enter how many numbers you want your unsorted list to be: ")
	
	try:
		numofelements = int(numofelements)
	except Exception as e:
		print("Please enter an integer.")

	# Create list.
	print("Creating an unsorted list of {} elements.".format(numofelements))
	unsorted_list = list(range(numofelements))
	# Shuffle list, I know... it's already sorted. 
	shuffle(unsorted_list)
	print("List suffled to:\t{}\n".format(unsorted_list))

	# Sorting unsorted list.
	print("Sorting ...")
	sorted_array = selection_sort(unsorted_list)

	# Printing sorted list.
	print("Sorted!\t{}".format(sorted_array))

def selection_sort(u_list):
	start = 0
	u_list_len = len(u_list)
	current = start
	print("length of list = {}".format(u_list_len))

	# While we haven't reach the last element of the unsorted list
	print("START = {}".format(start))
	while (start < u_list_len):
		# We use the first element of the unsorted list as the smallest.
		smallest = u_list[start]
		print("\tsmallest = {}".format(smallest))
		# We record the location of the smallest element as well
		s_loc = start
		print("\ts_loc = {}".format(s_loc))
		# While we are looping through the unsorted list
		print("\tcurrent = {}".format(current))
		while (current < u_list_len):
			# If the current element is smaller than the smallest element
			if u_list[current] < smallest:
				print("\t\t{} < {}".format(u_list[current], smallest))
				# We promote that element as the smallest element
				smallest = u_list[current]
				print("\t\tsmallest = {}".format(smallest))
				# We also record the location of that element.
				s_loc = current
				print("\t\ts_loc = {}".format(s_loc))
			current += 1
			if (current+1 < u_list_len):
				print("\tNext element will be at location {}, with value of {}.".format(current, u_list[current]))
			else:
				pass
		# once we've reached the end of the list, we start swapping
		# the location which we found the smallest element will be overwritten by the first element.
		u_list[s_loc] = u_list[start]
		print("\tLocation of smallest element is now populated w the value of the first element of the unsorted list = {}.".format(u_list[start]))
		# first location element of the list will be the smallest
		u_list[start] = smallest
		print("\tLocation of the first element is now populated w the value of the smallet element = {}.".format(smallest))
		print("The unsorted_list right now is: {}".format(u_list))
		start += 1
		current = start
		print("\tSTART is now at {}\n".format(start))

	return u_list

if __name__ == '__main__':
	main()
