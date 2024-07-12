combinations = []


def well_formed_combinations(no, opening, closing, s):
    if opening == closing and opening + closing == no * 2:
        combinations.append(s)
        return
    if opening < no:
        well_formed_combinations(no, opening + 1, closing, s + "(")

    if closing < opening:
        well_formed_combinations(no, opening, closing + 1, s + ")")


well_formed_combinations(4, 0, 0, "")
print(combinations)