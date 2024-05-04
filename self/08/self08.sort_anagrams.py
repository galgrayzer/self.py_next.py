def sort_anagrams(list_of_strings):
    out = []
    history = []
    for anagram in list_of_strings:
        if anagram in history:
            continue
        anagram_list = [anagram]
        for word in list_of_strings:
            if sorted(word) == sorted(anagram) and word != anagram:
                anagram_list.append(word)
                history.append(word)
        if anagram_list not in out:
            out.append(anagram_list)
    return out


def main():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating',
                     'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))


if __name__ == '__main__':
    main()
