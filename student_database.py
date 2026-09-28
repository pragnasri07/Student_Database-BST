# Student Database Management Using Binary Search Tree

# Student class
class Student:
    def __init__(self, roll_no, name, age, branch, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.branch = branch
        self.cgpa = cgpa


# BST Node class
class Node:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None


# Binary Search Tree class
class StudentBST:
    def __init__(self):
        self.root = None

    # Insert student
    def insert(self, student):
        new_node = Node(student)

        if self.root is None:
            self.root = new_node
            print("Student added successfully!")
            return

        current = self.root

        while True:
            if student.roll_no < current.student.roll_no:

                if current.left is None:
                    current.left = new_node
                    print("Student added successfully!")
                    return

                current = current.left

            elif student.roll_no > current.student.roll_no:

                if current.right is None:
                    current.right = new_node
                    print("Student added successfully!")
                    return

                current = current.right

            else:
                print("Roll number already exists!")
                return

    # Search student
    def search(self, roll_no):
        current = self.root

        while current is not None:

            if roll_no == current.student.roll_no:
                return current.student

            elif roll_no < current.student.roll_no:
                current = current.left

            else:
                current = current.right

        return None

    # Display students using inorder traversal
    def display(self, node):
        if node is not None:
            self.display(node.left)

            student = node.student

            print("--------------------------------")
            print("Roll Number :", student.roll_no)
            print("Name        :", student.name)
            print("Age         :", student.age)
            print("Branch      :", student.branch)
            print("CGPA        :", student.cgpa)

            self.display(node.right)

    # Find minimum node
    def find_min(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    # Delete student
    def delete(self, node, roll_no):

        if node is None:
            return None

        if roll_no < node.student.roll_no:
            node.left = self.delete(node.left, roll_no)

        elif roll_no > node.student.roll_no:
            node.right = self.delete(node.right, roll_no)

        else:

            # No child
            if node.left is None and node.right is None:
                return None

            # Only right child
            if node.left is None:
                return node.right

            # Only left child
            if node.right is None:
                return node.left

            # Two children
            successor = self.find_min(node.right)

            node.student = successor.student

            node.right = self.delete(
                node.right,
                successor.student.roll_no
            )

        return node


# Main program
def main():

    bst = StudentBST()

    while True:

        print("\n======================================")
        print("   STUDENT DATABASE MANAGEMENT")
        print("======================================")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display Students")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        # Add student
        if choice == "1":

            try:
                roll_no = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                branch = input("Enter Branch: ")
                cgpa = float(input("Enter CGPA: "))

                if cgpa < 0 or cgpa > 10:
                    print("CGPA must be between 0 and 10.")
                    continue

                student = Student(
                    roll_no,
                    name,
                    age,
                    branch,
                    cgpa
                )

                bst.insert(student)

            except ValueError:
                print("Please enter valid values.")

        # Search student
        elif choice == "2":

            try:
                roll_no = int(input("Enter Roll Number to search: "))

                student = bst.search(roll_no)

                if student is not None:
                    print("\nStudent Found!")
                    print("--------------------------------")
                    print("Roll Number :", student.roll_no)
                    print("Name        :", student.name)
                    print("Age         :", student.age)
                    print("Branch      :", student.branch)
                    print("CGPA        :", student.cgpa)
                    print("--------------------------------")

                else:
                    print("Student not found!")

            except ValueError:
                print("Please enter a valid roll number.")

        # Display students
        elif choice == "3":

            if bst.root is None:
                print("Database is empty!")

            else:
                print("\n===== STUDENT RECORDS =====")
                bst.display(bst.root)
                print("--------------------------------")

        # Update student
        elif choice == "4":

            try:
                roll_no = int(input("Enter Roll Number to update: "))

                student = bst.search(roll_no)

                if student is not None:

                    print("\nCurrent Details")
                    print("Name   :", student.name)
                    print("Age    :", student.age)
                    print("Branch :", student.branch)
                    print("CGPA   :", student.cgpa)

                    print("\nEnter New Details")

                    student.name = input("Enter New Name: ")
                    student.age = int(input("Enter New Age: "))
                    student.branch = input("Enter New Branch: ")
                    student.cgpa = float(input("Enter New CGPA: "))

                    if student.cgpa < 0 or student.cgpa > 10:
                        print("CGPA must be between 0 and 10.")
                    else:
                        print("Student updated successfully!")

                else:
                    print("Student not found!")

            except ValueError:
                print("Please enter valid values.")

        # Delete student
        elif choice == "5":

            try:
                roll_no = int(input("Enter Roll Number to delete: "))

                student = bst.search(roll_no)

                if student is not None:

                    bst.root = bst.delete(
                        bst.root,
                        roll_no
                    )

                    print("Student deleted successfully!")

                else:
                    print("Student not found!")

            except ValueError:
                print("Please enter a valid roll number.")

        # Exit
        elif choice == "6":

            print("\nThank you for using Student Database Management System!")
            break

        else:
            print("Invalid choice! Please select 1 to 6.")


# Start program
if __name__ == "__main__":
    main()