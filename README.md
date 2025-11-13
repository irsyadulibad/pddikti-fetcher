# PDDIKTI Scraper API

A simple API to access student data from PDDIKTI using FastAPI.

## Project Structure

```
scrapedikti/
├── app/
│   ├── __init__.py
│   ├── config.py          # Application configuration
│   ├── api/
│   │   ├── __init__.py
│   │   └── students.py    # Student endpoints
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py     # Pydantic models
│   └── services/
│       ├── __init__.py
│       └── pddikti_service.py  # Service for the PDDIKTI API
├── main.py                # FastAPI application
├── run.py                 # Script to run the server
├── requirements.txt       # Dependencies
├── app_original.py        # Original script (for reference)
├── .gitignore             # Git ignore file
└── README.md
```

## Installation

1. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the server:

```bash
python run.py
```

Or run uvicorn directly:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Usage

### Available Endpoints

1. GET / — Root endpoint
2. GET /health — Health check
3. GET /api/v1/search/students?keyword={name} — Search students

## Testing

To test the API, run this curl command:

```bash
# Search for a student named "Restu Imam Syafii"
curl "http://localhost:8000/api/v1/search/students?keyword=Restu%20Imam%20Syafii"
```

### Response Format

```json
{
  "success": true,
  "message": "Successfully found 2 students",
  "data": [
    {
      "id": "HHcoIvXzHYZAIHyzuuwbqlEuLJlS0VbNr7ljYIYIVk_w-7LbQTpN7K1gxRDKHAXCrFWXDQ==",
      "nama": "RESTU IMAM SYAFII",
      "nama_prodi": "TEKNIK INFORMATIKA",
      "nama_pt": "POLITEKNIK NEGERI JEMBER",
      "nim": "E41221735",
      "sinkatan_pt": "POLIJE"
    }
  ],
  "total": 1
}
```

Note: Field names in the response follow the source system (Indonesian), e.g., "nama" (name), "nama_prodi" (program), "nama_pt" (university).

## API Documentation

After starting the server, the API docs are available at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Environment Variables

- `DEBUG`: Set to "true" for development mode (default: false)
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `LOG_LEVEL`: Logging level (default: INFO)

### Environment file (.env)

This project supports loading configuration from a `.env` file using `python-dotenv`. A sample file is provided as `.env.example`. To use it:

1. Copy the example file to `.env`:

```bash
cp .env.example .env
```

2. Edit `.env` to adjust settings (for example `DEBUG`, `HOST`, `PORT`, `LOG_LEVEL`).

Notes:

- Values in the `.env` file are loaded at application start and are used as defaults; environment variables set in the system will override `.env` values.
- It's recommended to add `.env` to your `.gitignore` so secrets or environment-specific settings are not committed.
- `.env.example` is safe to commit and documents the available variables and defaults.

## Development

For development, set the environment variable and run:

```bash
export DEBUG=true
python run.py
```
