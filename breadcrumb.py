import json
import csv

datafile = 'crouton.csv'
enrollmentsfile = 'enrollments.txt'

def calc_average_enrollment(enrollment_list):
	total = 0
	for key in enrollment_list:
		total += float(enrollment_list[key])
	return total / len(enrollment_list.keys())

with open(datafile, 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	course_dict = {}
	for row in reader:
		course_key = "{} {}-{} {}".format(row['academic_subject_code'], row['course_number'], row['course_subnum'], row['course_name'])
		course_term = "{} {}".format(row['academic_quarter'], row['academic_year'])

		if course_key in course_dict.keys():
			this_course = course_dict[course_key]

			if course_term in this_course['enrollment_list'].keys():
				this_course['enrollment_list'][course_term] += int(row['enrollment_count'])
			else:
				this_course['enrollment_list'][course_term] = int(row['enrollment_count'])

			this_course['average_enrollment'] = calc_average_enrollment(this_course['enrollment_list'])
		else:
			course_dict[course_key] = {
				'average_enrollment' : int(row['enrollment_count']),
				'enrollment_list' : {
					course_term : int(row['enrollment_count'])
				}
			}

	with open(enrollmentsfile, 'w') as outfile:
		 json.dump(course_dict, outfile)
