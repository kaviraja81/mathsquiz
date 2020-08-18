def validate(output):
    valid = []

    IsValid = True
    for i in range(10):

        if output[i] == '' or (not output[i].isnumeric()):
            valid.insert(i, False)
            IsValid = False
        else:
            valid.insert(i, True)
    return valid, IsValid


def calcscore(output, correctresult):
    score = 0
    for i in range(10):
        if correctresult[i] == output[i]:
            score += 1
            print(f"All right {i}")
        else:
            print("Some Wrong")
    return score