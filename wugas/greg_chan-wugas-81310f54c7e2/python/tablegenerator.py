import urllib2
import json
import random

resp = urllib2.urlopen("http://vazzak2.ci.northwestern.edu/subjects/")
#send the html get request
#html is the json string returned
html = resp.read()

#parsing of the json string
#putting the list of departments in depts (array type)
js = json.loads(html)
depts = []
for x in range(0, len(js)):
	depts.append(js[x]['symbol'])

#checkpoint
print len(depts)
print depts[0]
	
#get first (latest) term
resp = urllib2.urlopen("http://vazzak2.ci.northwestern.edu/terms/")
html = resp.read()

#parse
#terms = []
js = json.loads(html)
#for x in range(0, len(js)):
term = js[1]['term_id']

#checkpoint
#print terms[0]
print term

#looping through the departments and generating for one term
#1) overall rating of instruction
#2) overall rating of course
#3) how much did you learn in the class
#4) how intellectually difficult was the course
#5) how effective was the instructor
#6) how time-consuming was the class
#7) how fulfilling was the class
courses = []
count = 0
#for term in terms:
for dept in depts:
	resp = urllib2.urlopen("http://vazzak2.ci.northwestern.edu/courses/?term=" + str(term) + "&subject=" + dept)
	html = resp.read()
	js = json.loads(html)
	if (not html == ''):
#		print dept
		for x in range(0, len(js)):
			class_title = js[x]['title']
#			print class_title
			class_num = js[x]['catalog_num']
			instructor = js[x]['instructor']['name']
			location = js[x]['room']
			rating1 = random.random() * 2 + 1
			rating2 = random.random() * 2 + 1
			rating3 = random.random() * 2 + 1
			rating4 = random.random() * 2 + 1
			rating5 = random.random() * 2 + 1
			rating6 = random.random() * 2 + 1
			rating7 = random.random() * 2 + 1
			start_time = js[x]['start_time']
			end_time = js[x]['end_time']
			days = js[x]['meeting_days']
			#Check if there are components (Labs, Discussion, etc)
			components = []
			comp = js[x]['coursecomponent_set']
			if (comp == ''):
				components.append([""])
			else:
				for ii in range(0, len(comp)):
					components.append([comp[ii]['meeting_days'], comp[ii]['start_time'], comp[ii]['end_time'], comp[ii]['room'], comp[ii]['section']])
			courses.append([dept, class_num, rating1, rating2, rating3, rating4, rating5, rating6, rating7, class_title, instructor, location, start_time, end_time, days, components, 0])
#		print "\n"


#checkpoint
for i in range(0, len(courses)):
	test = courses[i]
	for j in range(0, len(test)):
		print test[j]
	print "\n"

#writing to file
f = open('table.txt', 'w')
for i in range(0, len(courses)):
	test = courses[i]
	line = test[0]
	for j in range(1, len(test)):
		line += "::" + str(test[j])
	line += "\n"
	f.write(line)
f.close()
	
