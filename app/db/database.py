from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

# DB 연결 엔진 생성
engine = create_engine(settings.database_url)

# DB 작업 단위 생성기
sessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine,
)

# ORM 모델들이 상속받을 기본 클래스
Base = declarative_base()

# FastAPI API에서 DB 세션을 주입받기 위한 함수
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

