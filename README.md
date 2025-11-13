# PDDIKTI Scraper API

API sederhana untuk mengakses data mahasiswa dari PDDIKTI menggunakan FastAPI.

## Struktur Project

```
scrapedikti/
├── app/
│   ├── __init__.py
│   ├── config.py          # Konfigurasi aplikasi
│   ├── api/
│   │   ├── __init__.py
│   │   └── students.py    # Endpoint untuk mahasiswa
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py     # Model Pydantic
│   └── services/
│       ├── __init__.py
│       └── pddikti_service.py  # Service untuk PDDIKTI API
├── main.py                # FastAPI application
├── run.py                 # Script untuk menjalankan server
├── start_dev.sh           # Development server script
├── test_api.py            # Script untuk testing API
├── requirements.txt       # Dependencies
├── app_original.py        # Original script (untuk referensi)
├── .gitignore            # Git ignore file
└── README.md
```

## Instalasi

### Method 1: Quick Start (Recommended)

```bash
./start_dev.sh
```

### Method 2: Manual Installation

1. Buat virtual environment (opsional tapi direkomendasikan):

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Jalankan server:

```bash
python run.py
```

Atau menggunakan uvicorn langsung:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Penggunaan

### Endpoint Tersedia

1. **GET /** - Root endpoint
2. **GET /health** - Health check
3. **GET /api/v1/search/students?keyword={nama}** - Cari mahasiswa

## Testing

Untuk menguji API, jalankan script test:

```bash
python test_api.py
```

Atau test manual dengan curl:

```bash
# Cari mahasiswa dengan nama "Restu Imam Syafii"
curl "http://localhost:8000/api/v1/search/students?keyword=Restu%20Imam%20Syafii"
```

### Response Format

```json
{
  "success": true,
  "message": "Berhasil menemukan 2 data mahasiswa",
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

## API Documentation

Setelah menjalankan server, dokumentasi API dapat diakses di:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Environment Variables

- `DEBUG`: Set to "true" untuk development mode (default: false)
- `HOST`: Host untuk server (default: 0.0.0.0)
- `PORT`: Port untuk server (default: 8000)
- `LOG_LEVEL`: Level logging (default: INFO)

## Development

Untuk development, set environment variable:

```bash
export DEBUG=true
python run.py
```
