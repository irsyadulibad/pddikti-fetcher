from pydantic import BaseModel
from typing import List, Optional


class StudentResponse(BaseModel):
    """Model untuk response data mahasiswa"""
    id: str
    nama: str
    nama_prodi: str
    nama_pt: str
    nim: str
    sinkatan_pt: str


class StudentSearchResponse(BaseModel):
    """Model untuk response pencarian mahasiswa"""
    success: bool
    message: str
    data: List[StudentResponse]
    total: int


class ErrorResponse(BaseModel):
    """Model untuk response error"""
    success: bool
    message: str
    error: Optional[str] = None
