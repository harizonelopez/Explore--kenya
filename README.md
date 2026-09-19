# Explore Kenya Web App

Explore Kenya is a Flask-based web application designed to assist tourists and visitors in exploring Kenya's breathtaking scenic attractions.

The platform provides users with a seamless experience to discover, book, and plan visits to various destinations across the country.

## Features

### a. User Authentication

1. User registration with email and password verification
2. Secure user login/logout functionality

### b. Destination Exploration

1. Browse through various scenic locations in Kenya
2. View details, images, and descriptions of popular attractions
3. Search functionality to quickly find destinations

### c. Booking System

1. Book visits to desired destinations
2. View available slots and check for fully booked locations
3. Get instant booking confirmation and updates

### d. Flash Messaging System

1. Notify users about available and booked-out destinations
2. Provide real-time feedback on booking success or failure

## Technologies Used

| Component         | Technology                                   |
| ----------------- | -------------------------------------------- |
| Backend           | Flask (Python)                               |
| Database          | SQLite (can be extended to PostgreSQL/MySQL) |
| Frontend          | HTML, CSS, JavaScript, Mako                  |
| Templating Engine | Jinja2                                       |
| Styling           | Bootstrap & custom CSS                       |

## Installation Guide

### Prerequisites

Ensure you have the following installed on your system:

1. **Python 3.11.x**
2. **SQLite** (included with Python)
3. **Git** (for cloning the repository)

> **Note:** The current project dependencies are pinned to versions compatible with the existing Flask application. Python 3.11 is recommended for this version of the project. Python 3.14 may cause compatibility issues with the current dependency stack.

### Setup and Installation

#### 1. Clone the repository

```sh
git clone https://github.com/harizonelopez/Explore--kenya.git
cd Explore--kenya
```

#### 2. Create a virtual environment

Using Python 3.11:

```sh
py -3.11 -m venv .env
```

#### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.env\Scripts\Activate
```

**Windows Command Prompt:**

```cmd
.env\Scripts\activate
```

**macOS/Linux:**

```sh
source .env/bin/activate
```

> If PowerShell prevents script execution, run the following command once for your Windows user account:
>
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

#### 4. Install dependencies

```sh
python -m pip install -r requirements.txt
```

### Dependency Compatibility

The current project uses the following dependency versions:

```text
Flask==2.2.5
Flask-SQLAlchemy==2.5.1
Flask-Login==0.6.3
Flask-Migrate==3.1.0
Flask-Mail==0.9.1
Werkzeug==2.2.3
SQLAlchemy==1.4.49
email-validator==1.3.1
python-dotenv==1.0.0
Jinja2==3.1.2
itsdangerous==2.1.2
gunicorn==21.2.0
```

These versions should be installed from `requirements.txt` to maintain compatibility with the current application.

### 5. Set Up the Database

Initialize the database migration system:

```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Run the Application

To start the application:

```sh
python app.py
```

Alternatively, if Flask is configured correctly:

```sh
flask run
```

## Access the Application

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Endpoint        | Method | Description              |
| --------------- | ------ | ------------------------ |
| `/`             | GET    | Homepage                 |
| `/signup`       | POST   | User registration        |
| `/login`        | POST   | User login               |
| `/logout`       | GET    | User logout              |
| `/destinations` | GET    | View all destinations    |
| `/booking`      | POST   | Book a destination       |
| `/search`       | GET    | Search for destinations  |
| `/reset`        | POST   | Reset user password      |
| `/contact`      | POST   | Reach out/send a message |

## Future Enhancements

* Add a payment gateway for online booking payments
* Implement Google Maps API for interactive destination mapping
* Develop a review and rating system for users to share their experiences
* Improve UI/UX design for better navigation and usability

## License

This project is licensed under the MIT License and adheres to the applicable rules and regulations.

## Contributors

* **Harizone Lopez** — Main Developer
* Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Support

For any issues, please open an issue in the repository or contact:

`support@explorekenya.com`

<i>Happy Exploring! 🌍✈️</i>
