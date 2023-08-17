from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str = Field(..., min_length=1, max_length=50)
    overview: str = Field(..., min_length=1, max_length=500)
    year: int = Field(..., gt=1900, lt=2100)
    rating: float = Field(..., gt=0, lt=10)
    category: str = Field(..., min_length=1, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Godfather",
                "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                "year": 1972,
                "rating": 9.2,
                "category": "Drama",
            }
        }
