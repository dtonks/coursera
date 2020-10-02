import csv
with open('software.csv') as s:
  reader = csv.DictReader(s)
  for row in reader:
    print(f"{row['name']} has {row['users']} users")
