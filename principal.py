import pyplanet
import cyplanet
import time

start_time_py = time.time()
pyplanet.main()
final_time_py =time.time()
total_time_py=final_time_py-start_time_py
print("Python: --- %s seconds ---" % total_time_py)

start_time_cy = time.time()
cyplanet.main()
final_time_cy =time.time()
total_time_cy=final_time_cy-start_time_cy
print("Cython: --- %s seconds ---" % total_time_cy)


