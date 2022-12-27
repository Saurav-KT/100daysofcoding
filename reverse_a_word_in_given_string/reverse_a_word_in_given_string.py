# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i

# Input:
# S = pqr.mno
# Output: mno.pqr
# Explanation: After reversing the whole
# string , the input string becomes
# mno.pqr

def reverseWords(S):
    arr = S.split('.')
    new_word = ''
    for word_index in range(len(arr) - 1, -1, -1):
        if new_word:
            new_word = new_word + "." + arr[word_index]
        else:
            new_word = arr[word_index]
    return new_word