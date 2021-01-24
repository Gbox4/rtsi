import datetime

def file_len(fname):
    i = 0
    with open(fname, encoding='utf-8') as f:
        for i, l in enumerate(f):
            pass
    

    return i + 1

#TODO: include more error data like file it was called in
def log_error(msg):
    with open("error.log", "a") as f:
        f.write(f"ERROR {datetime.datetime.now()}: "+msg)