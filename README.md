📝 Personal Notes App

A simple personal note-taking web application built with Python and Django. Users can create an account, securely log in, and manage their personal notes with full CRUD functionality.

This project was developed to practice Django fundamentals, including authentication, database relationships, ORM operations, views, templates, and user-specific data management.

🚀 Features
User Registration: Users can create an account with a username and password.
User Login: Registered users can securely log in.
User Logout: Users can log out of their accounts.
Create Notes: Logged-in users can create personal notes with a title and content.
View Notes: Users can view all their notes from their dashboard.
Update Notes: Users can edit their existing notes.
Delete Notes: Users can delete notes they no longer need.
User-Specific Notes: Each note is associated with its owner, ensuring users can only access their own notes through the application's note views.
Automatic Timestamps: Notes automatically store their creation and last update dates.
🛠️ Technologies Used
Python – Programming language
Django – Backend web framework
SQLite – Database
HTML – Frontend structure
Django Template Language (DTL) – Dynamic template rendering
Git & GitHub – Version control and project hosting
📂 Project Structure
text
personal_note/
│
├── myproject/
│   │
│   ├── myproject/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── codehere/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── codehere/
│   │   │       ├── home.html
│   │   │       ├── signup.html
│   │   │       ├── login.html
│   │   │       ├── dashboard.html
│   │   │       ├── create_note.html
│   │   │       └── update_note.html
│   │   │
│   │