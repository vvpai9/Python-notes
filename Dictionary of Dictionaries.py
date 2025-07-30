bvb = {}
while True:
    print ("", "1: Add a new student","2: Modify Student Details", "3: Delete a student", "4: Search a student", "5: Display All", "0: Exit", sep = '\n')
    ch = int (input ("Enter your choice: "))
    if ch == 1 :
        usn = input ("Enter USN: ")
        stud = {}
        stud["Roll No."] = int(input("Enter Roll No.:"))
        stud["Name"] = input("Enter Name:")
        stud["Percentage"] = float(input("Enter percentage: "))
        bvb[usn] = stud
        print ("Added successfully")
    elif ch == 2 :
        usn = input("Enter USN: ")
        if usn in bvb:
            stud = bvb[usn]
            print ("Existing data:", "Roll No.: %d"%stud["Roll No."], "Name: %s"%stud["Name"], "Percentage: %f"%stud["Percentage"], sep = '\n')
            print ("")
            stud["Roll No."] = int(input("Enter new Roll No.:"))
            stud["Name"] = input("Enter new Name:")
            stud["Percentage"] = float(input("Enter new percentage: "))
            bvb[usn] = stud
            print("Updated successfully")
        else:
            print ("Student record with USN", usn, "not found")
    elif ch == 3:
        usn = input("Enter USN of student to be deleted: ")
        stud = bvb.pop (usn, None)
        if stud == None:
            print("Student record with USN", usn, "not found")
        else:
            print ("Deleted student record:", "USN: %s"%usn, "Roll No.: %d"%stud["Roll No."], "Name: %s"%stud["Name"], "Percentage: %f"%stud["Percentage"], sep = '\n')
    elif ch == 4:
        usn = input("Enter USN of student to search: ")
        if usn in bvb:
            print ("Student record found:", "USN: %s"%usn, "Roll No.: %d"%stud["Roll No."], "Name: %s"%stud["Name"], "Percentage: %f"%stud["Percentage"], sep = '\n')
        else:
            print("Student record with USN", usn, "not found")
    elif ch == 5:
        print ("Student details: ")
        print ("USN", "Roll No.", "Name", "Percentage", sep = '\t')
        for stud in bvb:
            s = bvb[stud]
            print ("USN: %s"%stud, "Roll No.: %d"%s["Roll No."], "Name: %s"%s["Name"], "Percentage: %f"%s["Percentage"],"", sep = '\n')
    elif ch == 0:
        break
    else:
        print ("Invalid choice")