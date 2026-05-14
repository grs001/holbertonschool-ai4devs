def is_palindrome(s):
    cleaned = s.replace(" ", "")
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    print(is_palindrome("racecar"))
    print(is_palindrome("A man a plan a canal Panama"))
    print(is_palindrome("Hello"))

if __name__ == "__main__":
    main()
