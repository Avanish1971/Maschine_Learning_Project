from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging

def test_exception():
    try:
        logging.info("error are comes here's ")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)

if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        raise SensorException(e, sys)
