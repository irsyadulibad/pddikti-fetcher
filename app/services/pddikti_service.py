from pddiktipy import api
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class PddiktiService:
    """Service untuk berinteraksi dengan PDDIKTI API"""

    def __init__(self):
        self.client = None

    async def search_students(self, keyword: str) -> List[Dict[str, Any]]:
        """
        Mencari data mahasiswa berdasarkan keyword

        Args:
            keyword (str): Kata kunci pencarian (nama mahasiswa)

        Returns:
            List[Dict[str, Any]]: List data mahasiswa

        Raises:
            Exception: Jika terjadi error saat mengakses API
        """
        try:
            with api() as client:
                result = client.search_mahasiswa(keyword)

                if not result:
                    return []

                # Pastikan hasilnya adalah list
                if isinstance(result, dict):
                    result = [result]
                elif not isinstance(result, list):
                    return []

                # Filter dan format data
                formatted_result = []
                for item in result:
                    if isinstance(item, dict) and all(key in item for key in ['id', 'nama']):
                        formatted_result.append({
                            'id': item.get('id', ''),
                            'nama': item.get('nama', ''),
                            'nama_prodi': item.get('nama_prodi', ''),
                            'nama_pt': item.get('nama_pt', ''),
                            'nim': item.get('nim', ''),
                            'sinkatan_pt': item.get('sinkatan_pt', '')
                        })

                return formatted_result

        except Exception as e:
            logger.error(f"Error searching students: {str(e)}")
            raise Exception(f"Gagal mencari data mahasiswa: {str(e)}")

    async def get_student_detail(self, student_id: str) -> Dict[str, Any]:
        """
        Mendapatkan detail mahasiswa berdasarkan ID

        Args:
            student_id (str): ID mahasiswa

        Returns:
            Dict[str, Any]: Detail data mahasiswa
        """
        try:
            with api() as client:
                # Implementasi untuk mendapatkan detail mahasiswa
                # Tergantung pada method yang tersedia di pddiktipy
                pass
        except Exception as e:
            logger.error(f"Error getting student detail: {str(e)}")
            raise Exception(f"Gagal mendapatkan detail mahasiswa: {str(e)}")
