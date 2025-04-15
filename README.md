# AiCodeTools

AiCodeTools is a modern web application that provides AI-powered code assistance and analysis tools. The project features a React-based frontend and a Flask-based backend, offering a seamless user experience for developers.

## Features

- **User Authentication**: Secure login and registration system with JWT token-based authentication
- **AI Code Analysis**: Integration with OpenAI API for code analysis and suggestions
- **Modern UI**: Responsive and user-friendly interface built with React
- **RESTful API**: Well-structured backend API with proper error handling
- **Database Integration**: SQLAlchemy-based database for user management and data persistence

## Project Structure

```
AiCodeTools/
├── .github/
│   └── workflows/          # GitHub Actions CI/CD configuration
├── backend/
│   ├── api/               # API endpoints and business logic
│   │   └── openai_api.py  # OpenAI API integration and endpoints
│   ├── user/              # User management and authentication
│   │   ├── models.py      # Database models
│   │   └── user.py        # User-related routes and controllers
│   ├── tests/             # Backend test suite
│   ├── app.py            # Main Flask application
│   ├── config.py         # Configuration management
│   ├── requirements.txt  # Python dependencies
│   └── .env             # Environment variables
├── frontend/
│   ├── src/              # React source code
│   │   ├── App.js       # Main application component
│   │   ├── contexts/    # React context providers
│   │   ├── pages/       # Page components
│   │   │   ├── Login.js # Authentication page
│   │   │   └── MainPage.js # Main dashboard
│   │   ├── components/  # Reusable UI components
│   │   ├── services/    # API service functions
│   │   └── utils/       # Utility functions
│   ├── public/          # Static assets
│   └── package.json     # Node.js dependencies
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Node.js (v14 or higher)
- Python (v3.8 or higher)
- PostgreSQL (v12 or higher)
- OpenAI API key

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/AiCodeTools.git
cd AiCodeTools
```

2. **Set up the backend**:
```bash
cd backend

# Create and activate virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Create .env file with the following content:
# OPENAI_API_KEY=your_openai_api_key
# DATABASE_URL=postgresql://username:password@localhost:5432/dbname
# JWT_SECRET_KEY=your_jwt_secret_key
```

3. **Set up the database**:
```bash
# Start PostgreSQL service
# On Windows:
net start postgresql
# On macOS/Linux:
sudo service postgresql start

# Create database
createdb aicode_db

# Initialize database tables
flask db upgrade
```

4. **Set up the frontend**:
```bash
cd frontend
npm install
```

### Running the Application

1. **Start the backend server**:
```bash
cd backend
# Activate virtual environment if not already activated
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Start Flask server
flask run
```
The backend server will be available at `http://127.0.0.1:5000`

2. **Start the frontend development server**:
```bash
cd frontend
npm start
```
The frontend will automatically open in your default browser at `http://localhost:3000`

### Development Workflow

1. **Backend Development**:
   - The backend uses Flask with SQLAlchemy for database operations
   - API endpoints are defined in the `api/` directory
   - User authentication is handled through JWT tokens
   - Database migrations are managed using Flask-Migrate

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
   - Frontend tests can be run with:
     ```bash
     cd frontend
     npm test
     ```

4. **Environment Variables**:
   - Backend requires:
     - `OPENAI_API_KEY`: Your OpenAI API key
     - `DATABASE_URL`: PostgreSQL connection string
     - `JWT_SECRET_KEY`: Secret key for JWT token generation
   - Frontend requires:
     - `REACT_APP_API_URL`: Backend API URL (defaults to http://127.0.0.1:5000)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request








