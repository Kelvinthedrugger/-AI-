import os

def write_lib(source, file):
    if file.startswith("_"):
        print("skip %s since it started with _" % file)
        return True
    with open(source, "r") as f1, open(file, "w") as f2:
        for line in f1:
            f2.write(line)
    f1.close()
    f2.close()
    return True

def setup():
    if not os.path.isdir("emo_ai"):
        os.system("mkdir %s" % "emo_ai")
    os.chdir(os.getcwd() + "\emo_ai")

def main():
    # change current directory to emo_ai directory
    setup()
    # retrieve all the libs from source
    lib_source = "C:" + chr(92) + "Users" + chr(92) + "Kelvin" + chr(92) + "Documents" + chr(92) + "GitHub" + chr(92) + "EMO_AI" + chr(92) + "EMO_AI"
    lib_list = list(os.walk(lib_source))[0][2]
    print(lib_list)
    # write all the scripts from source
    for src in lib_list:
        if not write_lib(lib_source + chr(92) + src, src):
            print("Failed")
    print("Success")

if __name__ =="__main__":
    main()

