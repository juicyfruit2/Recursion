# A function that returns the largest number in a list of integers taken

# created a def function it takes in 2 parameters 
def sum(list,Number):

# if index == 0 it recursively adds up all the numbers until the index
  if Number == 0:
    return list[0]
  else:
    return list[0] + sum(list[1:],Number-1)

# print functions calls the 2 lists of numbers
print(sum([1,4,3,5,12,16],4))
print(sum([4,3,1,5],1)) 
