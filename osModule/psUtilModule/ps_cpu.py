import psutil


### used for seeing device infomation 
print(psutil.cpu_percent(interval=1))
print(psutil.cpu_count())
print(psutil.cpu_freq())
print(psutil.disk_usage(r"C:\Users\AURAGAM\Desktop\PythonTutorial\Collections"))

mem = psutil.virtual_memory()
print(mem.total , mem.used , mem.percent) 

disk = psutil.disk_usage("/")
print(disk.total , disk.used , disk.percent) 

net = psutil.net_io_counters()
print(net.bytes_sent ,net.bytes_recv) 