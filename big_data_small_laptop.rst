Big data in little laptop
====================


Juan Nunez-Iglesias

We have three types of data: 
    * small data (fits on your PC)
    * intermediate data (fits on your PC but only if you think about it)
    * big data (fits on a cluster)

For intermediate data (multi-GB range) generators are very useful.

So yield, yield, yield means that we get a small memory usage. The disadvantage is that the code becomes quite unclear. For this purpose we have toolz.

    import toolz as tz

    # reads a tsv, computes the line by line log and computes the mean over all of them
    tz.pipe(fin, readtsv, log, mean)


    # we have a nice decorator that converts functions that are called with the wrong number of arguments into a new function
    @tz.curry
    def myadd(a,b):
        return a+b

    add5 = myadd(5)
    add5(7) # returns 12
    # NB only works for stuff that takes exactly two arguments






