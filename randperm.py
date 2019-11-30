
import random as r


def A(S):
    subset = []
    randomPick = S[r.randint(0,len(S)-1)]
    randomPick2 = S[r.randint(0,len(S)-1)]
    while randomPick == randomPick2:
        randomPick2 = S[r.randint(0,len(S)-1)]
    subset.append(randomPick)
    subset.append(randomPick2)
    return subset

def randperm(S):
    if p > 0:
        X_1 = A(S)
        for i in S:
            if i not in X_1:
                X_2.append(i)
        randperm(X_1)
        randperm(X_2)
        return X_1 ++ X_2
    if p == 0:
        return S[0]


if __name__ == "__main__":
    S = ["a", "b", "c", "d"]
    randperm(S)
