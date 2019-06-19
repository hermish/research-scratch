from algorithms import *

# Stable marriage algorithm
men = {"A": ["4", "3", "2", "1"],
	"B": ["4", "2", "3", "1"],
	"C": ["4", "2", "3", "1"],
	"C": ["4", "2", "1", "3"]}

women = {"1": ["C", "B", "A", "D"],
	"2": ["D", "C", "B", "A"],
	"3": ["D", "C", "B", "A"],
	"4": ["C", "D", "B", "A"]}

output = stable_marriage(men, women, count=True)
print(output)
