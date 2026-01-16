Furniture Shop – Web Application

A full-stack Furniture Shop web application built using Django.
This project allows users to browse furniture products, manage a shopping cart, and place orders through a clean and responsive interface.

📌 Features

  User-friendly furniture catalog

  Product categories
  
  Shopping cart functionality

  Customer management

  Admin panel for product control

  Responsive UI with static assets

  SQLite database integration

🛠️ Tech Stack

  Backend   Python

  Django    Framework

  Frontend  HTML5 CSS3 JavaScript Bootstrap

  Database  SQLite3

📂 Project Structure

FurnitureShop/

│

├── FurnitureShop/

│   ├── manage.py

│   ├── db.sqlite3

│   ├── FurnitureShop/

│   │   ├── settings.py

│   │   ├── urls.py

│   │   └── wsgi.py

│

├── FurniApp/

│   ├── admin.py

│   ├── apps.py

│   ├── forms.py

│   ├── models.py

│   ├── views.py

│   ├── urls.py

│   ├── migrations/

│   ├── templates/

│   └── static/

│

└── README.md


🚀 Installation & Setup

Follow these steps to run the project locally:

1️⃣ Clone the Repository

git clone https://github.com/BhosaleAkshay47/Furniture-Shop.git
cd furniture-shop

2️⃣ Create Virtual Environment (Optional but Recommended)

python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

3️⃣ Install Dependencies

pip install django

4️⃣ Run Migrations

python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser
python manage.py createsuperuser

6️⃣ Run the Development Server
python manage.py runserver


Open browser and visit:

http://127.0.0.1:8000/

🔐 Admin Panel
Access Django admin panel:

http://127.0.0.1:8000/admin/


Login using the superuser credentials you created.
