# test_db.py
from database import SessionLocal, Lawyer

def test_connection():
    db = SessionLocal()
    try:
        lawyers = db.query(Lawyer).all()
        for lawyer in lawyers:
            print(lawyer.name)
    finally:
        db.close()

test_connection()
