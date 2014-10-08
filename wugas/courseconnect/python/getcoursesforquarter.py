import urllib2
import json
response = urllib2.urlopen("http://vazzak2.ci.northwestern.edu/terms/");

terms_json = json.loads(response.read());

terms = []
for term in terms_json:
	terms.append(term["term_id"])

subjects = []
response = urllib2.urlopen("http://vazzak2.ci.northwestern.edu/subjects/");

subjects_json = json.loads(response.read())

subjects = []
for subject in subjects_json:
	subjects.append(subject["symbol"])

for term in terms:
	contents = ""
	for subject in subjects:
		url = "http://vazzak2.ci.northwestern.edu/courses/?term=" + str(term) + "&subject=" + str(subject)
		response = urllib2.urlopen(url);
		courses_json = json.loads(response.read())
		for course in courses_json:
			contents += str(course["id"]) + "~" + str(course["subject"]) + " " + str(course["catalog_num"]) + " - " + str(course["title"]) + " - " + str(course["section"]) + "|"
	print "writing term: " + str(term)
	file = open(str(term) + ".txt", "w")
	file.write(contents)
	file.close()