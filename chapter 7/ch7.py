#Problem 1: Basic SQLite CRUD

  import sqlite3
   
  conn = sqlite3.connect('school.db')
  cursor = conn.cursor()
   
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS students (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
     grade REAL
 )
 ''')
  
 students = [
     (1, 'Ali', 85.5),
     (2, 'Sara', 92.0),
     (3, 'Mohamed', 78.3)
 ]
  
 cursor.executemany('INSERT INTO students VALUES (?, ?, ?)', students)
 conn.commit()
  
 cursor.execute('SELECT * FROM students')
 for row in cursor.fetchall():
     print(row)
  
 conn.close()


#Problem 2: Parameterized Queries
 
  import sqlite3
   
  conn = sqlite3.connect('school.db')
  cursor = conn.cursor()
   
  name = input("Enter name: ")
  grade = float(input("Enter grade: "))
   
  cursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)', (name, grade))
 conn.commit()
  
 cursor.execute('SELECT * FROM students')
 print("--- Updated Records ---")
 for row in cursor.fetchall():
     print(row)
 
 conn.close()





#Problem 3: Transactions

  import sqlite3
   
  conn = sqlite3.connect('school.db')
  cursor = conn.cursor()
   
  try:
      conn.execute('BEGIN')
      
      cursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)', ('Omar', 90.0))
     cursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)', ('Fatima', 95.5))
     
     result = 10 / 0 
     
     conn.commit()
     print("Transaction committed successfully.")
     
 except ZeroDivisionError as e:
     print(f"Error occurred: {e}")
     conn.rollback()
     print("Transaction rolled back.")
     
     cursor.execute('SELECT * FROM students')
     print("Final Records:")
     for row in cursor.fetchall():
         print(row)
  
 finally:
     conn.close()











#Problem 4: ORM with SQLAlchemy

  from sqlalchemy import create_engine, Column, Integer, String
  from sqlalchemy.ext.declarative import declarative_base
  from sqlalchemy.orm import sessionmaker
   
  Base = declarative_base()
   
  class Book(Base):
      __tablename__ = 'books'
     
     id = Column(Integer, primary_key=True)
     title = Column(String)
     author = Column(String)
     
    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}')"
  
 engine = create_engine('sqlite:///books.db')
 Base.metadata.create_all(engine)
 
Session = sessionmaker(bind=engine)
session = Session()
 
 book1 = Book(title='Python Basics', author='Guido')
 book2 = Book(title='AI with Python', author='Mohamed')
  
 session.add(book1)
 session.add(book2)
 session.commit()
 
 books = session.query(Book).all()
 for book in books:
print(book)

 session.close()
