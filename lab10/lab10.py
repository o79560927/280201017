
# example 1
def f(n, mult=0):
     if n == 1:
         return 3
     mult += 3
     return mult + f(n-1)  # f(5) = 3 + f(4) = 3+3+f(3)) = 3+3+3+f(2) = 3+3+3+3(f(1)) = 3+3+3+3+3
print(f(5))               #                                                   base case

#example 2
def hailstone(x, hail_str=""):
    if x == 1:
        hail_str += "1"
        return hail_str
    else:
        if x % 2 == 0:
            hail_str += str(x) + ", "
            return hail_str + hailstone(x//2)
        else:
            hail_str += str(x) + ", "
            return hail_str + hailstone(3*x+1)
print(hailstone(11))

# example 3
def sum_of_a_nested_list(x):
    if not isinstance(x, list):
        return x
    else:
        sum = 0
        for a in x:
            sum += sum_of_a_nested_list(a)
        return sum
print(sum_of_a_nested_list([1,2,[3,4],[5]]))

#example 4
def pascal_triangle_line(n):

    if n == 1:
        return [1]

    else:

        line = [1]

        previous_line = pascal_triangle_line(n-1)

        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])

        line += [1]

        return line

print(pascal_triangle_line(6))
# example 5 
def pascal_triangle(n):

    if n == 1:
        return [[1]]
    else:
        line = [1]

        all_lines = pascal_triangle(n-1)

        last_line = all_lines[-1]

        for i in range(len(last_line)-1):

            line.append(last_line[i] + last_line[i+1])

        line += [1]

        all_lines.append(line)

    return all_lines

print(pascal_triangle(6))
