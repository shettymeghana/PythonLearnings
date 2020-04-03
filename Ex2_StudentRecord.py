#Take inputs from 5 different students which include marks of sub1, sub2, sub3, sub4, sub5 and Student name.
# Calculate average and percentage marks. As per highest percentage mark, display name of Student as output

n = int(raw_input("Enter the number of student -> "))
all_students = []
for i in range(0,n):
    std_name = raw_input("Enter the Name of the student: ")
    subject1 = int(raw_input("Enter the marks of Subject1 "))
    subject2 = int(raw_input("Enter the marks of Subject2 "))
    subject3 = int(raw_input("Enter the marks of Subject3 "))
    subject4 = int(raw_input("Enter the marks of Subject4 "))
    subject5 = int(raw_input("Enter the marks of Subject5 "))
    total = subject1 + subject2 + subject3 + subject4 + subject5
    #print "Total of %s is %d "%(all_students[std_name],total)
    average = total / 5
    #print "Average of %s is %d " % (all_students[std_name], average)

    all_students.append({'Name': std_name, 'm1': subject1, 'm2': subject2, 'm3': subject3, 'm4': subject4,
                           'm5': subject5, 'Total': total, 'Average': average})
    print type(all_students)
for students in all_students:
    #print "\n"
    for key,value in students.items():
        print '{0}:{1}'.format(key,value)
        max_avg = sorted(students.values(),reverse=True)
        print max_avg
