# Locations are listed by a unique number called the location ID
# Pair the smallest number in both lists, the second smallest etc..
# Add up all the distance of how far apart the two numbers are (e.g. 3, 7 and distance is 4)

X = []
Y = []
distance = 0

with open("day1.txt", "r") as lists:
    for row in lists:
        x, y = row.split()
        X.append(int(x))
        Y.append(int(y))

X.sort()
Y.sort()

for num1, num2 in zip(X, Y):
    diff = abs(num1-num2)
    distance += diff

print(distance)

########## PART 2 ##########
# Calculate a total similarity score
# Add each number in the left list after multiplying it by the number of times
# it appears in the right list

similarity_score = 0

for num1 in X:
    occurrences = Y.count(num1)
    score = num1 * occurrences
    similarity_score += score

print(similarity_score)
