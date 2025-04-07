# Flask CRUD App with MySQL

A simple **CRUD (Create, Read, Update, Delete)** web application built using **Flask (Python)** and **MySQL**, styled with **Bootstrap 5**. This project demonstrates the basics of how to use Flask with MySQL, manage routes, templates, and perform database operations in a clean, beginner-friendly structure.

---

## 🛠 Features

✅ Add new user  
✅ List all users  
✅ Edit user details  
✅ Delete user  


## 🚀 Tech Stack

- Python 3.x
- Flask
- MySQL Connector (mysql-connector-python)
- Jinja2 templating engine
- Bootstrap 5
- HTML/CSS/JS




## 🧑‍💻 Getting Started

### 🔧 Prerequisites

- Python 3.x
- MySQL server
- pip

---

### ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/intsar/flask-crud-app.git
cd flask-crud-app
Update DB credentials in confir.py
Create new table 
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20)
);

python app.py

