import re


# Problem Statement:
# Given a string of lots of space between the word remove unnecesary spaces.
# Example: str="I     love    my                     country."

# Approach-1
# def remove_space(text):
#     x = ' '.join(text.split())
#     print(x)

# Approach-2
def remove_space(text):
    x = re.sub('[ \t\n]+', ' ', text)
    print(x)


str = "The     quick brown                \n\n             \t        fox"
remove_space(str)
