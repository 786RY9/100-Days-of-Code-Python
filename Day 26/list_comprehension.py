


# 




# new_list = [new_item for item in list]

nums = [1,2,3]
new_nums = [n+1 for n in nums]
print(new_nums)

print([n*2 for n in nums])

name = 'rashid yaseen'
print([letter for letter in name])


range_list = [i*2 for i in range(1,5)]
print(range_list)



# new_list = [new_item for item in list if test]

names = ['rashid','hamza','ali','ajmal','jahanzaib','ans']

short_names = [name for name in names if len(name)<5]

print(short_names)

upper_longer_names = [name.upper() for name in names if len(name)>=5]

print(upper_longer_names)


