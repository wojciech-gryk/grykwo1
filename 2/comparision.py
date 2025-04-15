number1 = 123
number2 = 456
number3 = 123

float1 = 0.1
float2 = 1.3

print(number1 > number2)
print(number1 < number2)
print(number1 == number2)
print(number1 != number2)
print(number1 >= number2)
print(number1 <= number2)

is_equal = float1 == float2
is_first_smaller = float1 < float2
print("is_equal: ", is_equal, "type: ", type(is_equal))

if is_equal or is_first_smaller:
    print("equal")

if float1 == float2 or float1 < float2:
    print("cos tam")
