import sqlite3

# Connect to the SQLite database (or create it)
conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

# Create a notes table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
""")
conn.commit()

def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    print("✅ Note added successfully!")

def view_notes():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    if not notes:
        print("No notes found.")
    else:
        for note in notes:
            print(f"{note[0]}. {note[1]} - {note[2]}")

def search_notes():
    keyword = input("Enter keyword to search: ")
    cursor.execute("SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
    notes = cursor.fetchall()
    if not notes:
        print("No matching notes found.")
    else:
        for note in notes:
            print(f"{note[0]}. {note[1]} - {note[2]}")

def delete_note():
    note_id = input("Enter the note ID to delete: ")
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    print("🗑️ Note deleted successfully!")

def main():
    while True:
        print("\n📝 Notes App Menu:")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
