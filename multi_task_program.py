# ============================
# Task 1: List Input and Sum
# ============================
print("Task 1: Sum of a List of Integers")
numbers = input("Enter integers separated by spaces: ")
int_list = [int(num) for num in numbers.split()]
total = sum(int_list)
print("Your list:", int_list)
print("Sum of all integers:", total)
print("-" * 40)

# =================================
# Task 2: Tuple of Favorite Books
# =================================
print("Task 2: Favorite Books (Tuple)")
favorite_books = ("To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Hobbit", "The Great Gatsby")
print("My favorite books:")
for book in favorite_books:
    print(book)
print("-" * 40)

# ====================================
# Task 3: Dictionary with User Info
# ====================================
print("Task 3: Personal Information (Dictionary)")
person_info = {}
person_info["name"] = input("Enter your name: ")
person_info["age"] = int(input("Enter your age: "))
person_info["favorite_color"] = input("Enter your favorite color: ")
print("Personal Information:")
print(person_info)
print("-" * 40)

# ================================
# Task 4: Sets and Intersection
# ================================
print("Task 4: Set Intersection")
set1_input = input("Enter integers for the first set (separated by spaces): ")
set2_input = input("Enter integers for the second set (separated by spaces): ")
set1 = set(int(num) for num in set1_input.split())
set2 = set(int(num) for num in set2_input.split())
common_elements = set1 & set2
print("Common elements:", common_elements)
print("-" * 40)

# =============================================
# Task 5: List Comprehension with Word Length
# =============================================
print("Task 5: Words with Odd Number of Characters")
words = ["apple", "banana", "kiwi", "cherry", "grape", "orange"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)
print("-" * 40)
