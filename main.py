import sqlite3

def initialize_db():
    conn = sqlite3.connect("jobs.db")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS jobs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        title TEXT NOT NULL,
        status TEXT NOT NULL,
        date_applied TEXT
    )
    """)
    conn.commit()
    conn.close()

def create_job():
    comp_name = input("Company Name: ")
    job_title = input("Position Name: ")
    status = input("Status of Application: ")
    date_applied = input("Date Applied: ")

    conn = sqlite3.connect("jobs.db")
    conn.execute("INSERT INTO jobs(company, title, status, date_applied) VALUES (?, ?, ?, ?)",
                 (comp_name, job_title, status, date_applied))
    conn.commit()
    conn.close()


def view_all_jobs():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    results = cursor.fetchall()
    for row in results:
        print(f"[{row[0]}] {row[1]} - {row[2]} - {row[3]} - {row[4]}")
    conn.close()

def show_menu():
    print("1. Add a new job")
    print("2. View saved jobs")
    print("3. Exit")

def main():
    initialize_db()
    while True:
        show_menu()
        choice = input("Choose a option (1-3): ")

        if choice == '1':
            create_job()
        elif choice == '2':
            view_all_jobs()
        elif choice == '3':
            break
        else:
            print("Invalid options. Please choose a valid option.")

   
if __name__ == "__main__":
    main()