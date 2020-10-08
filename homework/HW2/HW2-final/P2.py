def dna_complement(str):
    dna = {'A':'T','T':'A','G':'C','C':'G'}
    result = ''
    if str is None or str == '':
        return None
    for i in str:
        c = i.upper()
        if c not in dna:
            return None
        else:
            result += dna[c]
    return result


demo_input_1 = "AATGGC"
print(demo_input_1)
print(dna_complement(demo_input_1))

demo_input_2 = "QWERTY"
print(demo_input_2)
print(dna_complement(demo_input_2))