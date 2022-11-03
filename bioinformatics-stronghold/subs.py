"""
The location of a substring s[j:k] is its beginning position j; note that t will have multiple
locations in s if it occurs more than once as a substring of s.

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""


def subs_positions(string, substring):
    positions = []
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            positions.append(i+1)
    return positions


if __name__ == "__main__":
    with open("in\subs.txt", "r") as dataset:
        dataset = dataset.readlines()
    positions = subs_positions(dataset[0][:-1], dataset[1][:-1])
    with open("out\subs.txt", "w") as output:
        for p in positions:
            output.write(f'{p} ')