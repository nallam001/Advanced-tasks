# Assumes a file students.csv with these contents:

# ID,Name,Grade
# 2. 1,Ali,85
# 3. 2,Mona,92
# 4. 3,Omar,78


# Simple program (uses built-in csv):
  import csv
   
  def print_high_scorers(csv_path, threshold=80):
      with open(csv_path, newline='', encoding='utf-8') as f:
          reader = csv.DictReader(f)
          for row in reader:
              if int(row['Grade']) > threshold:
                 print(row['Name'])
  
 print_high_scorers('students.csv')

# 2) JSON Handling — write dict to JSON then read students list

# Given:

#  data = {"course": "Python", "duration": "3 months", "students": ["Ali", "Sara"]}





# Write to course.json and read back:
  import json
   
  data = {"course": "Python", "duration": "3 months", "students": ["Ali", "Sara"]}
   
  with open('course.json', 'w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=2)
   
  with open('course.json', 'r', encoding='utf-8') as f:
      loaded = json.load(f)
  
 print(loaded['students'])
  


# 3) Excel Handling — create DataFrame, save to Excel, read back Name & Salary

# This uses pandas. Install pandas/openpyxl if needed.

  import pandas as pd
  df = pd.DataFrame([
      {'ID': 1, 'Name': 'Alice', 'Salary': 45000},
      {'ID': 2, 'Name': 'Bob',   'Salary': 52000},
      {'ID': 3, 'Name': 'Carol', 'Salary': 48000},
  ])
  df.to_excel('employees.xlsx', index=False, sheet_name='Employees')
  df2 = pd.read_excel('employees.xlsx', sheet_name='Employees')
  print(df2[['Name', 'Salary']])
  


#4) Data Transformation — CSV (Name,Age,City) → JSON structure with "people"

#Reads a CSV like:
#Name,Age,City
# Ali,25,Cairo
# Mona,30,Alexandria


#and writes:
{
  "people": [
    {"Name": "Ali", "Age": 25, "City": "Cairo"},
    {"Name": "Mona", "Age": 30, "City": "Alexandria"}
  ]
}


#Code:

  import csv
  import json
   
  def csv_to_people_json(csv_path, json_path):
      people = []
      with open(csv_path, newline='', encoding='utf-8') as f:
         reader = csv.DictReader(f)
         for row in reader:
             person = {
                 "Name": row.get("Name", ""),
                 "Age": int(row["Age"]) if row.get("Age", "").isdigit() else row.get("Age", ""),
              "City": row.get("City", "")
          }
             people.append(person)
  
     result = {"people": people}
     with open(json_path, 'w', encoding='utf-8') as f:
         json.dump(result, f, ensure_ascii=False, indent=2)
  
 csv_to_people_json('people.csv', 'people.json')
