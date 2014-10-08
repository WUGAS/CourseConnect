#Be able to use the parse function from tableparser.py
from tableparser import convertToArray

def updateCourseRank(ratings):
	currTable = convertToArray()
	courseFound = False
	counter = 0
	#iterating through all the courses the user rated
	for rating in ratings:
		#iterating through all the courses in the database
		for courseMainTable in currTable:
			#check to see if you foudn the course
			if (rating[0] == courseMainTable[0] and rating[1] == courseMainTable[1]):
				print counter
				courseFound = True
				#if number of ratings is 0, then update ratings with user ratings
				if (courseMainTable[16] == "0\n"):
					for rat in range(2, 9):
						courseMainTable[rat] = rating[rat]
				else:
					avg = courseMainTable[16]
					for rat in range(2, 9):
						newRating = (avg * courseMainTable[rat] + rating[rat]) / float(avg + 1)
						courseMainTable[rat] = newRating
				break
			counter += 1
		if courseFound:
			break
	return currTable

#Check some stuff, len = 4005
#print len(convertToArray())
#print convertToArray()[4004]

#Example Test
#course: EECS 354
#rankings: 1, 3, 1, 2, 3, 1, 2
rankings = [["EECS", "348-0", 1, 3, 1, 2, 3, 1, 2]]
arr = updateCourseRank(rankings)
for i in range(1060, 1070):
	print arr[i]
