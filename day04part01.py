def input():
    f = open('day04part01.input', 'r+')
    return f.readlines()

def contains_dupes(words):
    list_of_words = words.split()
    seen = set()
    for x in list_of_words:
        if x in seen: return True
        seen.add(x)
    return False

def main():
    list_of_pass_phrases = input()
    count = 0
    for x in list_of_pass_phrases:
        if contains_dupes(x) is False:
            count = count + 1
    print count

main()
