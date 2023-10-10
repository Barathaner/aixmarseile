def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

# Beispieltest:
DNA_samples = [
    'ACCATACCTTCGATTGTCGTGGCCACCCTCGGATTACACGGCAGAGGTGC',
    'GTTGTGTTCCGATAGGCCAGCATATTATCCTAAGGCGTTACCCCAATCGA'
    # ... weitere Sequenzen ...
]

print(hamming_distance(DNA_samples[0], DNA_samples[1]))  # Output sollte 42 sein
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

# Beispieltest:
print(levenshtein_distance("python", "kryptonite"))  # Output sollte Ihre erwartete Zahl sein



import numpy as np

num_samples = len(DNA_samples)
distance_matrix = np.zeros((num_samples, num_samples), dtype=int)

for i in range(num_samples):
    for j in range(num_samples):
        distance_matrix[i, j] = levenshtein_distance(DNA_samples[i], DNA_samples[j])

# Matrix in einer Textdatei speichern
np.savetxt("distance_matrix.txt", distance_matrix, fmt='%d')

def smith_waterman(seq1, seq2, match=1, mismatch=-1, gap=-1):
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    score_matrix = [[0] * cols for _ in range(rows)]

    max_score = 0
    max_pos = (0, 0)

    for i in range(1, rows):
        for j in range(1, cols):
            match_score = score_matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            score_matrix[i][j] = max(0, score_matrix[i-1][j] + gap, score_matrix[i][j-1] + gap, match_score)

            if score_matrix[i][j] >= max_score:
                max_score = score_matrix[i][j]
                max_pos = (i, j)

    align1, align2 = traceback(seq1, seq2, score_matrix, max_pos, gap)
    print_alignment(align1, align2)
    return align1, align2

def traceback(seq1, seq2, score_matrix, start_pos, gap):
    i, j = start_pos
    align1, align2 = [], []
    while score_matrix[i][j] != 0:  
        if i > 0 and j > 0 and score_matrix[i][j] == score_matrix[i-1][j-1] + (1 if seq1[i-1] == seq2[j-1] else -1):
            align1.append(seq1[i-1])
            align2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif i > 0 and score_matrix[i][j] == score_matrix[i-1][j] + gap:
            align1.append(seq1[i-1])
            align2.append('-')
            i -= 1
        else:
            align1.append('-')
            align2.append(seq2[j-1])
            j -= 1
    return ''.join(reversed(align1)), ''.join(reversed(align2))

def print_alignment(align1, align2):
    symbols = []
    for a1, a2 in zip(align1, align2):
        symbols.append('|' if a1 == a2 else ' ')
    print("1", align1)
    print("2", ''.join(symbols))
    print("3", align2)


seq1 = "ACTTA"
seq2 = "ACATA"
align1, align2 = smith_waterman(seq1, seq2)