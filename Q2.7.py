# Given list
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# i. Print Complete list
print("i. Complete list:", a)

# ii. Print 4th element of list
print("ii. 4th element of the list:", a[3])

# iii. Print list from 0th to 4th index
print("iii. List from 0th to 4th index:", a[0:5])

# iv. Print list -7th to 3rd element
print("iv. List from -7th to 3rd element:", a[-7:4])

# v. Appending an element to list
a.append(110)
print("v. List after appending 110:", a)

# vi. Sorting the elements of the list
a.sort()
print("vi. Sorted list:", a)

# vii. Popping an element
popped_element = a.pop()
print("vii. Popped element:", popped_element)
print("    List after popping:", a)

# viii. Removing specified element
specified_element = 60
a.remove(specified_element)
print(f"viii. List after removing {specified_element}:", a)

# ix. Entering an element at specified index
index_to_insert = 2
element_to_insert = 25
a.insert(index_to_insert, element_to_insert)
print(f"ix. List after inserting {element_to_insert} at index {index_to_insert}:", a)

# x. Counting the occurrence of a specified element
specified_element_count = a.count(25)
print(f"x. Count of {element_to_insert} in the list:", specified_element_count)

# xi. Extending list
extension_list = [120, 130, 140]
a.extend(extension_list)
print("xi. List after extending with another list:", a)

# xii. Reversing the list
a.reverse()
print("xii. Reversed list:", a)
