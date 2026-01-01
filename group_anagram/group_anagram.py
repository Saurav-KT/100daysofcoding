'''Write a function called find_anagram_groups that takes a list of
strings as input. The function should group the anagrams together and return a
list of lists, where each inner list contains strings that are anagrams of each other.
The order of the output groups and the strings
within the groups does not matter.'''

from collections import defaultdict

def find_anagram_groups(words):
    groups = defaultdict(list)

    for word in words:
        # Count frequency of each character (assuming lowercase a–z)
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1

        # Convert list to tuple so it can be used as a dict key
        groups[tuple(count)].append(word)

    return list(groups.values())


def find_anagram(input_lst):
    output = []
    visited = set()

    for word in input_lst:
        if word in visited:
            continue

        group = []
        for candidate in input_lst:
            if sorted(word) == sorted(candidate):
                group.append(candidate)
                visited.add(candidate)

        output.append(group)

    return output

def find_anagram(input_lst: list):
    output_lst=[]
    visited= set()
    for i in range(len(input_lst)):
        if input_lst[i] in visited:
            continue
        target_lst=[]
        for j in range(len(input_lst)):
            if len(input_lst[i])== len(input_lst[j]):
                lst=[i for i in input_list[i]]
                if validate_str(input_lst[j],lst):
                    target_lst.append(input_lst[j])
                    visited.add(input_lst[j])
        output_lst.append(target_lst)
    return output_lst


def validate_str(input_str, lst:list):
    counter = 0
    for k in lst:
        if k in input_str:
            counter += 1
    if len(input_str) == counter:
        return True
    return False



input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(find_anagram(input_list))

input_list = ["eat", "tea", "tan", "ate", "nat", "bat", "cat"]
print(find_anagram_groups(input_list))