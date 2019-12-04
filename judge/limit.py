import resource

MAX_VIRTUAL_MEMORY = 1 * 1024 * 1024

def change_max_virtual_memory(value):
    global MAX_VIRTUAL_MEMORY
    MAX_VIRTUAL_MEMORY = value

def limit_virtual_memory():
    try:
        resource.setrlimit(resource.RLIMIT_AS, (MAX_VIRTUAL_MEMORY, resource.RLIM_INFINITY))
        #RLIMIT_AS
    except Exception as e:
        print("Limit error:", e)
