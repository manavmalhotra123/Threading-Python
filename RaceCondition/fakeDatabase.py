import logging as log
import time
from concurrent.futures import ThreadPoolExecutor

class FakeDatabase:
    def __init__(self):
        self.value = 0.0

    # here the updation is atomic function 
    def update(self, name):
        log.info(f"Thread {name}: Started update")
        # copy is saved here which can be read by the other thread when switching is done 
        local_copy = self.value
        local_copy += 2
        time.sleep(0.5)
        self.value = local_copy
        log.info(f"Thread {name}: Finished updating")

if __name__ == "__main__":
    log.basicConfig(format="%(asctime)s : %(message)s", level=log.DEBUG, datefmt="%H:%M:%S")
    DB = FakeDatabase()
    log.info(f"Testing update. Start Value is {DB.value}")
    with ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(DB.update, index)
    log.info("Testing update. Ending value is %f.", DB.value)
