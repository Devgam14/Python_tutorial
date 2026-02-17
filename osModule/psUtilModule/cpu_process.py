import psutil

# for process in psutil.process_iter(["pid", "name"]):
#     print(process)
show = psutil.Process(14016)
print(show.cpu_percent()) ### show cpu usage percent 

print(show.memory_info()) ### show memory info 
print(show.open_files()
# show.terminate() ## killing a process id 