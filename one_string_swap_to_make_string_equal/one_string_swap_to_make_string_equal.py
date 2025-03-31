# Leetcode problem: Check if one string swap can make strings equal

def are_almost_equal(self, s1: str, s2: str) -> bool:
    mismatch = []
    for i, j in zip(s1, s2):
        if i != j:
            mismatch.append((i, j))

    if len(mismatch) == 0:
        return True
    if len(mismatch) != 2:
        return False
    a1, b1 = mismatch[0]
    a2, b2 = mismatch[1]
    return a1 == b2 and b1 == a2