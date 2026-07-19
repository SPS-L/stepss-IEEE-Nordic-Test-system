
# coding: utf-8

from scipy.io import FortranFile
import numpy as np
import matplotlib.pyplot as plt

f = FortranFile( 'obs.trj', 'r' )

busnum = f.read_ints()[0]
busname = []
for i in range(busnum):
    busname.append(f.read_record(dtype="S18")[0].decode('UTF-8').strip())

shunum = f.read_ints()[0]
shuname = []
for i in range(shunum):
    shuname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())

ldnum = f.read_ints()[0]
ldname = []
for i in range(ldnum):
    ldname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())

branum = f.read_ints()[0]
braname = []
for i in range(branum):
    braname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())

syncnum = f.read_ints()[0]
excobsnum = []
excobsname = []
torobsnum = []
torobsname = []
syncname = []

for i in range(syncnum):    
    syncname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())
    excobsnum.append(f.read_ints()[0])
    excobsname.append([])
    for j in range(excobsnum[i]):
        excobsname[i].append(f.read_record(dtype="S10")[0].decode('UTF-8').strip())
    torobsnum.append(f.read_ints()[0])
    torobsname.append([])
    for j in range(torobsnum[i]):
        torobsname[i].append(f.read_record(dtype="S10")[0].decode('UTF-8').strip())

injnum = f.read_ints()[0]
injobsnum = []
injobsname = []
injname = []

for i in range(injnum):    
    injname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())
    injobsnum.append(f.read_ints()[0])
    injobsname.append([])
    for j in range(injobsnum[i]):
        injobsname[i].append(f.read_record(dtype="S10")[0].decode('UTF-8').strip())

twopnum = f.read_ints()[0]
twopobsnum = []
twopobsname = []
twopname = []

for i in range(twopnum):    
    twopname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())
    twopobsnum.append(f.read_ints()[0])
    twopobsname.append([])
    for j in range(twopobsnum[i]):
        twopobsname[i].append(f.read_record(dtype="S10")[0].decode('UTF-8').strip())

dctlnum = f.read_ints()[0]
dctlobsnum = []
dctlobsname = []
dctlname = []

for i in range(dctlnum):    
    dctlname.append(f.read_record(dtype="S20")[0].decode('UTF-8').strip())
    dctlobsnum.append(f.read_ints()[0])
    dctlobsname.append([])
    for j in range(dctlobsnum[i]):
        dctlobsname[i].append(f.read_record(dtype="S10")[0].decode('UTF-8').strip())

totobs = 2*busnum + shunum + 2*ldnum + 6*branum + 13*syncnum + sum(excobsnum) + sum(torobsnum) + sum(injobsnum) + sum(twopobsnum) + sum(dctlobsnum)

results = []
buffsz = f.read_ints(np.int64)[0]
while buffsz > 0:
    temp = f.read_reals(dtype=np.float64)
    results = np.concatenate((results, temp))
    buffsz = f.read_ints(np.int64)[0]

results = np.reshape(results, (-1,totobs+1), order='C')

time = results[:,0]
np.delete(results, (0), axis=0)

results = np.asfortranarray(results)

try:
    i=busname.index("1041")
except ValueError:
    print("Bus not found")
else:
    plt.plot(time, results[:,2*i+1])
    plt.axis([0, 200, 0.6, 1.1])
    plt.show()

