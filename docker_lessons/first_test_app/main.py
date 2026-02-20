import time
import numpy as np

total = 100

for i in range(total):
    print(f"sin({i/100}) = {np.sin(i/100):.4f}")
    time.sleep(1)