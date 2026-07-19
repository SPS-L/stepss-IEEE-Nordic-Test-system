#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:57:11 2017

@author: Petros
"""

import warnings
import os
import errno
from scipy.io import FortranFile
import numpy as np

class extractor(object):
    """Extractor class
    :param str traj: the trajectory path

    :Example:

    >>> import PyDyngraph
    >>> ext = PyDyngraph.extractor('obs.trj')
    
    """
    
    def __init__(self,traj):
        
        if not isinstance(traj, str):
            raise TypeError('PyDyngraph: Class Extractor expects a string path of the trajectory file to initialize.')
        
        self._trajfilename = traj
        
        if not os.path.isfile(traj):
            raise FileNotFoundError(errno.ENOENT, 
                                    os.strerror(errno.ENOENT), traj)    
            
        f = FortranFile(traj, 'r')
        
        self._busnum = f.read_ints()[0]
        self._busname = []
        for i in range(self._busnum):
            self._busname.append(f.read_record(dtype="S18")[0].decode('UTF-8').strip())
        
        self._shunum = f.read_ints()[0]
        self._shuname = []
        for i in range(self._shunum):
            self._shuname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())
        
        self._ldnum = f.read_ints()[0]
        self._ldname = []
        for i in range(self._ldnum):
            self._ldname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())
        
        self._branum = f.read_ints()[0]
        self._braname = []
        for i in range(self._branum):
            self._braname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())
        
        self._syncnum = f.read_ints()[0]
        self._excobsnum = []
        self._excobsname = []
        self._torobsnum = []
        self._torobsname = []
        self._syncname = []
        for i in range(self._syncnum):    
            self._syncname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())
            self._excobsnum.append(f.read_ints()[0])
            self._excobsname.append([])
            for j in range(self._excobsnum[i]):
                self._excobsname[i].append(f.read_record(dtype="S10")[0].decode('UTF-8').strip())
            self._torobsnum.append(f.read_ints()[0])
            self._torobsname.append([])
            for j in range(self._torobsnum[i]):
                self._torobsname[i].append(f.read_record(dtype="S10")[0].decode('UTF-8').strip())
        
        self._injnum = f.read_ints()[0]
        self._injobsnum = []
        self._injobsname = []
        self._injname = []
        for i in range(self._injnum):    
            self._injname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())
            self._injobsnum.append(f.read_ints()[0])
            self._injobsname.append([])
            for j in range(self._injobsnum[i]):
                self._injobsname[i].append(f.read_record(dtype="S10")[0].decode('UTF-8').strip())
        
        self._twopnum = f.read_ints()[0]
        self._twopobsnum = []
        self._twopobsname = []
        self._twopname = []
        for i in range(self._twopnum):    
            self._twopname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())
            self._twopobsnum.append(f.read_ints()[0])
            self._twopobsname.append([])
            for j in range(self._twopobsnum[i]):
                self._twopobsname[i].append(f.read_record(dtype="S10")[0].decode('UTF-8').strip())
        
        self._dctlnum = f.read_ints()[0]
        self._dctlobsnum = []
        self._dctlobsname = []
        self._dctlname = []
        for i in range(self._dctlnum):    
            self._dctlname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())
            self._dctlobsnum.append(f.read_ints()[0])
            self._dctlobsname.append([])
            for j in range(self._dctlobsnum[i]):
                self._dctlobsname[i].append(f.read_record(dtype="S10")[0].decode('UTF-8').strip())
        
        self._totobs = 2*self._busnum + self._shunum + 2*self._ldnum + 6*self._branum + \
                       13*self._syncnum + sum(self._excobsnum) + sum(self._torobsnum) + \
                       sum(self._injobsnum) + sum(self._twopobsnum) + sum(self._dctlobsnum)
        
        self._results = []
        buffsz = f.read_ints(np.int64)[0]
        while buffsz > 0:
            temp = f.read_reals(dtype=np.float64)
            self._results = np.concatenate((self._results, temp))
            buffsz = f.read_ints(np.int64)[0]
        
        self._results = np.reshape(self._results, (-1,self._totobs+1), order='C')
        
        self._time = self._results[:,0]
        np.delete(self._results, (0), axis=0)
        f.close()
 
    def __del__(self):
        warnings.warn("Extractor of file %s was deleted." % self._trajfilename)
        
    def getBus(self, busname):
        try:
            i=self._busname.index(busname)
        except ValueError:
            print("Bus not found")
        return self.getBusClass(self._time, self._results, i)

    class getBusClass(object):
        def __init__(self, time, results, i):
            self._time = time
            self._results = results
            self._i = i

        @property
        def mag(self):
            return self._time, self._results[:,2*self._i+1]