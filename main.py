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

def main():
    initialize_db()
    
    comp_name = input("Company Name: ")
    job_title = input("Position Name: ")
    status = input("Status of Application: ")
    date_applied = input("Date Applied: ")

    conn = sqlite3.connect("jobs.db")
    conn.execute("INSERT INTO jobs(company, title, status, date_applied) VALUES (?, ?, ?, ?)",
                 (comp_name, job_title, status, date_applied))
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    main()