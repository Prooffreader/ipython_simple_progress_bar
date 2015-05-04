# ipython_simple_progress_bar
A quick and dirty progress 'bar' (really, a count to 100) that will display below an IPython/Jupyter cell while it is running

[Link to NBViewer preview of full example](http://nbviewer.ipython.org/github/Prooffreader/ipython_simple_progress_bar/blob/master/example.ipynb)

Example use:

    loop_length = 1000000

    pbar = ProgressBar(loop_length)
    for i in range(loop_length):
        # your code goes here
        pbar.increment()
    pbar.finish()
    
Output below cell:

    % complete: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
    31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61
    62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92
    93 94 95 96 97 98 99 100
    Elapsed time: 1.7 seconds.
