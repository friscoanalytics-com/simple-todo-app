# Simple Todo App - Local Setup Instructions

## Prerequisites

- **Node.js** (Latest LTS version)
- **Yarn** (for frontend)
- **Python 3.9+** (for backend)
- **MySQL Server** (for the database)
- **Docker** (optional, if running with containers)

---

## Backend Setup (FastAPI)

1. **Navigate to the backend directory:**
   ```bash
   cd todo-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables:**
   ```bash
   export SQL_USERNAME=<SQL_USERNAME>
   export SQL_PASSWORD=<SQL_PASSWORD>
   export SQL_DBNAME=<SQL_DBNAME>
   export SQL_SERVER=<SQL_SERVER>
   ```

5. **Run the backend server:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

---

## Frontend Setup (React)

1. **Navigate to the frontend directory:**
   ```bash
   cd todo-portal
   ```

2. **Install dependencies:**
   ```bash
   yarn install
   ```

3. **Set environment variable:**
   - Create a `.env` file with the following content:
     ```
     REACT_APP_API_URL=http://localhost:8000/todos
     ```

4. **Run the frontend application:**
   ```bash
   yarn start
   ```

---

## Docker Setup (Optional)

1. **Build Docker images:**
   ```bash
   docker build -t todo-backend todo-api/
   docker build -t todo-frontend todo-portal/
   ```

2. **Run Docker containers:**
   ```bash
   docker run -d --name todo-backend -p 8000:8000 \
     -e SQL_USERNAME=<SQL_USERNAME> \
     -e SQL_PASSWORD=<SQL_PASSWORD> \
     -e SQL_DBNAME=<SQL_DBNAME> \
     -e SQL_SERVER=<SQL_SERVER|host.docker.internal:3306> \
     todo-backend

   docker run -d --name todo-frontend -p 3000:3000 \
     -e REACT_APP_API_URL=http://localhost:8000/todos \
     todo-frontend
   ```

---

## Access the Application

- **Frontend:** [http://localhost:3000](http://localhost:3000)
- **Backend API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

---