import statistics, sys

filename: str = sys.argv[1]

item = []
with open(filename, mode="r") as file:
    item = [int(i) for i in file.readlines()]


print("Statistics Summary")
print(f"mean: {statistics.mean(item)}")
print(f"std: {statistics.stdev(item)}")
print(f"min: {min(item)}")
print(f"max: {max(item)}")
