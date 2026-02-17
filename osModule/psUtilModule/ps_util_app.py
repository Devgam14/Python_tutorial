import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

cpu_history = []
ram_history = []

def update(frame) :
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    
    cpu_history.append(cpu)
    ram_history.append(ram)

    if len(cpu_history) > 60:
        cpu_history.pop(0)
        ram_history.pop(0)
        
    plt.cla()
    plt.plot(cpu_history , label="CPU %")    
    plt.plot(ram_history , label="RAM %") 
    plt.ylim(0, 100)
    plt.legend()
    plt.title("Real-Time Cpu & Ram Usage")
    plt.xlabel("Seconds")   
    plt.xlabel("Usage %")   

ani = FuncAnimation(plt.gcf(), update, interval=1000)
plt.tight_layout()
plt.show()