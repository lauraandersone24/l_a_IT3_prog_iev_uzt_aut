from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, MediaItem

engine = create_engine("sqlite:///media.db")
Session = sessionmaker(bind=engine)


def add_item(session, title, type_, status="planned"):
    item = MediaItem(title=title, type=type_, status=status)
    session.add(item)
    session.commit()
    return item


def mark_done(session, item_id):
    item = session.get(MediaItem, item_id)
    if item:
        item.status = "done"
        session.commit()
    return item


def get_all(session):
    return session.query(MediaItem).all()

def delete_item(session, item_id):
    item = session.get(MediaItem, item_id)
    if item:
        session.delete(item)
        session.commit()
    return item


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session()
    add_item(session, "Dune", "book")
    for item in get_all(session):
        print(item.title, item.type, item.status)