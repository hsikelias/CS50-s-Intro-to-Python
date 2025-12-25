students = [
  {"name": "Hermione","house":"Gryffindor","patronus":"Otter"},
  {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
  {"name":"Ron","house":"Gryffindor","patronus":"Jack Russell terrier"},
  {"name":"Draco","house":"Slytherin","patronus":None}
]

# None = means there is no value for that key.
# we make a list of dictionaries, each student is in a dictionary in itself

for student in students:
  print(student)
  print(student["name"], student["house"], sep=", ")
