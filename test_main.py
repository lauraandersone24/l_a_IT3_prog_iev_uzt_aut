import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from main import add_item, mark_done, get_all, delete_item, set_rating  


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def test_add_item(session):
    item = add_item(session, "Dune", "book")
    assert item.title == "Dune"
    assert item.status == "planned"


def test_mark_done(session):
    item = add_item(session, "Interstellar", "movie")
    mark_done(session, item.id)
    assert get_all(session)[0].status == "done"

def test_delete_item(session):
    item = add_item(session, "Dune", "book")
    delete_item(session, item.id)
    assert get_all(session) == []

def test_set_rating(session):
    item = add_item(session, "Dune", "book")
    set_rating(session, item.id, 5)
    assert get_all(session)[0].rating == 5