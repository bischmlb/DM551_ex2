





def randperm(S):
    X_1 = {}
    X_2 = {}
    if p > 0:
        X_1 = A(S)
        X_1 = randperm(X_1)
        for i in S:
            if i not in X_1:
                X_2.append(i)
        X_2 = randperm(X_1)
        return X_1X_2
    if p = 0:
        return S[0]
    else:
        return error
