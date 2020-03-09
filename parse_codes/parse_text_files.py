import os

rootdir = "C:\\Users\\IZZY\\Downloads\\Bolso\\"
extensions = ('.srt')

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        ext = os.path.splitext(file)[-1].lower()
        if ext in extensions:
            f_prev = open(os.path.join(subdir, file), "r")
            f_new = open(os.path.splitext(os.path.join(subdir, file))[0] + '.txt', "w+")
            str_list = []
            
            for string in f_prev:
                if "-->" in string or string.strip().isdigit() or not string.strip():
                    continue
                    
                str_list.append(string)
                
            str_list = f7(str_list)
            
            for string in str_list:
                f_new.write(string)
                
            f_new.close()
            f_prev.close()