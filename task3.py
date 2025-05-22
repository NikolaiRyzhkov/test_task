from sys import argv
import re
from packaging import version

grep_ver, config_file = argv[1:]
grep_ver = version.parse(grep_ver)

# read config file
data = ''
with open(config_file, 'r', encoding="utf-8") as file:
    for line in file:
        data += line\

data = data[1:-2].split(', ')


# Changing the format of recording versions
list_template = list()
for template in data:
    temp = template.split(':')
    temp[1] = re.sub(r"[”]", '', temp[1])
    for num in range(2):
        ver = version.parse(re.sub(r'[*]', str(num), temp[1]))
        list_template.append(ver)

list_template = sorted(list_template)

print('Sorted list of versions:')
for template in list_template:
    print(template)

print(f'\nVersions earlier {grep_ver}:')
for template in list_template:
    if template < grep_ver:
        print(template)