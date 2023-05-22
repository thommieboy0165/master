import re
from collections import Counter

print("parsing process-list.txt in current directory... done.")

# Find all running processes
with open('process-list.txt', 'r') as f:
	print("Analysing process list... done.")
	totaal = -1
	for line in f.readlines():
		totaal += 1
	print("Total number of processes: " + str(totaal))

# Find all userinvoked processen
with open('process-list.txt', 'r') as f:
	totaal1 = 0
	for line in f.readlines():
		if not re.search(r"(/sbin|/usr|/bin|-bash|PID)", line):
			totaal1 += 1

	print("user-invoked processes:", totaal1)

#Find all running .sh processen
with open('process-list.txt', 'r') as f:
	shlist = []
	for line in f.readlines():
		result1 = re.search(r'\w+\.sh', line)
		if result1:
			shlist.append(result1.group())

	shlist1 = Counter(shlist)
	print("Active scripts (*.sh):")
	for key, value in shlist1.items():
		print(str(value) + "x ", key)

