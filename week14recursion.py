# part 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0))  # prints 0
print(fibonacci(1))  # prints 1
print(fibonacci(2))  # prints 1
print(fibonacci(3))  # prints 2
print(fibonacci(4))  # prints 3
print(fibonacci(5))  # prints 5

# part 2

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)


gcd(8, 12)
gcd(12, 8 % 12)
gcd(12, 8)
gcd(8, 12 % 8)
gcd(8, 4)
gcd(4, 8 % 4)
gcd(4, 0)

# Part 3


def compare_to(s1, s2):
    # base case: if one of the strings is empty, return the length of the other string
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)

    # recursive case: compare the first characters of each string
    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        # if the first characters are the same, compare the rest of the strings recursively
        return compare_to(s1[1:], s2[1:])

print(compare_to("abc", "abc"))  # prints 0
print(compare_to("abc", "abd"))  # prints -1
print(compare_to("abd", "abc"))  # prints 1
print(compare_to("abc", "abcd"))  # prints -1
print(compare_to("abcd", "abc"))  # prints 1
