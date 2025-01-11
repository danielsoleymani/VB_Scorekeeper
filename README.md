# VB_Scorekeeper

## Introduction

Welcome to **VB_Scorekeeper**, a powerful and user-friendly solution for tracking scores and events in real time. This application leverages modern web development technologies and integrates with the Twitter API for sharing updates directly to your audience.

---

## Features

- **Score Tracking**: Easily record and manage scores for different events or games.
- **Real-Time Updates**: Get instant feedback and maintain live scoreboards.
- **Twitter Integration**: Post game updates directly to Twitter to keep your followers informed.
- **Database Management**: Securely store and retrieve game data using MongoDB.
- **Cross-Platform Access**: Accessible via desktop and mobile browsers.

---

## Technologies Used

### Backend
- **Python**: Core programming language for server-side functionality.
- **MongoDB**: Database for storing game and score data.
- **Twitter API**: For posting live updates to Twitter.

### Frontend
- **HTML**: Structure and content of the web pages.
- **CSS**: Styling for an intuitive and responsive user interface.
- **JavaScript**: For dynamic and interactive functionality.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/scorekeeping-app.git
2. Navigate to the project directory:
   ```bash
   cd scorekeeping-app
3. Install required python packages:
   ```bash
   pip install flask pymongo tweepy
4. Set up your MongoDB database:
   - Create a new cluster
   - Add a collection titled 'users' to the cluster
   - Add a database titled 'userDB' to the collection
   - Configure your connection string
   - Update the .env file with your database URI.
5. Set up Twitter API credentials:
   - Create a Twitter Developer account and obtain API keys.
   - Update the .env file with your Twitter API credentials.
6. Run the application:
   ```bash
   python SignIn.py
7. Open the app in your browser using the local host:
   - http://127.0.0.1:5000

##Contributing 
Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Commit your changes
4. Push to your branch
5. Submit a pull request


 




