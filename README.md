# PY-FULLWEBSITE-EXAMPLE

## Overview

This project demonstrates the integration between frontend and backend components using FastAPI and MongoDB. It allows users to perform CRUD operations on a simple database.

## Features

- **Local Development:** The code runs smoothly locally on a laptop.
- **Backend:** FastAPI is used to create the backend server.
- **Database:** MongoDB is used as the database for storing and retrieving data.
- **Frontend Integration:** The frontend interacts with the backend API to perform CRUD operations.
- **GitHub Pages:** While the project is designed to work on GitHub Pages, there are some issues currently being addressed.
- **GitHub Workspace:** The project is actively being developed and improved in a GitHub workspace environment using Codespaces.
- **Workspace Status:** Currently, the project is encountering issues in the Codespace environment, and efforts are underway to resolve these issues.

## Usage

1. Clone the repository to your local machine.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the FastAPI server using `uvicorn main:app --reload`.
4. Access the application locally in a web browser at `http://localhost:8000`.
5. Interact with the frontend to test CRUD operations.
6. Report any issues or bugs encountered during usage.

## Modules Used

- **dotenv:** Used for loading environment variables from a .env file.
- **pymongo:** MongoDB driver for Python, used for interacting with MongoDB.
- **fastapi:** A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **pydantic:** Data validation and settings management using Python type annotations.
- **bson:** Binary JSON encoding format used by MongoDB.

## Routes for CRUD App

- **GET /items:** Retrieve all items from the database.
- **GET /items/{id}:** Retrieve a specific item by ID.
- **POST /items:** Create a new item.
- **PUT /items/{id}:** Update an existing item by ID.
- **DELETE /items/{id}:** Delete an item by ID.

## Work in Progress (WIP)

- **PUT Method:** Currently implementing the PUT method to update existing items in the database.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for any improvements or bug fixes.

## Conclusion

GitHub Pages itself is a static site hosting service and does not support server-side processing or dynamic content generation, including handling POST requests. 
Therefore, you cannot directly use POST methods with GitHub Pages alone.
