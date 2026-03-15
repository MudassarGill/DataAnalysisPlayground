import numpy as np
import logging
import time

# Logger setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("numpy.log")
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




logger.info('Python list sum')
# Python list
py_list = list(range(1, 1000001))
start = time.time()
py_list_sum = sum(py_list)
end = time.time()
print("Python list sum:", py_list_sum, "Time:", end-start)
logger.info("Python list sum: %s, Time: %s", py_list_sum, end-start)

logger.info('NumPy array sum')
# NumPy array
np_array = np.array(range(1, 1000001))
start = time.time()
np_array_sum = np.sum(np_array)
end = time.time()
print("NumPy array sum:", np_array_sum, "Time:", end-start)
logger.info("NumPy array sum: %s, Time: %s", np_array_sum, end-start)



