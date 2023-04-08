# 📝 Todo RESTful API

This is a RESTful API for managing tasks, built with FastAPI and Python. The project uses Firebase, MongoDB, and PostgreSQL to store tasks.

## 🚀 Quick Start

1. Clone this repository.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Create a `.env` file with your Firebase credentials, MongoDB URI, and PostgreSQL URI. Example:

    ```
    FIREBASE_API_KEY=your-api-key
    FIREBASE_AUTH_DOMAIN=your-auth-domain
    FIREBASE_PROJECT_ID=your-project-id
    MONGO_URI=mongodb://localhost:27017/todo
    POSTGRES_URI=postgresql://user:password@localhost:5432/todo
    ```

4. Start the server with `uvicorn app.main:app --reload`.
5. Open your browser and go to `http://localhost:8000/docs` to access the API documentation.

## 🛠️ Technologies

- [FastAPI](https://fastapi.tiangolo.com/): a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- [Python](https://www.python.org/): a high-level programming language for general-purpose programming.
- [Firebase](https://firebase.google.com/): a mobile and web application development platform developed by Firebase, Inc. in 2011, then acquired by Google in 2014.
- [MongoDB](https://www.mongodb.com/): a general purpose, document-based, distributed database built for modern application developers and for the cloud era.
- [PostgreSQL](https://www.postgresql.org/): a powerful, open source object-relational database system.

## 📄 API Documentation

You can find the API documentation in the Swagger UI by accessing the following URL: `http://localhost:8000/docs`.

## 👨‍💻 Development

To contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch with your changes: `git checkout -b my-feature`.
3. Commit your changes: `git commit -m 'feat: add new feature'`.
4. Push to the branch: `git push origin my-feature`.
5. Create a pull request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
