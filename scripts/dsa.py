# -*- coding: utf-8 -*-
"""Example of Dynamic Security Assesment (DSA) analysis using PyRAMSES"""

from PyRAMSES import sim, cfg
from PyRAMSES.globals import RAMSESError
import multiprocessing as mp
import os

num_daemons = mp.cpu_count()
DSTQueue = mp.JoinableQueue()
ResultQueue = mp.queues.Queue()
procs = []

def worker(workdir):
    """RAMSES daemon that will take care of disturbances."""
    
    os.chdir(workdir) # move worker to working directory
    ram = sim() # create new simulator instance
    
    for DST in iter( DSTQueue.get, None ):
        try:
            case = cfg(DST)
            case.addOut('Output_' + DST)
            ram.execSim(case)
        except RAMSESError, e:            
            ResultQueue.put((DST,e.message))
        DSTQueue.task_done()
    DSTQueue.task_done()
    del ram

def start_daemons(workdir):
    """Start num_daemons RAMSES daemons."""
    try:
        global procs
        if procs:
            print 'Daemons already running, please close them first'
            return
        for i in range(num_daemons):
            procs.append( mp.Process(target=worker, args=(workdir,)) )
            procs[-1].daemon = True
            procs[-1].start()
        print 'Daemons started and initialized: ', nb_active_daemons()

    except:
        import traceback
        traceback.print_exc()
        
def addCase(case):
    '''Adds a case to be simulated to the queue'''
    DSTQueue.put(case)
        
def close_daemons():
    '''Close the daemons'''
    try:
        print 'Waiting for current jobs to finish'
        DSTQueue.join()
        global procs
        for p in procs:
            DSTQueue.put( None )
        print 'Waiting for ',nb_active_daemons(), ' daemons to close'
        DSTQueue.join()
        for p in procs:
            p.join()
        del procs[:]
    except:
        import traceback
        traceback.print_exc()

def nb_active_daemons():
    '''Get number of active daemons'''
    return len(mp.active_children())
    
def get_DSTErrors_list():
    '''Get list of errors'''
    DST_error_list=[]
    while not  ResultQueue.empty():
        DST_error_list.append(ResultQueue.get())
    return DST_error_list

if __name__ == '__main__':
    start_daemons(os.getcwd())
    addCase('cmd_DSA1.txt')
    addCase('cmd_DSA2.txt')
    addCase('cmd_DSA3.txt')
    addCase('cmd_DSA4.txt')
    close_daemons()
    failed_DST_list=get_DSTErrors_list()
    if failed_DST_list:
        print 'Exit Msg   Disturbance'
        for x in failed_DST_list:
            print '   ',x[1], '    ', x[0].getDst()

    print "Finished everything...."