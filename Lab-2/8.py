# Create an empty set to store all students' roll numbers
master = set()
n_master = int(input("Enter total number of students: "))
print("Enter roll numbers of all students:")
for _ in range(n_master):
    master.add(int(input()))

# Create a set for students who play cricket
cricket = set()
n_cricket = int(input("Enter number of students who play cricket: "))
print("Enter roll numbers of students who play cricket:")
for _ in range(n_cricket):
    cricket.add(int(input()))

# Create a set for students who play football
football = set()
n_football = int(input("Enter number of students who play football: "))
print("Enter roll numbers of students who play football:")
for _ in range(n_football):
    football.add(int(input()))

# Find students who play both cricket and football
both = cricket.intersection(football)
# Find students who play only one of the two sports
only_one = cricket.symmetric_difference(football)
# Find students who play neither cricket nor football
neither = master.difference(cricket.union(football))

print("\nStudents who play both sports:", sorted(both))
print("Students who play only one sport:", sorted(only_one))
print("Students who play neither sport:", sorted(neither))
print("Students who play neither sport:", sorted(neither))
