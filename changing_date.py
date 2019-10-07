import re
from datetime import datetime


path = "file.txt"
old_file = str(open(path).read())

first_old_date = re.findall("(\D{3} \d{1,2} \d{4} \d{1,2}[:]\d{1,2} (?:PM|AM))", old_file, re.IGNORECASE | re.DOTALL)
second_old_date = re.findall("(\d{1,2}\/\d{1,2}\/\d{4} \d{1,2}[:]\d{1,2})", old_file, re.IGNORECASE | re.DOTALL)
third_old_date = re.findall("(\d{1,2}[-]\d{1,2}[-]\d{4} \d{2}[:]\d{2} (?:AM|PM))", old_file, re.IGNORECASE | re.DOTALL)

print("Program found dates in the file and divied them into 3 groups:\n",
      first_old_date, "\n", second_old_date, "\n", third_old_date)


first_new_date = []
for x in first_old_date:
    change_1 = datetime.strptime(x, "%b %d %Y %H:%M %p")
    new_1 = datetime.strftime(change_1, "%d.%m.%Y %H:%M")
    first_new_date.append(new_1)


second_new_date = []
for x in second_old_date:
    change_2 = datetime.strptime(x, "%m/%d/%Y %H:%M")
    new_2 = datetime.strftime(change_2, "%d.%m.%Y %H:%M")
    second_new_date.append(new_2)


third_new_date = []
for x in third_old_date:
    change_3 = datetime.strptime(x, "%d-%m-%Y %H:%M %p")
    new_3 = datetime.strftime(change_3, "%d.%m.%Y %H:%M")
    third_new_date.append(new_3)


print("Program changed all dates into new date format:\n",
    first_new_date, "\n", second_new_date, "\n", third_new_date)
print("All new dates have saved in the new txt file")


new_path = "file_with_new_date.txt"
with open(new_path, 'w') as f:
    for i in first_new_date:
        f.write(str(i))
        f.write("\n")
    for i in second_new_date:
        f.write(str(i))
        f.write("\n")
    for i in third_new_date:
        f.write(str(i))
        f.write("\n")

