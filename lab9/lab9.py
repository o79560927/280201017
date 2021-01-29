#example 1
"""
def harmonic_sum(n):
     if n == 1:
         return 1
     else:
         return 1/n + harmonic_sum(n-1)
print(harmonic_sum(7))
"""
#example 2
# too easy

# example 3
"""
def get_evens_recursive(l):
    if len(l) == 0:
        return []
    else:
        if l[0] % 2 == 0:
            return [l.pop(0)] + get_evens_recursive(l[1:])
        else:
            return get_evens_recursive(l[1:])
"""
# example 4
"""
def get_evens(even_list):
    count = 0
    while count <= len(even_list):
        count += 1
    return count

print(get_evens(get_evens_recursive([1,2,3,4])))
"""
# example 5
"""
import time
def countdown(t):
    if t == 0:
        print("alert")
        return None
    print(f"remaining time : {t}")
    time.sleep(1)
    return countdown(t-1)

countdown(4)
"""