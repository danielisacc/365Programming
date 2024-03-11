import sqlite3 as db
import Animals as anim


class Database:
    conn = db.connect("animals_db.db")
    curr = conn.cursor()

    def __init__(self) -> None:

        try:
            Database.curr.execute("""
                            CREATE TABLE IF NOT EXISTS animals (
                            animal_id INTEGER PRIMARY KEY,
                            name TEXT,
                            sound TEXT,
                            age INTEGER
                            )
                            """)
        except db.DatabaseError as dbErr:
            print("Animal Table Creation Failed..." + dbErr)
        except db.Error as e:
            print("Animal Table Creation Failed..." + e)
        else:
            print("Animals DB Initialized...")

    def add_animal(self, animal: anim.Animal):
        Database.curr.execute("SELECT COUNT(*) FROM animals")
        animal_id = Database.curr.fetchone()[0] + 1

        Database.curr.execute(f"""INSERT INTO animals VALUES(
                              {animal_id},'{animal.name}','{animal.sound}',{animal.age}
                            )""")
        print(f"{animal.name} added successful!")

    def retrieve_animal(self, animal_id: int) -> anim.Animal:
        Database.curr.execute(
            f"SELECT * FROM animals WHERE animal_id = {animal_id}")
        animal = Database.curr.fetchone()
        return anim.Animal(name=animal[1], sound=animal[2], age=animal[3])

    def db_commit(self):
        Database.conn.commit()


animal = anim.Animal(name="Firby", sound="Hummm", age=2)
db = Database()
db.add_animal(animal)
db.db_commit()
animal = db.retrieve_animal(4)
print(animal)
