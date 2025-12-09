


# try:
#     file = open('a_file.txt')
#     a_dict =  {'a':1,'b':2}
#     print(a_dict['a'])
# except FileNotFoundError:
#     file = open('a_file.txt',mode='w')
#     file.write('something')
# except KeyError as error_msg:
#     print('That key does not exists: ', error_msg)
    
    
# else:
#     content = file.read()
#     print(content)
    

# finally:
#     raise TypeError("dfasf adf adsf")
#     file.close()
#     print('closed the file')

height =  float(input("Height: "))
weight = float(input('Weight: '))


if height>3:
    raise ValueError("Height should be less then 3")
else:
    bmi = weight/height**2
    print(bmi)

