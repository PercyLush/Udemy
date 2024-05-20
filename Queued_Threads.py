import time 
import random
import queue

from threading import Thread

counter = 0
job_queue = queue.Queue() # things to be printed out
counter_queue = queue.Queue() # amounts by which to increase counter