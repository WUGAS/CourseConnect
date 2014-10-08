import re
def parse():
	courses = []
	file = open("table.txt")
	for line in file :
		# Do string processing here
		arr_parsed = unicode(line.split("::"))
		courses.append(arr_parsed)
	file.close()
	return courses;

def convertToArray():
	courses = []
	file = open("table.txt")
	for line in file:
		arr_parse = line.split("::")
		courses.append(arr_parse)
	file.close()
	return courses

# #checkpoint
# for i in range(0, len(courses)):
# 	test = courses[i]
# 	for j in range(0, len(test)):
# 		print test[j]
# 	print "\n"
