import time

class ProgressBar: 
    def __init__(self, loop_length):
        import time
        self.start = time.time()
        self.increment_size = 100.0/loop_length
        self.curr_count = 0
        self.curr_pct = 0
        self.overflow = False
        print '% complete:',
    
    def increment(self):
        self.curr_count += self.increment_size
        if int(self.curr_count) > self.curr_pct:
            self.curr_pct = int(self.curr_count)
            if self.curr_pct <= 100:
                print self.curr_pct, 
            elif self.overflow == False:
                print "\n*!* Count has gone over 100%; likely either due to:\n*!*   - an error in the loop_length specified when " + \
                      "progress_bar was instantiated\n*!*   - an error in the placement of the increment() function"
                print '*!* Elapsed time when progress bar full: %0.1f seconds.' % (time.time() - self.start)
                self.overflow = True

    def finish(self):
        if self.curr_pct == 99:
            print "100", # this is a cheat, because rounding sometimes makes the maximum count 99. One day I'll fix this bug.
        if self.overflow == True:
            print '*!* Elapsed time after end of loop: %0.1f seconds.\n' % (time.time() - self.start)
        else:
            print '\nElapsed time: %0.1f seconds.\n' % (time.time() - self.start)
