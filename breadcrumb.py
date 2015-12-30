import json
import csv

datafile = 'crouton.csv'
enrollmentsfile = 'enrollments.json'
popularfile = 'popular.json'

def calc_average_enrollment(enrollment_list):
	total = 0
	for key in enrollment_list:
		total += float(enrollment_list[key])
	return total / len(enrollment_list.keys())

with open(datafile, 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	course_dict = {}
	for row in reader:
		quarter_code = 0

		if row['academic_quarter'] == "Winter":
			quarter_code = 1
		elif row['academic_quarter'] == "Spring":
			quarter_code = 2
		elif row['academic_quarter'] == "Summer":
			quarter_code = 3
		elif row['academic_quarter'] == "Fall":
			quarter_code = 4

		course_key = "{} {}-{}".format(row['academic_subject_code'], row['course_number'], row['course_subnum'])
		course_term = "{}-{}".format(quarter_code, row['academic_year'])

		if course_key in course_dict.keys():
			this_course = course_dict[course_key]

			if course_term in this_course['enrollment_list'].keys():
				this_course['enrollment_list'][course_term] += int(row['enrollment_count'])
			else:
				this_course['enrollment_list'][course_term] = int(row['enrollment_count'])

			this_course['average_enrollment'] = calc_average_enrollment(this_course['enrollment_list'])
		else:
			course_dict[course_key] = {
				# 'academic_subject_code' : row['academic_subject_code'],
				# 'course_number_full' : "{}-{}".format(row['course_number'], row['course_subnum']),
				# 'course_name' : row['course_name'],
				'course_name' : row['course_name'],
				'average_enrollment' : int(row['enrollment_count']),
				'enrollment_list' : {
					course_term : int(row['enrollment_count'])
				}
			}

	with open(enrollmentsfile, 'w') as outfile:
		 json.dump(course_dict, outfile)

most_popular_courses = {}
min_enroll = 0
for course_key in course_dict.keys():
	if len(most_popular_courses.keys()) < 20:
		most_popular_courses[course_key] = course_dict[course_key]
		min_key = min(most_popular_courses.iterkeys(), key=(lambda key: most_popular_courses[key]['average_enrollment']))
		min_enroll = most_popular_courses[min_key]['average_enrollment']
	elif course_dict[course_key]['average_enrollment'] > min_enroll:
		most_popular_courses[course_key] = course_dict[course_key]
		min_key = min(most_popular_courses.iterkeys(), key=(lambda key: most_popular_courses[key]['average_enrollment']))
		min_enroll = most_popular_courses[min_key]['average_enrollment']
		most_popular_courses.pop(min_key, None)
		min_key = min(most_popular_courses.iterkeys(), key=(lambda key: most_popular_courses[key]['average_enrollment']))
		min_enroll = most_popular_courses[min_key]['average_enrollment']

with open(popularfile, 'w') as outfile:
	 json.dump(most_popular_courses, outfile)
