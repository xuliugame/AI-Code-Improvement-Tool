# AI Code Optimization Tool

An intelligent code optimization tool that leverages AI to analyze and improve your code. This application provides suggestions for code optimization and generates optimized versions of your code.

## Features

-  Instant code optimization suggestions
-  Smart code analysis
- Code history tracking
- Clean and modern UI
- Secure user authentication
-  History management

## Tech Stack

### Frontend
- React.js
- Material-UI
- Axios for API calls
- JWT for authentication

### Backend
- Python
- Flask
- PostgreSQL
- OpenAI GPT API
- SQLAlchemy
- JWT Authentication

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.9 or higher)
- PostgreSQL (v12 or higher)
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/xuliugame/AI-Code-Improvement-Tool.git
cd AI-Code-Improvement-Tool
```

2. Set up PostgreSQL:
- Create a new PostgreSQL database
- Note down your database connection details (host, database name, user, password)

3. Set up the backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file in the backend directory with:
```
OPENAI_API_KEY=your_openai_api_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

5. Set up the frontend:
```bash
cd ../frontend
npm install
```

### Running the Application

1. Start the backend server:
```bash
cd backend
python app.py
```

2. Start the frontend development server:
```bash
cd frontend
npm start
```

3. Access the application at `http://localhost:3000`

## Usage

1. Register/Login to your account
2. Enter your code in the input box
3. Select the programming language
4. Click "Generate Suggestions" to get optimization recommendations
5. View the optimized code and suggestions
6. Access your optimization history in the history panel

## Features in Detail

### Code Optimization
- Analyzes code structure and patterns
- Provides specific optimization suggestions
- Generates optimized code versions
- Supports multiple programming languages

### User Authentication
- Secure JWT-based authentication
- Protected API endpoints
- User session management

### History Management
- Saves all optimization attempts
- View past optimizations
- Delete history entries
- Timestamp tracking

### Modern UI/UX
- Responsive design
- Intuitive interface
- Real-time feedback
- Clean and professional look

## API Endpoints

### Authentication
- POST `/register` - User registration
- POST `/login` - User login
- GET `/profile` - Get user profile

### Code Optimization
- POST `/optimize` - Submit code for optimization
- GET `/history` - Get optimization history
- DELETE `/history/<id>` - Delete history entry





## Acknowledgments

- OpenAI for providing the GPT API
- Material-UI for the component library
- Flask community for the excellent web framework

## Project Structure

```
AiCodeTools/
├── backend/
│   ├── api/               # API endpoints and business logic
│   │   └── openai_api.py  # OpenAI API integration
│   ├── user/              # User management and authentication
│   │   ├── models.py      # Database models
│   │   └── user.py        # User authentication routes
│   ├── tests/             # Backend test suite
│   ├── app.py            # Main Flask application
│   ├── config.py         # Configuration settings
│   ├── init_db.py        # Database initialization script
│   ├── requirements.txt  # Python dependencies
│   └── .env             # Environment variables
├── frontend/
│   ├── src/
│   │   ├── components/   # Reusable components
│   │   │   ├── CodeInput.js    # Code input component
│   │   │   ├── History.js      # History display component
│   │   │   ├── NavBar.js       # Navigation bar component
│   │   │   └── Suggestions.js  # Suggestions display component
│   │   ├── contexts/     # React contexts
│   │   │   └── AuthContext.js  # Authentication context
│   │   ├── pages/        # Page components
│   │   │   ├── Login.js        # Login page
│   │   │   └── MainPage.js     # Main application page
│   │   ├── services/     # API services
│   │   │   └── api.js          # API integration
│   │   ├── App.js        # Root component
│   │   ├── index.js      # Application entry point
│   │   └── styles.css    # Global styles
│   ├── public/           # Static assets
│   └── package.json      # Node.js dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## Development Workflow

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








