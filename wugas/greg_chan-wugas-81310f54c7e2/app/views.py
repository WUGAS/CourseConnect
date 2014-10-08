from flask import render_template
from flask import request
from app import app
import urllib2
import os
import json

@app.route("/")

@app.route("/index")
def index():
	return render_template("index.html", title="Home", array=[1,2,3])

@app.route("/suggestions")
def suggestions():
	courses = ""
	path = os.path.dirname(os.path.abspath(__file__)) + "/table.txt"
	fyle = open(path)
	for lyne in fyle :
		courses += lyne.rstrip() + "|"
	fyle.close()

	return render_template("suggestions.html", crs=courses)

@app.route("/browse")
def browse():
	courses = ""
	path = os.path.dirname(os.path.abspath(__file__)) + "/table.txt"
	fyle = open(path)
	for lyne in fyle :
		courses += lyne.rstrip() + "|"
	fyle.close()

	return render_template("browse.html", crs=courses)

@app.route("/departments")
def departments():
	response = urllib2.urlopen('http://vazzak2.ci.northwestern.edu/subjects/')
	return response.read()

@app.route("/terms")
def terms():
	response = urllib2.urlopen('http://vazzak2.ci.northwestern.edu/terms/')
	return response.read()

@app.route("/courses")
def courses():
	term = request.args.get('term')
	subject = request.args.get('subject')
	url = 'http://vazzak2.ci.northwestern.edu/courses/?term=' + str(term) + '&subject=' + str(subject)
	print url
	response = urllib2.urlopen(url)
	return response.read()

@app.route("/courses_by_id")
def courses_by_id():
	id = request.args.get('id')
	url = 'http://vazzak2.ci.northwestern.edu/courses/?id=' + str(id)
	print url
	response = urllib2.urlopen(url)
	return response.read()

@app.route("/course_terms")
def course_terms():
	term_id = request.args.get("term_id")
	path = os.path.dirname(os.path.abspath(__file__)) + "/data/" + term_id + ".txt"
	file = open(path, "r")
	contents = file.read()
	return contents

@app.route("/scatter")
def scatter():
	return render_template("scatter.html");

@app.route("/rate")
def rate():
	courses = ""
	path = os.path.dirname(os.path.abspath(__file__)) + "/table.txt"
	fyle = open(path)
	for lyne in fyle :
		courses += lyne.rstrip() + "|"
	fyle.close()
	return render_template("rate.html", crs=courses)

@app.route("/submit")
def submit():
    courses = ""
    print request.args.get('subject') + " " + request.args.get('name')
    path = "app/table.txt"
    # fyle = open(path)
    # for lyne in fyle :
    #     courses += lyne.rstrip() + "|"
    # fyle.close()
    param = [[request.args.get('subject'), request.args.get('name'), request.args.get('one'), request.args.get('two'), request.args.get('three'), request.args.get('four'), request.args.get('five'), request.args.get('six'), request.args.get('seven')]]
    newCourses = []
    fyle = open(path)
    for lyne in fyle :
        arr = lyne.split("::")
        newCourses.append(arr)
    fyle.close()
    courseFound = False
    counter = 0
	#iterating through all the courses the user rated
    for rating in param:
		#iterating through all the courses in the database
		for courseMainTable in newCourses:
			#check to see if you foudn the course
			if (rating[0] == courseMainTable[0] and rating[1] == courseMainTable[1]):
				print counter
				courseFound = True
				#if number of ratings is 0, then update ratings with user ratings
				if (courseMainTable[16] == "0\n"):
					for rat in range(2, 9):
						courseMainTable[rat] = rating[rat]
					courseMainTable[16] = "1\n"
				else:
					avg = courseMainTable[16]
					for rat in range(2, 9):
						newRating = (float(avg) * float(courseMainTable[rat]) + float(rating[rat])) / (float(avg) + 1)
						courseMainTable[rat] = newRating
					courseMainTable[16] = str(int(courseMainTable[16])+1) + "\n"
				break
			counter += 1
		if courseFound:
			break
    f = open('app/table.txt', 'w')
    for i in range(0, len(newCourses)):
        test = newCourses[i]
        line = test[0]
        for j in range(1, len(test)):
            line += "::" + str(test[j])
        f.write(line)
    f.close()
    return ""
