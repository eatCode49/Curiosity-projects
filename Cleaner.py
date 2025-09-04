import os, shutil

cache_dirs = [
    r"C:\Windows\Temp",
    os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Local\Temp"),
    r"C:\Windows\Prefetch",
    r"C:\Windows\SoftwareDistribution\Download",
    os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Local\Microsoft\Windows\INetCache"),
    os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Recent"),
    r"C:\$Recycle.Bin"
]



for cache in cache_dirs:
    if os.path.exists(cache):
        for item in os.listdir(cache):
            item_path = os.path.join(cache, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                pass
            except PermissionError as p:
                pass

