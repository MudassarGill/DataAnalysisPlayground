import numpy as np
import logging
import time

# Logger setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("second.log")
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Logging start
logger.info("Starting numpy")

# Numpy array creation
arr = np.array([1, 2, 3, 4, 5])
print(arr)
logger.info("Numpy array created: %s", arr.tolist())

#calclution using arrasy

logger.info('Python list sum')
# Python list
arr = np.array([1,2,3])

print(arr * 2)
logger.info("Numpy array created: %s", arr.tolist())
