# Job Application Tracker (Python + SQLite)

A simple command-line tool that helps you track your job applications locally using Python and SQLite.

## 💡 Features

- Add a new job application (company, role, status, date applied)
- Stores entries in a local SQLite database (`jobs.db`)
- Lightweight and runs entirely in your terminal
- Easy to extend with new features (listing, filtering, updating status, etc.)

## 🔧 Technologies

- Python 3
- SQLite (via Python's built-in `sqlite3` module)
- Git + GitHub for version control

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/BerryFarm97/job_tracker.git
cd job_tracker


python -m venv venv
venv\Scripts\activate  # On Windows


python main.py


📁 File Structure

    main.py – Main logic for interacting with the job database

    README.md – You're looking at it!

    jobs.db – SQLite database file (auto-created)

    ✅ Future Plans

    View all job applications

    Update application status

    Delete entries

    Export summary/report


👤 Author

Created by Austin Granbery
GitHub: BerryFarm97