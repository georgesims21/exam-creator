import random

exercises = [["1", "2", "4", "5", "6", "7"],
["10", "11", "12", "13", "14", "15", "16", "17"],
["24", "27", "28", "32", "33", "36", "39", "40", "41", "42", "46"],
["52", "53", "54", "55", "57", "64", "67", "76", "77", "78", "80", "81", "83"],
["85", "86", "91", "92"],
["93", "95", "96", "98", "199", "202", "204", "207", "208"],
["100", "101", "102", "103", "104", "105", "106", "108", "109", "112", "113", "114", "115", "117", "118"],
["120", "121", "122", "123", "124", "125", "126", "127", "128", "129"],
["185", "186", "188", "190", "191", "192", "1931", "196", "210"],
["00171", "00172", "00173", "00174", "00175", "00176", "00177", "00178", \
            "00181", "00182", "00183", "00184", "00185", "00186", "00187", "00188", \
            "00191", "00192", "00193", "00194", "00195", "00196", "00197", "00198"]]

mylist = []
# Get data from file into array, these are already done exercises
with open ("data.txt", "r") as myfile:
    for line in myfile:
        mylist = line.split() 

# Remove any file exercises from the initial list
exercises = [[ ex for ex in week if ex not in mylist ] for week in exercises]

# Amount of ex per week to be chosen daily
arr_sizes = [1, 1, 2, 2, 1, 2, 2, 2, 1, 4]

# Fetch array of 18 exercises at random from remaining list
i = 0
final = []
for week in exercises:
    # To account for last days with none remaining in the weeks
    while arr_sizes[i] > len(week):
        arr_sizes[i] -= 1
        if arr_sizes[i] == 0:
            continue
    choice = random.choices(week, k=arr_sizes[i])
    final.append(choice)
    i += 1

flat_list = []
for sublist in final:
    for item in sublist:
        flat_list.append(item)

print("Your exercises for the day are:")
print(flat_list)

with open ("data.txt", "a") as myfile:
    for ex in flat_list:
        myfile.write(ex)
        myfile.write(" ")

