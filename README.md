# Explore Kenya Web Application
 Explore Kenya is a Flask-based web application designed to assist tourists and visitors in exploring Kenya's breathtaking scenic attractions. 
 The platform provides users with a seamless experience to discover, book, and plan visits to various destinations across the country.


## Features

 ### a. User Authentication
   1. User registration with email and password verification
   2. Secure user login/logout functionality 

 ### b. Destination Exploration
   1. Browse through various scenic locations in Kenya
   2. View details, images, and descriptions of popular attractions.
   3. Search functionality to quickly find destinations

 ### c. Booking System
   1. Book visits to desired destinations
   2. View available slots and check for fully booked locations
   3. Get instant booking confirmation and updates

 ### d. Flash Messaging System
   1. Notify users about available and booked-out destinations
   2. Provide real-time feedback on booking success or failure

## Technologies Used 

| Component           | Technology                                     |
|---------------------|------------------------------------------------|
| Backend             | Flask (Python)                                 | 
| Database            | SQLite (can be extended to PostgreSQL/MySQL)   |                 
| Frontend            | HTML, CSS, Javascript, Mako                    |
| Templating Engine   | Jinja2                                         |
| Styling             | Bootstrap & custom CSS for enhanced styling    |


## Installation Guide

 ### Prerequisites
  Ensure you have the following installed on your system:
  1. Python 3.x
  2. SQLite (comes pre-installesd with python)
  3. Git (for cloning repository)


 ### Setup and Installation

 1. Clone the repository

 ```sh
  git clone https://github.com/harizonelopez/Explore--kenya.git
  cd Explore--kenya
 ```

 2. Create a virtual environment and activate it:

 ```sh
  python -m venv venv
  source venv/Scripts/activate   # On Mac use `source venv/bin/activate`
 ```

 3. Install the required packages or the dependencies:
 ```sh
  pip install -r requirements.txt
 ```
 4. Set Up the Database
 ```sh
  flask db init  # Initialize the database
  flask db migrate -m "Initial migration"   
  flask db upgrade   # Apply migrations to the database
 ```

## Run the application:
 To start the application, use the following command:
 ```sh
  python app.py
 ```

## Access the application in your web browser:
 
 Open your web browser and go to:
 ```sh
  `http://127.0.0.1:5000`
 ```

## API Endpoints

| Endpoint      | Method    | Description                |
|-------------- |-----------|----------------------------|
| /             | GET       | Homepage                   |
| /signup       | POST      | User registration          |                
| /login        | POST      | User login                 |
| /logout       | GET       | User logout                |
| /destinations | GET       | View all destinations      |
| /booking      | POST      | Book a destination         | 
| /search       | GET       | Search foe destinations    |
| /reset        | POST      | Reset user password        |


## Future Enhancements
   - Add a payment gateway for online booking payments
   - Implement Google Maps API for interactive destination mapping
   - Develop a review and rating system for users to share experiences
   - Improve UI/UX design for better navigation and usability


## License
 This project is licensed under the MIT License and adhered to the rules and regulations provided under the law.


## Contributors
   - <a>Harizone Lopez</a> - Main Developer
   - Contributions are welcome! Feel free to fork and submit pull requests.


## Support
 For any issues, feel free to open an issue or contact us at 
  `support@explorekenya.com.`



  <i>Happy Exploring! 🌍✈️</i>