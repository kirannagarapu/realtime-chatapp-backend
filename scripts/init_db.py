from app.core.database import engine, Base
from app.models import user  # ensure models are imported

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database initialized successfully!")
