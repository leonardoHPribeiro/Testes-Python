#Implicit Conversion - automatic type conversion
    #In certain situations, Python automatically converts one data type to another.
    # This is known as implicit type conversion.
int_num = 12
float_num = 12.6
new_num = int_num + float_num

    # display new value and resulting data type
print(new_num)
print(type(new_num))
print(' ')
#We get TypeError, if we try to add str and int. For example, '12' + 23.
#Python is not able to use Implicit Conversion in such conditions.
#Python has a solution for these types of situations which is known as Explicit Conversion.
#Explicit Conversion - manual type conversion
num_str = '13'
num_int1 = 13

print('data type of num_str before type casting: ', type(num_str))

num_str = int(num_str)

print('data type of num_str after type casting: ', type(num_str))

num_sum = num_int1 + num_str

print(num_sum)
print(type(num_sum))
