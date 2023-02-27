# Import libraries
# Using Beautiful Soup to scrape the given html file for data.

# Question 1 to 6
from bs4 import BeautifulSoup
import re
from collections import Counter


with open("python_class_question.html", "r", encoding='utf-8') as f:
    html_text = f.read()
# Create a BeautifulSoup object
soup = BeautifulSoup(html_text, "lxml")

# Find the table element can specify a table using class element
table = soup.find("table")

# Find all the table rows within the table element
trs = table.find_all("tr")

# Loop through each row and extract the data
data = []
for tr in trs:
    # Find all the table cells within the row
    tds = tr.find_all("td")
    # If there are cells, append them to the data list as text
    if tds:
        data.append([td.text.strip() for td in tds])

# Print the data list
print(data)
colors = []
for day in data:
    color_str = day[1]
    color_list = re.findall(r'\b\w+\b', color_str)
    colors.extend(color_list)

color_counts = Counter(colors)

# Mean color
mean_color = color_counts.most_common()[0][0]

# Most worn color
most_worn_color = color_counts.most_common()[0][0]

# Median color
sorted_colors = sorted(color_counts.items(), key=lambda x: x[1])
median_color = sorted_colors[len(sorted_colors)//2][0]

# Variance of the colors
mean_frequency = sum(color_counts.values()) / len(color_counts)
variance = sum((freq - mean_frequency) ** 2 for freq in color_counts.values()) / len(color_counts)

# Probability of red color
red_prob = color_counts['RED'] / sum(color_counts.values())

print(mean_color, most_worn_color, median_color, variance, red_prob)

# Saving colors and frequencies to PostgreSQL database
import psycopg2
conn = psycopg2.connect(dbname='mydb', user='myuser', password='mypassword', host='localhost')
cur = conn.cursor()

for color, count in color_counts.items():
    cur.execute("INSERT INTO colors (color, count) VALUES (%s, %s)", (color, count))

conn.commit()
cur.close()
conn.close()


# Question 7

def recursive_search(num_list, num_to_find):
    # Check if the list is empty
    if not num_list:
        return False

    # Check if the first element of the list is the number
    if num_list[0] == num_to_find:
        return True

    # If the number is not found yet, search the rest of the list recursively
    return recursive_search(num_list[1:], num_to_find)

num_list = [1, 2, 3, 4, 5]
num_to_find = 3

if recursive_search(num_list, num_to_find):
    print("The number is found in the list.")
else:
    print("The number is not found in the list.")

# Question 8
import random

def ran_binary():
    # Generate a random 4-digit binary number
    binary_num = ''.join([str(random.randint(0, 1)) for _ in range(4)])

    # Convert the binary number to base 10
    decimal_num = int(binary_num, 2)

    # Print the results
    print("Question 8 : Random 4-digit binary number: ", binary_num)
    print("Decimal equivalent: ", decimal_num)


ran_binary()


# Question 9
def fib_sum(n):
    # Define the first two numbers in the Fibonacci sequence
    a, b = 0, 1

    # Initialize a variable to keep track of the sum
    fib_sum = 0

    # Calculate the first 50 Fibonacci numbers and add them to the sum
    for i in range(n):
        fib_sum += a
        a, b = b, a + b

    return fib_sum


# Print the sum of the first 50 Fibonacci numbers
print("Question 9 answer:", fib_sum(50))
