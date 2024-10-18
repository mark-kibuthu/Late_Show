# Late Show API

## Overview
This API allows users to manage episodes, guests, and their appearances on a fictional late-night show.

## Endpoints
### GET /episodes
Returns a list of episodes.

### GET /episodes/:id
Returns details of a specific episode, including its appearances.

### GET /guests
Returns a list of guests.

### POST /appearances
Creates a new appearance associated with an episode and a guest.

## Installation

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite (or any other database of your choice)

### Steps to Install

1. Clone the repository:

2. Create a virtual environment:

 ##  bash

- python -m venv venv

3. Activate the virtual environment:

 - On Windows:

    ## bash

venv\Scripts\activate

 -  On macOS/Linux:

## bash

source venv/bin/activate 


4. Activate the virtual environment:

    - On Windows:

   ## bash

venv\Scripts\activate

   - On macOS/Linux:

## bash

source venv/bin/activate

5. Install the required packages:

 ## bash

pip install Flask Flask-SQLAlchemy


6. Set up the database:

## bash

python seed.py


Configuration

You can configure the database URI and other settings in your app.py file:

python

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


Usage

To start the Flask application, run:

bash

python app.py

The application will be accessible at http://localhost:5555.