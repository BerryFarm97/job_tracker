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

def create_job():                     #creates new job listings
    comp_name = input("Company Name: ")
    job_title = input("Position Name: ")
    status = input("Status of Application: ")
    date_applied = input("Date Applied: ")

    conn = sqlite3.connect("jobs.db")
    conn.execute("INSERT INTO jobs(company, title, status, date_applied) VALUES (?, ?, ?, ?)",
                 (comp_name, job_title, status, date_applied))
    conn.commit()
    conn.close()


def view_all_jobs():                       #list saved jobs
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs ORDER BY company ASC")  #Adjust this to sort jobs alphabetically
    results = cursor.fetchall()
    for row in results:
        print(f"[{row[0]}] {row[1]} - {row[2]} - {row[3]} - {row[4]}")
    conn.close()

def show_menu():                 #Add a menu for easy choice selection
    print("1. Add a new job")
    print("2. View saved jobs")
    print("3. Remove job")
    print("4. Update Status")
    print("5. Exit")

def delete_job():                 #lets you remove listings if no longer needed
    print("\nCurrent Job Applications:")   #Added this to make it smoother for user when trying to remove a job listing
    view_all_jobs()
    print("Which jobs would you like to remove?")
    job_id = input("Enter the ID of the job you want to delete: ")
    
    conn = sqlite3.connect("jobs.db")
    conn.execute("DELETE FROM jobs WHERE id = ?", (job_id))
    conn.commit()
    conn.close()
    print(f"Job with ID {job_id} has been deleted.")

def update_status():
    print("\nCurrent Job Applications:")
    view_all_jobs()
    job_id = input("Enter the ID of the job you want to update: ")
    new_status = input("Enter the new status (ex: Interviewing, Offer, Rejected): ")

    conn = sqlite3.connect("jobs.db")
    conn.execute("UPDATE jobs SET status = ? WHERE id = ?", (new_status, job_id))
    conn.commit()
    conn.close()

    print(f"Job ID {job_id} updated to status '{new_status}'.\n")

def main():
    initialize_db()
    while True:
        show_menu()
        choice = input("Choose a option (1-5): ")

        if choice == '1':
            create_job()
        elif choice == '2':
            view_all_jobs()
        elif choice == '3':
            delete_job()
        elif choice == '4':
            update_status()
        elif choice == '5':
            break
        else:
            print("Invalid options. Please choose a valid option.")

   
if __name__ == "__main__":
    main()