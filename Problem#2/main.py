# Riley Pollard
# Wednesday class, Thursday 2pm lab

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   #write your code here
   dolpermil = dollars_per_gallon/miles_per_gallon
   return (dolpermil*miles_driven)
   

if __name__ == '__main__':
   miles_per_gallon = float(input())
   dollars_per_gallon = float(input())
   #print your costs here like example below
   print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
   print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50.0):.2f}')
   print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 100.0):.2f}')
   