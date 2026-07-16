# Ragnarok - Simple Welcome Web Application

## Overview
A minimal Flask web application that displays a welcome message when accessing the home page.

## Features
- Single endpoint (`/`) that returns "Hello Neurostack User"
- Flask 3.x with modern Python patterns
- Docker support for AWS deployment
- Production-ready with Gunicorn

## Requirements
- Python 3.11+
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sumit-mishra-itp/ragnarok.git
cd ragnarok
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
# Edit .env if needed (defaults are fine for local development)
```

### 5. Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000/`

## Usage

Open your browser and navigate to:
```
http://localhost:5000/
```

You should see:
```
Hello Neurostack User
```

## API Endpoints

### GET /
- **Description:** Returns welcome message
- **Response:** Plain text "Hello Neurostack User"
- **Status Code:** 200 OK

### GET /health
- **Description:** Health check endpoint
- **Response:** JSON with status
- **Status Code:** 200 OK

## Docker Deployment

### Build Docker Image
```bash
docker build -t ragnarok:latest .
```

### Run Docker Container
```bash
docker run -p 5000:5000 ragnarok:latest
```

## AWS Deployment

### Using Docker on AWS ECS/EC2
1. Build the Docker image
2. Push to Amazon ECR:
```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
docker tag ragnarok:latest <account-id>.dkr.ecr.<region>.amazonaws.com/ragnarok:latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/ragnarok:latest
```
3. Deploy to ECS or EC2 using the pushed image

## Production Deployment

For production, the application uses Gunicorn as the WSGI server:
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 'app:create_app()'
```

## Testing

### Manual Testing
```bash
curl http://localhost:5000/
# Expected output: Hello Neurostack User

curl http://localhost:5000/health
# Expected output: {"status":"healthy"}
```

## Project Structure
```
ragnarok/
├── app.py                 # Application factory
├── config.py              # Configuration classes
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in git)
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore patterns
├── Dockerfile            # Docker configuration
├── .dockerignore         # Docker ignore patterns
├── README.md             # This file
└── routes/
    ├── __init__.py       # Routes package
    └── welcome_routes.py # Welcome endpoint
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, change the PORT in `.env` file:
```
PORT=8000
```

### Module Not Found Errors
Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

## License
MIT License

## Support
For issues or questions, please open an issue on GitHub.