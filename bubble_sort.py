#!/usr/bin/env python3

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
	sorted_array = bubble_sort(unsorted_list)

	# Printing sorted list.
	print("Sorted!\t{}".format(sorted_array))

def bubble_sort(u_list):
	"""
	Bubble sort identifies a list as sorted when 
	there are no swaps done. Hence we need to keep track of 
	the number of swaps between elements and also
	we have to start with swap_counter not as a zero/0.
	"""
	swap_counter = -1

	# number of elements in unsorted list
	end = len(u_list)
	
	# Starting point
	start = 0
	current = start

	# While swap_counter is not 0.
	while swap_counter != 0:
		# We set swap_counter as 0 to start using it to keep track of the nubmer of swaps.
		swap_counter = 0
		# current is now set to 0, which is also the value of start variable.
		# And current will traverse across the list, stopping before the last element
		# so that it can compare itself with the last element.
		while current < (end - 1):
			# If the current element's value is greater than the value of the next element.			
			if u_list[current] > u_list[current+1]:
				# Swap the value of the current element with the value of the next element.
				# I know the syntax is ... kinda unique to the Python code, the 'more' manual
				# way is the create a variable to act as a buffer and swap the values, like in Selection sort.
				u_list[current], u_list[current+1] = u_list[current+1], u_list[current]
				# Since a swap has occured, we'll increment swap_counter by 1.
				swap_counter += 1
			else:
				# If the value of the current element is not larger than the 
				# value of the next element in the list, we can just more on
				# I'm writing this line to be somewhat more explicit
				swap_counter += 0
			# And once we're done with the comparison, and possibly, the swapping
			# move on to the next element by incrementing current by 1.
			current += 1
		# Now, once we're done traversing through the list and 
		# moved the largest value to the end of the list,
		# we don't have to concern ourselves with the last element(the largest value)
		# so we can save the effort by reducing the length of the list by omitting the last
		# value out of the list.
		end -= 1
		# We bring current back to the start so it will start the comparison again.
		current = start
	# If we've reached here, this means we've gone through the whole list
	# and made no swaps, meaning, swap_counter is 0.
	# we can finally be reasonably sure that the list is sorted, and return the list back to main().
	return u_list

if __name__ == '__main__':
	main()
