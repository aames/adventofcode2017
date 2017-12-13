def input():
    f = open('day04part01.input', 'r+')
    return f.readlines()

def contains_dupes(words):
    """
    Check for anagrams of words - by sorting the characters in each word
    """
    list_of_words = words.split()
    seen = set()
    for x in list_of_words:
        if ''.join(sorted(x)) in seen: return True
        seen.add(''.join(sorted(list(x))))
    return False

def main():
    list_of_pass_phrases = input()
    count = 0
    for x in list_of_pass_phrases:
        if contains_dupes(x) is False:
            count = count + 1
    print count

main()
