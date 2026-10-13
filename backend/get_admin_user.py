import os
from pathlib import Path
from dotenv import load_dotenv
from core.security import hash_password, verify_password


from passlib.context import CryptContext

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


password = os.getenv("ADMIN_PASSWORD")  # change this
hashed = pwd_context.hash(password)

print(hashed)
print(verify_password(password, hashed))

mashed1= hash_password(password)
print(mashed1)

print(verify_password(password, mashed1))