# Django Event Registration System | Online Event Management Platform

EVENT-REGISTRATION-DJANGO is a Python and Django web application for managing event discovery and registrations through a browser-based interface. The project brings together attendee-facing registration flows and administrative event management, with Bootstrap styling and SQLite-backed development setup. It is a practical starting point for learning Django forms, views, authentication, and event-management workflows.


<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=2800&pause=2000&color=A855F7&center=true&vCenter=true&width=940&lines=🎉+Event+Registration+System+🎉;Built+with+Django+%26+Python+🐍;Modern+Event+Management+Platform+🚀" alt="Typing SVG" />

### *A Modern, Feature-Rich Event Management Platform Built with Django*

<p align="center">
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  </a>
  <a href="https://getbootstrap.com/">
    <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
  </a>
  <a href="https://www.sqlite.org/">
    <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License"/>
  </a>
</p>

<p align="center">
  <a href="#-demo">View Demo</a> •
  <a href="#-getting-started">Get Started</a> •
  <a href="#-features">Features</a> •
  <a href="https://github.com/koushik4475/EVENT-REGISTRATION-DJANGO-/issues">Report Bug</a> •
  <a href="https://github.com/koushik4475/EVENT-REGISTRATION-DJANGO-/issues">Request Feature</a>
</p>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

</div>

<br>

## 📋 Table of Contents

