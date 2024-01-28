import logging
import os
from datetime import datetime

directory = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
path = os.path.join(os.getcwd(), 'logs', directory)
os.makedirs(path, exist_ok=True)

filename = os.path.join(path, directory)

logging.basicConfig(
    filename=filename,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


