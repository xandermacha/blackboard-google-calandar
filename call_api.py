import time
import create
import hw

def call():
    
    numline = int(hw.numline())
    for i in range(numline):
        create.mevent(i)
        print(f"item {i + 1} added")
        time.sleep(2)
        
         
    
if __name__ == '__main__':
    call()