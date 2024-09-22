from operator import itemgetter

myList = [
	{
		'foo':12,
		'bar':14
	},
	{
		'moo':52,
		'car':641
	},
	{
		'doo':6,
		'tar':84
	}
]

print(myList)
b_key = "foo"

list_map_myList = list(map(itemgetter(b_key), myList))

values_of_key = [a_dict[b_key] for a_dict in myList if a_dict['foo'] == 12]

result_myList = [ sub[b_key] for sub in myList]

# Python3 code to demonstrate working of
# Get values of particular key in list of dictionaries
# Using list comprehension
  
# initializing list
test_list = [{'gfg' : 1, 'is' : 2, 'good' : 3}, 
             {'gfg' : 2}, {'best' : 3, 'gfg' : 4}]
  
# printing original list
print("The original list is : " + str(test_list))
print("The original list is : " + str(myList))

  
# Using list comprehension
# Get values of particular key in list of dictionaries
res = [ sub["gfg"] for sub in test_list ]
  
# printing result 
print("The values corresponding to key : " + str(res))

list_of_dicts = [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}, {"a": 7, "b": 8, "c": 9}]
a_key = "c"

values_of_key = [a_dict[a_key] for a_dict in list_of_dicts]


print(values_of_key)