# AI Code Optimization Tool

An intelligent web application that leverages OpenAI GPT-4.1 to analyze, optimize, and refactor code in Python, JavaScript, Java, and C++.  
Get instant, professional code review suggestions and improved code versions to help you write cleaner, more efficient, and maintainable code.

---

## Features

- **AI-Powered Code Optimization**: Supports Python, JavaScript, Java, and C++.
- **Detailed Analysis & Suggestions**: Explains code issues, offers actionable improvements, and summarizes changes.
- **One-Click Code Refactoring**: Instantly generates optimized code with best practices.
- **History Tracking**: View, manage, and revisit all your past code optimizations.
- **Modern UI/UX**: Responsive, intuitive interface built with React and Material-UI.
- **Secure Authentication**: JWT-based user login and session management.

---

## Tech Stack

- **Frontend**: React.js, Material-UI, Axios, JWT
- **Backend**: Python, Flask, SQLAlchemy, PostgreSQL, OpenAI GPT API, JWT

---

## Getting Started

### Prerequisites

- Node.js (v18+)
- Python (v3.9+)
- PostgreSQL (v12+)
- OpenAI API Key

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/xuliugame/AI-Code-Improvement-Tool.git
    cd AI-Code-Improvement-Tool
    ```

2. **Set up PostgreSQL**
    - Create a new database and note the connection details.

3. **Backend Setup**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
    - Create a `.env` file in `backend/`:
      ```
      OPENAI_API_KEY=your_openai_api_key
      JWT_SECRET_KEY=your_jwt_secret
      DATABASE_URL=postgresql://user:password@host:5432/dbname
      ```

4. **Frontend Setup**
    ```bash
    cd ../frontend
    npm install
    ```

### Running the Application

- **Start Backend**
    ```bash
    cd backend
    python app.py
    ```
- **Start Frontend**
    ```bash
    cd frontend
    npm start
    ```
- Visit [http://localhost:3000](http://localhost:3000)

---

## Usage

1. Register or log in.
2. Paste your code and select the language.
3. Click **Generate Suggestions**.
4. Review the AI's analysis, suggestions, and optimized code.
5. Copy, use, or save your improved code.
6. Browse your optimization history at any time.

---

## API Endpoints

- `POST /register` — Register a new user
- `POST /login` — User login
- `POST /optimize` — Submit code for AI optimization
- `GET /history` — Retrieve optimization history
- `DELETE /history/<id>` — Delete a history entry

---

## Project Structure

```
AiCodeTools/
├── backend/
│   ├── api/                  # API endpoints and OpenAI integration
│   │   ├── openai_api.py     # Handles code optimization requests via OpenAI
│   │   └── _init_.py         # API package initializer
│   ├── user/                 # User management and authentication
│   │   ├── models.py         # Database models (User, CodeHistory, etc.)
│   │   ├── manage.py         # User management utilities
│   │   ├── history.py        # Code optimization history logic
│   │   ├── __init__.py       # User package initializer
│   │   └── user.py           # User authentication routes
│   ├── tests/                # Backend test suite
│   ├── app.py                # Main Flask application
│   ├── config.py             # Configuration settings
│   ├── requirements.txt      # Python dependencies
│   ├── app.db                # SQLite database (for development/testing)
│   └── instance/             # Flask instance folder (runtime files)
├── frontend/
│   ├── src/
│   │   ├── components/       # Reusable React components
│   │   │   ├── CodeInput.js      # Code input editor
│   │   │   ├── History.js        # Optimization history panel
│   │   │   ├── NavBar.js         # Top navigation bar
│   │   │   └── Suggestions.js    # AI suggestions and optimized code display
│   │   ├── contexts/         # React context providers
│   │   │   └── AuthContext.js    # Authentication context
│   │   ├── pages/            # Page-level React components
│   │   │   ├── Login.js          # Login page
│   │   │   └── MainPage.js       # Main application page
│   │   ├── services/         # API service utilities
│   │   │   └── api.js            # API call abstraction
│   │   ├── App.js            # Root React component
│   │   ├── index.js          # React entry point
│   │   └── styles.css        # Global styles
│   └── package.json          # Frontend dependencies
├── .gitignore                # Git ignore rules
├── README.md                 # Project documentation
└── package-lock.json         # Node.js lockfile
```

---

## Testing

- **Backend**:  
  Run tests with:
  ```bash
  cd backend
  pytest
  ```
- **Frontend**:  
  Run tests with:
  ```bash
  cd frontend
  npm test
  ```

---

## Environment Variables

- **Backend**:
  - `OPENAI_API_KEY`
  - `DATABASE_URL`
  - `JWT_SECRET_KEY`
- **Frontend**:
  - `REACT_APP_API_URL` (defaults to http://127.0.0.1:5000)

---

## License

All rights reserved. This project is the intellectual property of the author. No part of this project may be reproduced, distributed, or transmitted in any form or by any means without the prior written permission of the author.

---

## Acknowledgments

- [OpenAI](https://openai.com/) for the GPT API
- [Material-UI](https://mui.com/) for UI components
- [Flask](https://flask.palletsprojects.com/) for the backend framework

## Development Workflow

1. **Backend Development**:
   - The backend uses Flask with SQLAlchemy for database operations
   - API endpoints are defined in the `api/` directory
   - User authentication is handled through JWT tokens

2. **Frontend Development**:
   - The frontend is built with React and Material-UI
   - API calls are made using Axios
   - State management is handled through React Context
   - Routing is managed with React Router

3. **Testing**:
   - Backend tests can be run with:
     ```bash
     cd backend
     pytest
     ```
   

4. **Environment Variables**:
   - Backend requires:
     - `OPENAI_API_KEY`: Your OpenAI API key
     - `DATABASE_URL`: PostgreSQL connection string
     - `JWT_SECRET_KEY`: Secret key for JWT token generation
   - Frontend requires:
     - `REACT_APP_API_URL`: Backend API URL (defaults to http://127.0.0.1:5000)








