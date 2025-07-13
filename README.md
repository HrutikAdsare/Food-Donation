# 🍎 Food Donation Web App

**Food-Donation** is a PHP-based web application designed to connect food donors with volunteers and organizations, streamline donation submissions, and manage delivery status updates.

## 🌍 Features

- 📝 **User Registration & Authentication**

  - Secure signup and login system for donors and volunteers.
  - Passwords hashed and sessions managed via PHP.

- 🍽️ **Donate Food**

  - Donors can fill out donation forms (`donate.php`) to submit food availability details.
  - File uploads (e.g., images) supported for better clarity.

- 🤝 **Volunteer Registration**

  - Volunteers register (`volunteer_registration.php`) to participate in pickups and deliveries.

- 📦 **Donation Management**

  - View pending donations (`index.php`) and volunteer assignment.
  - Update delivery status (`update_delivery_status.php`) as donations are collected and delivered.

- 📑 **Additional Pages**

  - **About** (`about.php`) – App overview and contact info.
  - **Get Involved** (`get_involved.php`) – How organizations and volunteers can join.

- 🔒 **Session Handling & Security**

  - Secure logout (`logout.php`) and session checks on protected pages.
  - Database interactions via prepared statements to prevent SQL injection.

---

## 🧠 Tech Stack

| Area         | Tech               |
| ------------ | ------------------ |
| Backend      | PHP, MySQL         |
| Frontend     | HTML, CSS          |
| Dependencies | Composer (vendor/) |

---

## 📁 Folder Structure

```
Food-Donation/
├── vendor/                     # Composer dependencies
├── images/                     # App images (e.g., Home.png, i1.png)
├── about.php                   # About page
├── auth.php                    # Authentication logic
├── db_connect.php              # Database connection settings
├── donate.php                  # Donation submission form
├── donation_submission.php     # Donation processing script
├── get_involved.php            # Info for organizations/volunteers
├── index.php                   # Dashboard / listing of donations
├── login.php                   # Login form
├── logout.php                  # Logout script
├── signup.php                  # Registration form
├── update_delivery_status.php  # Script to update status
├── volunteer_registration.php  # Volunteer signup form
├── s.css                       # Main stylesheet
└── README.md                   # This file
```

---

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   ```

git clone [https://github.com/HrutikAdsare/Food-Donation.git](https://github.com/HrutikAdsare/Food-Donation.git) cd Food-Donation

````

2. **Install Dependencies**
   ```bash
composer install
````

3. **Configure Database**

   - Create a MySQL database (e.g., `food_donation`).
   - Import `schema.sql` if provided or run:
     ```sql
     CREATE TABLE users (...);
     CREATE TABLE donations (...);
     -- and other tables
     ```
   - Update database credentials in `db_connect.php`.

4. **Run the App**

   - Serve via built-in PHP server:
     ```bash
     ```

php -S localhost:8000

```
   - Open `http://localhost:8000/index.php` in your browser.

5. **Use the App**
   - Sign up as a donor or volunteer.
   - Submit or manage donations.

---

## 👨‍💻 Developer

Built with ❤️ by [Hrutik Adsare](https://huggingface.co/Hrutik-Adsare)

```
