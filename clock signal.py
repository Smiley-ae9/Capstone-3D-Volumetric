import pigpio
import time
    
tick0 = None
pi = pigpio.pi()
tick1 = None
    
    
def mycallback(gpio, level, tick):
    global tick0, tick1
    
    if level == 0:
        tick0 = tick
        if tick1 is not None:
            diff = pigpio.tickDiff(tick1, tick)
            print ("high for " + str(diff) + " microseconds")
    
    else:
        tick1 = tick
        if tick0 is not None:
            diff = pigpio.tickDiff(tick0, tick)
            print ("low for " + str(diff) + " microseconds")
    
    
#pigpio.start()
    
cb = pi.callback(4, pigpio.EITHER_EDGE, mycallback)
    
time.sleep(5)
    
cb.cancel()  # cancel callback
    
#pigpio.stop()