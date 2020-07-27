import sys
import numpy as np
import math 
import time
import random
import os
import socket
rootdir = os.path.dirname(os.path.dirname(__file__))
os.sys.path.insert(0, rootdir)
print(rootdir)
from roman import *
from roman.rq import *

#############################################################
# These tests require a real hand for now (no sim option)
#############################################################
def connection_test(real_robot):
    print(f"Running {__file__}::{connection_test.__name__}()")
    con = Connection() if real_robot else SimConnection(None)
    con.connect()
    hand = Hand(con)
    hand.close(blocking=False)
    time.sleep(2)
    hand.open(blocking=False)
    time.sleep(2)
    con.disconnect()
    print("Passed.")

def controller_test():
    print(f"Running {__file__}::{controller_test.__name__}()")
    # check that a tight lop also works
    con = Connection()    
    con.connect()
    hand = Hand(HandController(con))
    hand.close()
    assert hand.state.position() == Position.CLOSED

    hand.open()
    assert hand.state.position() == Position.OPENED
    con.disconnect()
    print("Passed.")

#############################################################
# Runner
#############################################################
def run(real_robot = False):
    
    if real_robot:
        connection_test(real_robot)
        #controller_test()
   
if __name__ == '__main__':
    run(True)