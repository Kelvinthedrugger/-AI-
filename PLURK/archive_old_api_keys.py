
def main():
    import os
    # check if there's existing API.keys file first
    if not os.path.isfile("API.keys"):
        print("file does not exist, exit")
        return
    dirname = "ARCHIVE_API_KEYS"
    # create folder for archive (old) api keys if not exists
    if not os.path.isdir(dirname):
        os.system("mkdir %s" % dirname)
    # read the current file count to prevent collision
    from pathlib import Path
    filename = Path(dirname + "/cnt.txt")
    counter = 0
    if os.path.isfile(filename):
        # this file contains only one line, which is
        # the counter of current number of files
        with open(filename, "r") as f:
            for line in f:
                counter = int(line.strip("\n "))
            f.close()
        counter += 1
    api_name = f"API{counter}.keys"
    # just in case the cnt.txt file went wrong
    while os.path.isfile(Path(dirname+"/"+api_name)):
        counter += 1
        api_name = f"API{counter}.keys"
    # rename our current API.keys
    # it'll be moved to the "dirname" directory simultaneously
    api_name = Path(dirname+"/"+api_name)
    os.rename("API.keys", api_name)
    # update cnt.txt file
    with open(filename, "w") as f:
        f.write(str(counter))
        f.close()

if __name__ =="__main__":
    main()

