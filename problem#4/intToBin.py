# Riley Pollard
# Thursday 2pm lab, Wednesday class

def int_to_reverse_binary(num1):
    binary_val = ''
#write your while loop here
    while num1 > 0:
        #write your code
        placement = num1 %2
        binary_val += str(placement)
        num1 = num1 // 2
        


    return binary_val


def string_reverse(input_string): 
    reverse_input = ''
    length = 0
    strlen = len(input_string)
    while length < len(input_string):
        reverse_input += input_string[strlen-1-length]
        print(reverse_input)
        length += 1
   #write your for loop here
    
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)