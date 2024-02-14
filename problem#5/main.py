#Riley Pollard
# Thursday lab 2pm, Wednesday class

def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   user_val1, user_val2 = swap(user_val1, user_val2)
   user_val3, user_val4 = swap(user_val3, user_val4)
  
   return user_val1, user_val2, user_val3, user_val4
def swap(num1, num2):
   temp = num1
   num1 = num2
   num2 = temp
   return num1, num2

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here
   user_input1, user_input2, user_input3, user_input4 = swap_values(user_input1, user_input2, user_input3, user_input4)
   #print those output
   print('' + str(user_input1) + ' ' + str(user_input2) + ' ' + str(user_input3) + ' ' + str(user_input4))

 