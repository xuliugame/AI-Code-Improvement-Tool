# AI Code Improvement Tool

This project is a **web application** that allows users to submit code snippets and receive optimization suggestions using **OpenAI's GPT-4o**. The system consists of a **React frontend** and a **Flask backend**, deployed on **GitHub Pages** for frontend and **GitHub Actions** for automated testing.

## Features

- **Frontend (React)**: Provides a user-friendly interface for submitting and displaying optimized code.
- **Backend (Flask)**: Handles API requests, interacts with OpenAI API, and processes user input.
- **OpenAI API Integration**: Uses GPT-4o to analyze and improve code readability and efficiency.
- **CI/CD with GitHub Actions**: Automates backend testing and deployment.
- **Secure API Key Management**: Utilizes **GitHub Secrets** to manage OpenAI API keys securely.

## Installation & Setup

### Prerequisites

Ensure you have the following installed:

- Python 
- Node.js (for frontend)
- OpenAI API key (stored in `.env` locally and in GitHub Secrets for deployment)

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/xuliugame/AI-Code-Improvement-Tool.git
   cd AI-Code-Improvement-Tool/backend
   ```
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables**:
   - Create a `.env` file in the `backend/` directory:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```
5. **Run the backend server**:
   ```bash
   python app.py
   ```
   The backend should be running on `http://127.0.0.1:5000`.

### Frontend Setup

1. **Navigate to the frontend folder**:
   ```bash
   cd ../frontend
   ```
2. **Install dependencies**:
   ```bash
   npm install
   ```
3. **Start the development server**:
   ```bash
   npm start
   ```
   The frontend should be accessible at `http://localhost:3000`.

## Running Tests

The backend has **automated tests** using `pytest`:

```bash
pytest tests/test_app.py
```

Tests are automatically run in **GitHub Actions** when code is pushed.

## Deployment

### Frontend Deployment (GitHub Pages)

The frontend is automatically deployed to **GitHub Pages** using `gh-pages`. To deploy manually:

```bash
npm run deploy
```

### Backend Deployment (GitHub Actions)

The backend runs tests on every push using **GitHub Actions**.

- API key is stored in **GitHub Secrets** as `OPENAI_API_KEY`.
- `.gitignore` ensures sensitive files like `.env` are not pushed.

## File Structure

```
AI-Code-Improvement-Tool/
│── .github/workflows/       # CI/CD configuration
│── backend/                 # Flask backend
│   ├── api/
│   │   ├── openai_api.py     # Handles OpenAI API requests
│   ├── tests/
│   │   ├── test_app.py       # Backend tests
│   ├── app.py                # Main Flask app
│   ├── requirements.txt      # Backend dependencies
│── frontend/                 # React frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── CodeInput.js  # Code input component
│   │   │   ├── Suggestions.js# Optimized code display
│   │   ├── App.js            # Main frontend app
│   ├── styles.css            # Frontend styling
│   ├── package.json          # Frontend dependencies
│── .gitignore                # Ignored files
│── README.md                 # Project documentation





