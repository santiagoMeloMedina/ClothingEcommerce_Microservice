
import os

env = os.environ

KEY = env.get("JWT_KEY")
ALGORITHM = env.get("JWT_ALGORITHM")