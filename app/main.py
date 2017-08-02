# main 

import state
state = state.state()

import cloud
cloud = cloud.cloud()

import engine
engine = engine.engine()




def Initialize():
    # initialize state -> recognize and be aware of other cloud machines running
    pass



def Run():
    engine.Run()
    pass


try:
    Initialize()
    Run()
except: 
    # error 




