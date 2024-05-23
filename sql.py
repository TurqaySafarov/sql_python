import sqlite3


connection = sqlite3.connect("movies_collection.db")
cursor = connection.cursor()


def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            title TEXT, 
            director TEXT, 
            year INT, 
            genre TEXT
        )
    """)


def add_data():
    cursor.execute("INSERT INTO movies VALUES ('Inception', 'Christopher Nolan', 2010, 'Science Fiction')")
    connection.commit()


def dynamic_add_data(title, director, year, genre):
    cursor.execute("INSERT INTO movies VALUES (?, ?, ?, ?)", (title, director, year, genre))
    connection.commit()


def show_data():
    cursor.execute("SELECT * FROM movies")
    data = cursor.fetchall()
    for row in data:
        print(row)


def dynamic_show_data(director):
    cursor.execute("SELECT title FROM movies WHERE director = ?", (director,))
    data = cursor.fetchall()
    for row in data:
        print(row)


def update_data(old_genre, new_genre):
    cursor.execute("UPDATE movies SET genre = ? WHERE genre = ?", (new_genre, old_genre))
    connection.commit()


def delete_data(director):
    cursor.execute("DELETE FROM movies WHERE director = ?", (director,))
    connection.commit()


if __name__ == "__main__":
    create_table()
    add_data()
    dynamic_add_data('The Matrix', 'Lana Wachowski, Lilly Wachowski', 1999, 'Science Fiction')
    show_data()
    dynamic_show_data('Christopher Nolan')
    update_data('Science Fiction', 'Sci-Fi')
    delete_data('Christopher Nolan')
    
    Close the connection
    connection.close()
