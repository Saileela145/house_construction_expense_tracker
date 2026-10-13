# 🏠 HC Expense Tracker
### House Construction Expense Management System

A web-based application built to simplify house construction expense management. HC Expense Tracker helps individual home builders record material purchases, track labour costs, monitor payments, and manage outstanding balances through a centralized dashboard.

The application uses **Streamlit, FastAPI, and PostgreSQL** to provide an organized approach to tracking construction expenses from material purchases to other site-related costs.

---

## 📌 Project Overview

Managing house construction expenses manually can make it difficult to track purchases, payments, and pending balances.

HC Expense Tracker provides a centralized platform to record construction-related expenses, organize purchase history, and monitor spending across different categories.

### 🎯 Project Objectives

- Centralize house construction expense records.
- Track material purchases and labour expenses.
- Monitor payments and outstanding balances.
- Organize expenses by category and construction activity.
- Provide a clear overview of construction spending.

---

## ✨ Key Features

### 📊 Expense Dashboard
- View construction expense information in one place.
- Monitor total spending and payment-related information.
- Review expense summaries and category-wise breakdowns.
- Analyze construction expenses through visualizations.

### 🧱 Construction Material Tracking

| Category | Tracking Information |
|---|---|
| Cement | Quantity, purchase cost, and payment details |
| Steel | Material quantities, sizes, and expenses |
| Bricks | Quantity by block size and purchase cost |
| Sand | Sand type, quantity, and purchase cost |
| Stone | Material quantities and expenses |

### 👷 Labour and Service Expenses

Track expenses associated with construction activities, including:

- Labour payments
- Electrical work
- Plumbing work
- Painting work

### 💰 Payment and Expense Management
- Record construction purchases and expenses.
- Maintain purchase history.
- Track payments and outstanding amounts where supported.
- Organize records by expense category.

### 📈 Expense Analysis
- Review construction spending across different categories.
- Monitor material and service expenses.
- Use dashboard metrics to understand expenditure patterns.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| Programming Language | Python |
| Database | PostgreSQL |
| Database ORM | SQLAlchemy |
| Data Processing | Pandas, NumPy |
| API Communication | REST APIs, Requests |
| Database Hosting | Neon PostgreSQL |
| Dependency Management | uv |
| Version Control | Git, GitHub |

---

## 🏗️ System Architecture

```text
              User
               |
               v
      Streamlit Frontend
               |
               v
       REST API Requests
               |
               v
        FastAPI Backend
               |
               v
       SQLAlchemy ORM
               |
               v
       PostgreSQL Database
          (Neon Cloud)
```

### How It Works

1. The user interacts with the Streamlit frontend.
2. The frontend sends requests to the FastAPI backend.
3. The backend processes requests and performs database operations.
4. SQLAlchemy manages interactions with PostgreSQL.
5. The application returns the relevant information to the frontend for display.

---

## 📂 Project Structure

```text
HC_Tracker/
│
├── backend/
│   ├── core/                 # Security and application configuration
│   ├── database/             # Database connection and sessions
│   ├── models/               # SQLAlchemy database models
│   ├── repositories/         # Data access operations
│   ├── routers/              # FastAPI API endpoints
│   ├── schemas/              # Request and response schemas
│   ├── services/             # Business logic
│   ├── utils/                # Backend utilities
│   ├── create_user.py        # Admin user creation and update
│   └── main.py               # FastAPI entry point
│
├── frontend/
│   ├── assets/               # CSS and styling
│   ├── components/           # Reusable UI components
│   ├── page_layouts/         # Application pages
│   ├── services/             # API client
│   ├── utils/                # Frontend utilities
│   ├── requirements.txt      # Frontend dependencies
│   └── app.py                # Streamlit entry point
│
├── sample/                   # Sample data files
├── scripts/                  # Utility scripts
├── .env.example              # Example environment configuration
├── .gitignore
├── pyproject.toml            # Project configuration
└── README.md
```

---

## ⚙️ Installation and Setup

### Prerequisites

Install the following:

- Python
- uv
- Git
- Access to a configured PostgreSQL database

### 1. Clone the Repository

```bash
git clone https://github.com/Saileela145/house_construction_expense_tracker.git
```

Navigate to the project directory:

```bash
cd house_construction_expense_tracker
```

### 2. Configure Environment Variables

Create a `.env` file in the project root using `.env.example` as a reference.

Configure the environment variables required by your application, including the database connection and authentication settings.

For example:

```env
DATABASE_URL=your_postgresql_connection_string
SECRET_KEY=your_secure_secret_key
ADMIN_USERNAME=your_admin_username
ADMIN_EMAIL=your_admin_email
ADMIN_PASSWORD=your_admin_password
```

Replace the example values with your actual configuration.

**Security:** Never upload your real `.env` file, database credentials, passwords, or secret keys to GitHub.

### 3. Install Dependencies

From the project root, run:

```bash
uv sync
```

Install the frontend dependencies if they are not already available in the environment:

```bash
uv pip install -r frontend/requirements.txt
```

### 4. Start the Backend

Open a terminal in the project root and run:

```bash
uv run --directory backend uvicorn main:app --reload
```

The backend should be available at:

```text
http://127.0.0.1:8000
```

Explore the API documentation at:

```text
http://127.0.0.1:8000/docs
```

### 5. Start the Frontend

Open another terminal in the project root and run:

```bash
uv run streamlit run frontend/app.py
```

Open the local URL displayed in the terminal to access the application.

---

## 🔐 Security

- Database credentials are configured through environment variables.
- The `.env` file is excluded from version control.
- Authentication and password handling are implemented in the application.
- Administrative credentials should be kept private.
- Production deployment should use secure configuration and a strong application secret key.

---

## 🚀 Future Enhancements

Potential improvements include:

- Downloadable expense reports.
- Budget planning and budget-versus-actual comparisons.
- Advanced expense analytics and visualizations.
- Improved mobile-friendly layouts.
- Cloud deployment for remote access.

---
## 🔐 Admin Login Credentials

| Field | Value |
|---|---|
| Username | `Leela314` |
| Email | `Leela@project.com` |
| Password | `Leela_14` |
| Role | Admin |

## 👩‍💻 Author

**Saileela**

B.Tech Computer Science Engineering

GitHub: [Saileela145](https://github.com/Saileela145)

---

## 📄 License

This project is maintained as a private project. All rights reserved.
