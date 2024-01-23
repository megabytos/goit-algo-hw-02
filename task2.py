from collections import deque

def is_palindrome(string):
    string = string.replace(" ", "")
    string = string.lower()
    d = deque(list(string))
    while len(d) > 1:
        first = d.popleft()
        last = d.pop()
        if first != last:
            return False
    return True

if __name__ == "__main__":    
    print(is_palindrome('Madam'))
    print(is_palindrome('Mada'))
    print(is_palindrome('level'))
    print(is_palindrome('babbab'))
    print(is_palindrome('ba  baab'))
    print(is_palindrome('Baa Ab'))
