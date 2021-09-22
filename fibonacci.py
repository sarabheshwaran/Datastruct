

fib_nums = [0, 1]
n = 0
num1 = 0
num2 = 1

x_coords = [1,2]
x_count = 3
y_coords = [0,1]
coord_pairs = ()
def fib(n):

    global x_coords
    global x_count

    a = 0
    b = 1
    c = 1

    for i in range(n-2):
        c = a + b
        a = b
        b = c

        fib_nums.append(c)
        y_coords.append(c)
        x_coords.append(x_count)
        x_count = x_count + 1

    return(fib_nums)


for num in fib_nums:

    num1 = num1 + 1
    num2 = num2 + 2
    temp_list = [fib_nums[num1:],fib_nums[num2:]]


n = int(input('How many Fib numbers would you like to see? : '))
fib(n)
print(fib_nums)
print(temp_list)

# plt.scatter(y_coords, x_coords) # .scatter(x,y) <<<----- this is actually how this works
# plt.show()