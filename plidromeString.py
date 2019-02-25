def reverse(s):
    return s[::-1]


def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)

    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False


# Driver code
s = "nayan"
ans = isPalindrome(s)
if ans == 1:
    print("Yes")
else:
    print("No")