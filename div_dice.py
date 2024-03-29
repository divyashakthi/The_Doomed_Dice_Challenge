def undoom_dice(die_a, die_b):
    scaling_factor = sum(die_a) / sum(die_b)
    a = [min(4, spots) for spots in die_a]
    b = [round(spots * scaling_factor) for spots in die_b]
    return a, b

#-------------------PART - A-----------------------------------#
#initializing the dice
A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 6]

#calculating the total number of combinations
total_combinations = 6 * 6
print("\nTotal number of possible combinations: ", total_combinations)

#generating all possible combinations as a 6 x 6 matrix
all_sums = [[0] * 6 for i in range(6)]
all_combinations = [[0] * 6 for i in range(6)]
for i in range(1, 7):
    for j in range(1, 7):
        all_sums[i - 1][j - 1] = i + j
        all_combinations[i - 1][j - 1] = str(i) + " " + str(j)
print("\nAll sums: \n")
for i in all_sums:
    print(i)
print("\nAll combinations: \n")
for i in all_combinations:
    print(i)

#calculating the probabilities of all possible sums
print("\nProbability of each sum:\n")
probabilities = {}
for i in range(2, 13):
    count = sum(A.count(i - j) * B.count(j) for j in range(1, 7) if 1 <= i - j <= 6)
    probabilities[i] = count / (len(A) * len(B))
for key, value in probabilities.items():
    print("P(Sum =", key, ") =", value)

#-------------------END OF PART - A-----------------------#

#------------------PART - B-------------------------#
print("--------------------------------------------------------------")
new_die_a, new_die_b = undoom_dice(A, B)

print("\nModified Values of the Dice:\n")
print("New Die A:", new_die_a)
print("New Die B:", new_die_b)