- [✨ Features](#-features)
- [🎬 Demo](#-demo)
- [🏗️ Architecture](#️-architecture)
- [🚀 Getting Started](#-getting-started)
- [💻 Usage Guide](#-usage-guide)
- [🗄️ Database Schema](#️-database-schema)
- [🎨 Tech Stack](#-tech-stack)
- [🌐 Deployment](#-deployment)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" width="50" alt="User Features"/>
  
### 👥 User Experience

</div>

<br>

```diff
+ ✅ Seamless Registration Process
+ 🔍 Intuitive Event Discovery
+ 📧 Real-time Email Validation
+ ✔️ Instant Confirmation Feedback
+ 📱 Fully Responsive Design
+ 🎯 Easy-to-use Interface
+ ⚡ Lightning Fast Performance
```

</td>
<td width="50%" valign="top">

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif" width="50" alt="Admin Features"/>
  
### 🛡️ Admin Panel

</div>

<br>

```diff
+ 🎛️ Complete Management Control
+ 👤 Advanced User Management
+ ⚡ Quick Action Buttons
+ 📊 Powerful Bulk Operations
+ 🎯 Full CRUD for Events
+ 🔐 Secure Authentication
+ 📈 Registration Analytics
```

</td>
</tr>
</table>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 🎬 Demo

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="100">
</div>

### 🖼️ Application Screenshots

<details open>
<summary>
  <h3>🎯 Event Registration Form</h3>
  <i>👆 Click to expand/collapse</i>
</summary>
<br>

<div align="center">
  <a href="https://github.com/user-attachments/assets/7c382d81-7e2d-4e10-9ccd-36cb1cda9d41">
    <img src="https://github.com/user-attachments/assets/7c382d81-7e2d-4e10-9ccd-36cb1cda9d41" alt="Event Registration Form" width="100%" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </a>
  <p><b>📝 Clean and intuitive registration interface for seamless user experience</b></p>
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

</details>

<details>
<summary>
  <h3>✅ Registration Success Page</h3>
  <i>👆 Click to view</i>
</summary>
<br>

<div align="center">
  <a href="https://github.com/user-attachments/assets/8a5fcca0-d5e3-409f-a0ac-75092b122df3">
    <img src="https://github.com/user-attachments/assets/8a5fcca0-d5e3-409f-a0ac-75092b122df3" alt="Success Page" width="100%" style="border-radius: 10px;">
  </a>
  <p><b>🎉 Instant confirmation with beautiful success message</b></p>
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

</details>

<details>
<summary>
  <h3>➕ Admin Panel - Adding Events</h3>
  <i>👆 Click to view</i>
</summary>
<br>

<div align="center">
  <a href="https://github.com/user-attachments/assets/c7510cc3-3ac3-4eaf-ac38-3005695bf180">
    <img src="https://github.com/user-attachments/assets/c7510cc3-3ac3-4eaf-ac38-3005695bf180" alt="Admin Add Event" width="100%" style="border-radius: 10px;">
  </a>
  <p><b>🎨 Streamlined event creation with powerful admin interface</b></p>
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

</details>

<details>
<summary>
  <h3>📋 Admin Panel - Event List</h3>
  <i>👆 Click to view</i>
</summary>
<br>

<div align="center">
  <a href="https://github.com/user-attachments/assets/ab23608e-37ae-476b-81b8-41ae32f9aa50">
    <img src="https://github.com/user-attachments/assets/ab23608e-37ae-476b-81b8-41ae32f9aa50" alt="Event List" width="100%" style="border-radius: 10px;">
  </a>
  <p><b>📊 Comprehensive overview with sortable columns and filters</b></p>
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

</details>

<details>
<summary>
  <h3>📝 Admin Panel - Managing Registrations</h3>
  <i>👆 Click to view</i>
</summary>
<br>

<div align="center">
  <a href="https://github.com/user-attachments/assets/6cdc284f-65d0-4fad-b795-c813bcda3fa3">
    <img src="https://github.com/user-attachments/assets/6cdc284f-65d0-4fad-b795-c813bcda3fa3" alt="Manage Registrations" width="100%" style="border-radius: 10px;">
  </a>
  <p><b>⚡ Powerful registration management with bulk action capabilities</b></p>
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

</details>

<details>
<summary>
  <h3>🔐 Admin Login Page</h3>
  <i>👆 Click to view</i>
</summary>
<br>

<div align="center">
  <a href="https://github.com/user-attachments/assets/fc4bcb63-1c59-4421-89b9-67d1e6c558c8">
    <img src="https://github.com/user-attachments/assets/fc4bcb63-1c59-4421-89b9-67d1e6c558c8" alt="Admin Login" width="100%" style="border-radius: 10px;">
  </a>
  <p><b>🛡️ Secure authentication gateway for administrators</b></p>
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

</details>

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 🏗️ Architecture

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="100"><br>
</div>

```mermaid
graph TB
    A[👤 User] -->|Registers| B[🎯 Django Views]
    B -->|Validates| C[📝 Forms]
    C -->|Saves| D[💾 Database]
    E[👨‍💼 Admin] -->|Manages| F[🛡️ Django Admin]
    F -->|CRUD Operations| D
    D -->|Stores| G[🗃️ Events & Registrations]
    
    style A fill:#4CAF50,stroke:#2E7D32,stroke-width:3px
    style E fill:#FF9800,stroke:#F57C00,stroke-width:3px
    style D fill:#2196F3,stroke:#1976D2,stroke-width:3px
    style B fill:#9C27B0,stroke:#7B1FA2,stroke-width:3px
    style F fill:#F44336,stroke:#D32F2F,stroke-width:3px
    style C fill:#00BCD4,stroke:#0097A7,stroke-width:3px
    style G fill:#FFEB3B,stroke:#FBC02D,stroke-width:3px
```

### 📁 Project Structure

```
📦 event-registration-system/
┃
┣ 📂 event_registration/          ⚙️  Main Django project
┃ ┣ 📄 settings.py                🔧 Project configuration
┃ ┣ 📄 urls.py                    🌐 URL routing
┃ ┗ 📄 wsgi.py                    🚀 WSGI configuration
┃
┣ 📂 events/                      💼 Core application
┃ ┣ 📄 models.py                  🗃️  Data models
┃ ┣ 📄 views.py                   👁️  Business logic (CBVs)
┃ ┣ 📄 forms.py                   📝 Form definitions
┃ ┣ 📄 admin.py                   ⚡ Admin customization
┃ ┗ 📂 templates/                 🎨 HTML templates
┃   ┣ 📄 base.html
┃   ┣ 📄 registration_form.html
┃   ┣ 📄 success.html
┃   ┗ 📄 event_list.html
┃
┣ 📂 static/                      🎭 Static assets
┃ ┣ 📂 css/
┃ ┣ 📂 js/
┃ ┗ 📂 images/
┃
┣ 📄 requirements.txt             📦 Dependencies
┣ 📄 manage.py                    🎮 Django CLI
┗ 📄 README.md                    📖 Documentation
```

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 🚀 Getting Started

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100">
</div>

### 📋 Prerequisites

<table>
<tr>
<td align="center" width="33%">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="60"><br>
<b>Python 3.8+</b>
</td>
<td align="center" width="33%">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="60"><br>
<b>pip</b>
</td>
<td align="center" width="33%">
<img src="https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2db.gif" width="60"><br>
<b>Git</b>
</td>
</tr>
</table>

### ⚡ Quick Start Installation

<details open>
<summary><b>📥 Follow These Steps</b></summary>
<br>

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/koushik4475/EVENT-REGISTRATION-DJANGO-.git
cd EVENT-REGISTRATION-DJANGO-
```

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d899-44b4-b1d9-4eeccf656e44.gif" width="400">
</div>

#### 2️⃣ Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Database Setup

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

#### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
# Follow the prompts to set username, email, and password
```

#### 6️⃣ Run Development Server

```bash
python manage.py runserver
```

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284094-e50ac5d1-0b9c-4e5d-8e9a-24fb9896a1fc.gif" width="400">
</div>

#### 7️⃣ Access the Application

<table align="center">
<tr>
<td align="center">
<img src="https://user-images.githubusercontent.com/74038190/216122069-5b8169d7-1d8e-4a13-b245-a8e4176c99f8.png" width="40"><br>
<b>Main Site</b><br>
<a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>
</td>
<td align="center">
<img src="https://user-images.githubusercontent.com/74038190/235294019-40007353-6219-4ec5-b661-b3c35136dd0b.gif" width="40"><br>
<b>Admin Panel</b><br>
<a href="http://127.0.0.1:8000/admin/">http://127.0.0.1:8000/admin/</a>
</td>
</tr>
</table>

</details>

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 💻 Usage Guide

<table>
<tr>
<td width="50%">

### 👤 For End Users

<img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" width="30"> **Browse Events**
- Navigate to homepage
- View all available events

<img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" width="30"> **Register**
- Select your event
- Click "Register" button

<img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" width="30"> **Fill Form**
- Complete registration details
- Submit the form

<img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" width="30"> **Confirmation**
- Receive instant feedback
- Get success confirmation

</td>
<td width="50%">

### 👨‍💼 For Administrators

<img src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif" width="30"> **Login**
- Access `/admin/` endpoint
- Enter superuser credentials

<img src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif" width="30"> **Manage Registrations**
- View all registrations
- Approve/Reject/Pending status

<img src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif" width="30"> **Create Events**
- Navigate to Events section
- Add new events easily

<img src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif" width="30"> **Bulk Actions**
- Select multiple items
- Apply actions in bulk

</td>
</tr>
</table>

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 🗄️ Database Schema

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="100">
</div>

### 📊 Entity Relationship Diagram

```mermaid
erDiagram
    EVENT ||--o{ REGISTRATION : "has many"
    
    EVENT {
        int id PK "🔑 Primary Key"
        string event_name "📌 Event Name"
        text description "📝 Description"
        datetime date_and_time "📅 Date & Time"
        string location "📍 Location"
        int maximum_capacity "👥 Max Capacity"
    }
    
    REGISTRATION {
        int id PK "🔑 Primary Key"
        string user_name "👤 User Name"
        string email_address "📧 Email"
        string phone_number "📱 Phone"
        int selected_event FK "🔗 Event Reference"
        string registration_status "✅ Status"
        datetime timestamp "⏰ Created At"
    }
```

<details>
<summary><b>🗃️ View Model Details</b></summary>
<br>

### Event Model

```python
class Event(models.Model):
    event_name = CharField(max_length=200)
    description = TextField()
    date_and_time = DateTimeField()
    location = CharField(max_length=300)
    maximum_capacity = IntegerField()
```

### Registration Model

```python
class Registration(models.Model):
    user_name = CharField(max_length=100)
    email_address = EmailField()
    phone_number = CharField(max_length=15)
    selected_event = ForeignKey(Event)
    registration_status = CharField(
        choices=[
            ('pending', '⏳ Pending'), 
            ('approved', '✅ Approved'), 
            ('rejected', '❌ Rejected')
        ]
    )
    timestamp = DateTimeField(auto_now_add=True)
```

</details>

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 🎨 Tech Stack

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="100">
  
  <h3>🛠️ Technologies Used</h3>
</div>

<table align="center">
<tr>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="80"><br>
<sub><b>Backend</b></sub><br>
<img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="80"><br>
<sub><b>Frontend</b></sub><br>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=flat&logo=bootstrap&logoColor=white" />
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="80"><br>
<sub><b>Database</b></sub><br>
<img src="https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white" />
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2db.gif" width="80"><br>
<sub><b>Tools</b></sub><br>
<img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" />
</td>
</tr>
</table>

### 🔑 Key Technical Highlights

<div align="center">

| Feature | Description |
|---------|-------------|
| ⚡ **Class-Based Views** | ListView, CreateView for clean, reusable code |
| 🔒 **Authentication** | Django's robust security framework |
| 🎯 **Form Validation** | Comprehensive validation on both sides |
| 🔗 **Database Relations** | ForeignKey relationships for data integrity |
| 🎨 **Responsive UI** | Bootstrap 5 for mobile-first design |
| 🔄 **URL Resolution** | Using `reverse_lazy()` for proper redirects |

</div>

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 🌐 Deployment

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="100">
  
  <h3>☁️ Deploy Anywhere</h3>
</div>

<table align="center">
<tr>
<td align="center" width="25%">
<img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" alt="Heroku"><br>
<b>Heroku</b><br>
<sub>Easy deployment</sub>
</td>
<td align="center" width="25%">
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS"><br>
<b>AWS EC2</b><br>
<sub>Scalable cloud</sub>
</td>
<td align="center" width="25%">
<img src="https://img.shields.io/badge/DigitalOcean-0080FF?style=for-the-badge&logo=digitalocean&logoColor=white" alt="DigitalOcean"><br>
<b>DigitalOcean</b><br>
<sub>Simple setup</sub>
</td>
<td align="center" width="25%">
<img src="https://img.shields.io/badge/PythonAnywhere-1D9FD7?style=for-the-badge&logo=python&logoColor=white" alt="PythonAnywhere"><br>
<b>PythonAnywhere</b><br>
<sub>Free hosting</sub>
</td>
</tr>
</table>

### 📝 Pre-Deployment Checklist

- [x] Update `ALLOWED_HOSTS` in settings.py
- [x] Set `DEBUG = False` for production
- [x] Configure environment variables
- [x] Set up PostgreSQL database
- [x] Collect static files: `python manage.py collectstatic`
- [x] Set up SSL certificate

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 🤝 Contributing

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" width="100">
  
  <h3>💡 Contributions Welcome!</h3>
  <p>We love contributions! Help make this project even better.</p>
</div>

<details>
<summary><b>🚀 How to Contribute</b></summary>
<br>

### Step-by-Step Guide

1. **🍴 Fork the Project**
   ```bash
   Click the 'Fork' button at the top right
   ```

2. **📥 Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/EVENT-REGISTRATION-DJANGO-.git
   ```

3. **🌿 Create Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

4. **✨ Make Your Changes**
   ```bash
   # Add your awesome code
   git add .
   ```

5. **💾 Commit Changes**
   ```bash
   git commit -m '✨ Add some AmazingFeature'
   ```

6. **🚀 Push to Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

7. **🎉 Open Pull Request**
   ```bash
   Go to your fork on GitHub and click 'New Pull Request'
   ```

</details>

<br>

<div align="center">

### 💡 Contribution Ideas

| Category | Ideas |
|----------|-------|
| 🎨 **UI/UX** | Improve design, add animations, enhance responsiveness |
| 🐛 **Bug Fixes** | Fix issues, improve error handling, optimize performance |
| 📝 **Documentation** | Improve README, add tutorials, create guides |
| ✨ **Features** | Email notifications, payment integration, QR codes |
| 🔧 **Code Quality** | Refactoring, testing, code optimization |

</div>

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 📄 License

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="100">
  
  <h3>📜 MIT License</h3>
  <p>This project is open-source and free to use</p>
</div>

```
MIT License

Copyright (c) 2024 Koushik H Y

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

✨ Feel free to use this project for personal or commercial purposes ✨
```

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 👨‍💻 Author

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif" width="100">
  
  <h2>Koushik H Y</h2>
  <p><i>Full Stack Developer | Django Enthusiast | Open Source Contributor</i></p>
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=A855F7&center=true&vCenter=true&width=435&lines=Building+Scalable+Web+Applications;Passionate+About+Clean+Code;Always+Learning+New+Technologies" alt="Typing SVG" />
</div>

<br>

<div align="center">
  
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://koushik4475.netlify.app)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:koushik4475@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/koushik4475)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/koushik4475)

</div>

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 🌟 Show Your Support

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/216122065-2f028bae-25d6-4a3c-bc9f-175394ed5011.png" width="100">
  
  <h3>⭐ Star This Repository!</h3>
  <p>If you found this project helpful, please give it a star!</p>
  
  <a href="https://github.com/koushik4475/EVENT-REGISTRATION-DJANGO-/stargazers">
    <img src="https://img.shields.io/github/stars/koushik4475/EVENT-REGISTRATION-DJANGO-?style=social" alt="Stars">
  </a>
  <a href="https://github.com/koushik4475/EVENT-REGISTRATION-DJANGO-/network/members">
    <img src="https://img.shields.io/github/forks/koushik4475/EVENT-REGISTRATION-DJANGO-?style=social" alt="Forks">
  </a>
  <a href="https://github.com/koushik4475/EVENT-REGISTRATION-DJANGO-/issues">
    <img src="https://img.shields.io/github/issues/koushik4475/EVENT-REGISTRATION-DJANGO-?style=social" alt="Issues">
  </a>
  
  <br><br>
  
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="600">
</div>

<br>

### 📊 Project Stats

<div align="center">
  
![GitHub repo size](https://img.shields.io/github/repo-size/koushik4475/EVENT-REGISTRATION-DJANGO-?style=for-the-badge&color=blueviolet)
![GitHub language count](https://img.shields.io/github/languages/count/koushik4475/EVENT-REGISTRATION-DJANGO-?style=for-the-badge&color=brightgreen)
![GitHub top language](https://img.shields.io/github/languages/top/koushik4475/EVENT-REGISTRATION-DJANGO-?style=for-the-badge&color=blue)
![GitHub last commit](https://img.shields.io/github/last-commit/koushik4475/EVENT-REGISTRATION-DJANGO-?style=for-the-badge&color=red)

</div>

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

## 📬 Get In Touch

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/216122069-5b8169d7-1d8e-4a13-b245-a8e4176c99f8.png" width="100">
  
  <h3>💬 Questions or Feedback?</h3>
  <p>Feel free to reach out!</p>
  
  <table>
  <tr>
    <td align="center">
      <a href="https://github.com/koushik4475/EVENT-REGISTRATION-DJANGO-/issues">
        <img src="https://img.icons8.com/fluency/96/000000/bug.png" width="50"><br>
        <b>Report Issues</b>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/koushik4475/EVENT-REGISTRATION-DJANGO-/discussions">
        <img src="https://img.icons8.com/fluency/96/000000/comments.png" width="50"><br>
        <b>Discussions</b>
      </a>
    </td>
    <td align="center">
      <a href="mailto:koushik4475@gmail.com">
        <img src="https://img.icons8.com/fluency/96/000000/email-open.png" width="50"><br>
        <b>Email Me</b>
      </a>
    </td>
  </tr>
  </table>
</div>

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>

<br>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" width="100%">
  
  <h2>🎉 Thank You for Visiting! 🎉</h2>
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=A855F7&center=true&vCenter=true&width=435&lines=Made+with+%E2%9D%A4%EF%B8%8F+and+Django;Happy+Coding!+%F0%9F%9A%80;Star+%E2%AD%90+if+you+like+it!" alt="Typing SVG" />
  
  <br><br>
  
  <p>
    <img src="https://komarev.com/ghpvc/?username=koushik4475&label=Profile%20Views&color=blueviolet&style=for-the-badge" alt="Profile Views">
  </p>
  
  <br>
  
  **Built with ❤️ by Koushik H Y | © 2024 All Rights Reserved**
  
  <br>
  
  <a href="#top">
    <img src="https://img.shields.io/badge/Back%20to%20Top-000000?style=for-the-badge&logo=github&logoColor=white" alt="Back to Top">
  </a>
</div>
