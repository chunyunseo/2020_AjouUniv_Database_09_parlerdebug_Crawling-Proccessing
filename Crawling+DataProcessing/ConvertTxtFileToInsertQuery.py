
def write_query(ln):
    string = "("
    for i in ln:
        string = string + '"' + i + '"' + ','

    string = string[0:-1]
    string = string + "),\n"
    return string


file_read = open("i.txt", 'r', -1, "utf-8")
file_write = open("w.txt", "w", -1, "utf-8")

print("테이블 이름을 입력하시오")
input_string = input()


file_write.write("INSERT OR REPLACE INTO " + input_string + "\n")
file_write.write("values\n")

while True:
    line = file_read.readline()
    line = line[0:-1]
    if not line:
        break
    lines = line.split('\t')
    file_write.write(write_query(lines))

file_read.close()
file_write.close()






