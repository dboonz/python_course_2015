Works on the blue-gene project

Speaker: Eilif Muller (eilif dot mueller at epfl dot ch)

New processors have more cores, not faster single-threaded performance

Scientific parallel processing is usually pretty easy because the computations are not coupled.

Objectives:
    1. Get hands-on experiments
    2. Get familiar with the most useful APIs (8 functions each)
    2. Think parallel

Example: Parallel sum (reduce)
------------------------------
What to look out for:
    1. Load balancing: The program will be as fast as the slowest task.
    2. Speedup: The most speedup that you can expect is the number of threads
    3. Scaling: Usually there will be some part of the algorithm that continues
           to be serial. So this will lead to a dropoff when the number of CPUs is increased. 


Types of concurrency
--------------------
SMP (Few cores), Message passsing (More cores), Stream (GPU)

Multicore processing using IPython
-----------------------------------

Cheat sheet:


    from IPython.parralel import client
    mec = ....
    from scipy import factorial
    exe = mec.execute()
    exe("from scipy import factorial")
    result = mec.map(factorial, range(int(4e5)))

    # scatter an iterable over the CPUs
    mec.scatter("a", "hello world")
    mec['a']: # returns ['hel', 'lo ', 'worl', 'ld']
    mec.execute('a = a.upper()', targets=[2,3])

    # gather: retrieve and concatenate the iterable (inverse scatter)
    ''.join(mec.gather("a")) # returns 'hello WORLD'
    # difference with mec['a']: flattens the array in the case that arrays were
    # returned

If you disconnect, the workers stay alive, so you have to actually kill them if
you want to have a clean sheet.

Advantages: Easy to program
Main disadvantage: There is no shared memory access. This leads to more memory
usage and slowdowns.


SMP: Symmetric multiprocessing
------------------------------
Used for Parallel CPU's. At most 50 cores.


Advantages: Shared memory access
Disadvantage: Only works on small clusters (needs to be on one PC)
Example:

    import multiprocessing as mp
    pool = mp.Pool()
    result = pool.map(myfunc, x)
    lock = mp.Lock()
    
Issues to watch out for: Deadlock. Always release your lock. Difficult to debug
because the bug might be infrequent (race condition). The scheduling is
dependent on the OS.

Shared memory numpy access

Part 3: Mpi4pi
---------------

Apparently one of the best APIs.

Basic usage:
    $ mpiexec -n 16 python helloworld.py

Features:
   P2P messaging between the different threads,
   Every thread has it's own ID.

Basic stuff:
    from mpi4py import MPI
    # figure out how large the world is (how many processes we have)
    comm = MPI.COMM_WORLD
    # figure out # CPUS
    comm.size
    comm.rank # which process am I. Zeroth rank is usually used for serial stuff,
    #"master"

    rank = comm.Get_rank()

    if rank = 0:
        data = {...}
        comm.Send(data, dest=1, tag=11) # tag is "communication channel"
    elif rank == 1:
        data = comm.Recv(source=0, tag=11) 

    # with numpy
    if rank = 0:
        data = numpy.arange(1000, dtype='i')
        comm.Send([data, MPI.INT], dest=1, tag=77)
    elif rank==1:
        # preallocate the memory where the message is going to arrive
        data = np.empty(1000, dtype='i')
        comm.Recv([data, MPI.INT], source=0, tag=77)

    # nonblocking: Prepend I, so req = comm.Isend(data, dest=1, ...)
    # with numpy
    if rank = 0:
        data = numpy.arange(1000, dtype='i')
        req = comm.Isend([data, MPI.INT], dest=1, tag=77)
        # returns a request
    elif rank==1:
        # preallocate the memory where the message is going to arrive
        data = np.empty(1000, dtype='i')
        req1 = comm.Irecv([data, MPI.INT], source=0, tag=77)
        # wait for all things to finish
        status = [MPI.Status(), ...]
        # wait for all request to have finished
        MPI.Request.Waitall([req1, ...], status)

    Watch out with gather: It is a collective operation. To gather a result
    _all_ the clusters have to send it! So for all, Scatter and Gather, even
    though only rank 0 will have a proper result, the rest just gibberish

    Nice other stuff: Parallel IO!
    It is also compatible with ipcluster
    ipcluster start -n 4 --engines=MPIEngineSetLauncher

    Use px to execute on all numbers

    Look at PyBrook
    


GPU processing
===============

They are AWESOME!





    


