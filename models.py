from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MediaItem(Base):
    __tablename__ = "media_items"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)    # "book" / "movie" / "music"
    status = Column(String, default="planned")  # "planned" / "in_progress" / "done"
    rating = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<MediaItem(title='{self.title}', type='{self.type}', status='{self.status}', rating={self.rating})>"