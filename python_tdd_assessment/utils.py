def get_max(numbers):
    if not numbers:
        return None
    return max(numbers)

def count_vowels(word):
    vowels = 'aeiou'
    return sum(1 for ch in word.lower() if ch in vowels)


