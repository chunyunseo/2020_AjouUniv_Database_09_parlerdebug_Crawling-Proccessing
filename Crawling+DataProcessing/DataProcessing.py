
count = 0
prev_location_string = ""
count = count + 1


def get_location_string(province, city, town):
    global count
    global prev_location_string
    cur_location_string = str(count) + '\t' + province + '\t' + city + '\t' + town + '\n'

    if cur_location_string == prev_location_string:
        is_diff = False
    else:
        is_diff = True
        count = count + 1

    prev_location_string = str(count) + '\t' + province + '\t' + city + '\t' + town + '\n'
    return [cur_location_string, count, is_diff]


def is_animal(species):
    animal_list = ["무척추동물류(곤충제외)", "곤충류", "어류", "포유류", "조류", "파충류", "양서류", "미삭동물",
                   "원생동물류"]

    flag = False;

    for i in animal_list:
        if i == species:
            flag = True

    return flag


file_read = open("i.txt", 'r', -1, "utf-8")
file_location = open("location.txt", "w", -1, "utf-8")
file_animal = open("animal.txt", "w", -1, "utf-8")
file_live = open("live_in.txt", "w", -1, "utf-8")
file_growth = open("growth_in.txt", "w", -1, "utf-8")
file_plant = open("plant.txt", "w", -1, "utf-8")


while True:
    line = file_read.readline()
    line = line[0:-1]
    if not line:
        break
    lines = line.split('\t')
    lines[6] = lines[6][1:]
    location_string, num_count, is_dif = get_location_string(lines[0], lines[1], lines[2])
    if is_dif:
        file_location.write(location_string)
    if is_animal(lines[6]):
        file_animal.write(lines[3] + '\t' + lines[6] + '\t' + lines[4] + '\n')
        file_live.write(lines[3] + '\t' + str(num_count) + '\n')
    else:
        file_plant.write(lines[3] + '\t' + lines[6] + '\t' + lines[4] + '\n')
        file_growth.write(lines[3] + '\t' + str(num_count) + '\n')


file_read.close()
file_growth.close()
file_animal.close()
file_plant.close()
file_location.close()