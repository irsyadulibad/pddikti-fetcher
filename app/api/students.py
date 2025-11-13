from fastapi import APIRouter, HTTPException, Query
from typing import Optional
import logging

from ..services.pddikti_service import PddiktiService
from ..models.student import StudentSearchResponse, ErrorResponse, StudentResponse

logger = logging.getLogger(__name__)

router = APIRouter()
pddikti_service = PddiktiService()


@router.get("/search/students", response_model=StudentSearchResponse)
async def search_students(
    keyword: str = Query(..., description="Kata kunci pencarian nama mahasiswa", min_length=3)
):
    """
    Endpoint untuk mencari data mahasiswa berdasarkan nama

    Args:
        keyword (str): Kata kunci pencarian (nama mahasiswa), minimal 3 karakter

    Returns:
        StudentSearchResponse: Response dengan data mahasiswa yang ditemukan

    Raises:
        HTTPException: Jika terjadi error saat pencarian
    """
    try:
        # Validasi input
        if not keyword or len(keyword.strip()) < 3:
            raise HTTPException(
                status_code=400,
                detail="Keyword pencarian harus minimal 3 karakter"
            )

        # Search students
        students_data = await pddikti_service.search_students(keyword.strip())

        # Convert to response model
        students = [StudentResponse(**student) for student in students_data]

        return StudentSearchResponse(
            success=True,
            message=f"Berhasil menemukan {len(students)} data mahasiswa" if students else "Tidak ada data mahasiswa yang ditemukan",
            data=students,
            total=len(students)
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in search_students endpoint: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Terjadi error internal: {str(e)}"
        )


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "PDDIKTI Scraper API is running"}
