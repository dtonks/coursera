import csv

users = [ {'name': 'Sol Mansi', 'username': 'solm', 'department': 'IT infrastructure'},
          {'name': 'Lio Nelson', 'username': 'lion', 'department': 'User Experience Research'},
          {'name': 'Charlie Grey', 'username': 'greyc', 'department': 'Development'}]
keys = ['name', 'username', 'department']
with open('by_department.csv', 'w') as d:
  writer = csv.DictWriter(d, fieldnames=keys)
  writer.writeheader()
  writer.writerows(users)
