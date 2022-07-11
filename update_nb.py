import os

# kinda slow and dump but it works
def write_nb(source, file):
    if file.startswith("_"):
        print("skip %s since it started with _" % file)
        return True
    if not file.endswith(".ipynb"):
        print("%s is not a notebook, skipped" % file)
        return True
    with open(source, "r") as f1, open(file, "w") as f2:
        for line in f1:
            f2.write(line)
    f1.close()
    f2.close()
    return True

def setup():
    if not os.path.isdir("emo_ds"):
        os.system("mkdir %s" % "emo_ds")
    os.chdir(os.getcwd() + "\emo_ds")

def main():
    # change current directory to emo_ds directory
    setup()
    # retrieve all the libs from source
    lib_source = "C:" + chr(92) + "Users" + chr(92) + "Kelvin" + chr(92) + "Documents" + chr(92) + "GitHub" + chr(92) + "EMO_AI"
    lib_list = list(os.walk(lib_source))[0][2]
    print(lib_list)
    # write all the scripts from source
    for src in lib_list:
        if not write_nb(lib_source + chr(92) + src, src):
            print("Failed")
            exit(1)
    print("Success")

if __name__ =="__main__":
    main()

