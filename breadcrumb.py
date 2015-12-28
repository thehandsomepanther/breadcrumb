import json
import csv

datafile = 'crouton.csv'
enrollmentsfile = 'enrollments.txt'

def calc_average_enrollment(current_enrollment, average_enrollment, num_terms):
	return (float(current_enrollment) + float(average_enrollment) * (num_terms - 1)) / num_terms

def calc_growth(current_enrollment, previous_enrollment):
	return (float(current_enrollment) - float(previous_enrollment)) / float(previous_enrollment)

with open(datafile, 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	course_dict = {}
	for row in reader:
		course_key = "{} {}-{} {}".format(row['academic_subject_code'], row['course_number'], row['course_subnum'], row['course_name'])
		print course_key
		course_term = "{} {}".format(row['academic_quarter'], row['academic_year'])

		if course_key in course_dict.keys():
			this_course = course_dict[course_key]

			this_course['growth'].append(calc_growth(row['enrollment_count'], this_course['enrollment_counts'][-1]))
			this_course['total_growth'] += calc_growth(row['enrollment_count'], this_course['enrollment_counts'][-1])

			this_course['enrollment_counts'].append(int(row['enrollment_count']))
			this_course['enrollment_terms'].append(course_term)
			this_course['average_enrollment'] = calc_average_enrollment(row['enrollment_count'], this_course['average_enrollment'], len(this_course['enrollment_counts']))
		else:
			course_dict[course_key] = {
				'average_enrollment' : int(row['enrollment_count']),
				'enrollment_counts' : [int(row['enrollment_count'])],
				'enrollment_terms' : [course_term],
				'growth' : [],
				'total_growth': 0
			}

	with open(enrollmentsfile, 'w') as outfile:
		 json.dump(course_dict, outfile)
