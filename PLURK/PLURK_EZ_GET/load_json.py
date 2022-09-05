import json

from pathlib import Path

basedir = Path("faces")

def func(fname):
    if not fname.endswith(".json"):
        fname += ".json"
    with open(f"{basedir/fname}", "r") as f:
        ret = json.load(f)
        f.close()
    return ret

class G:
    def __init__(self):
        import pickle
        with open("face_list.pkl", "rb") as f:
            self.ret = pickle.load(f)
            f.close()

    def get_fname(self,idx):
        fname =  self.ret[idx][1]
        print(fname)
        return fname


if __name__ == "__main__":
    import sys
    #recv = [func(ele) for ele in sys.argv[1:]]
    g = G()
    recv = [func(g.get_fname(int(ele))) for ele in sys.argv[1:]]
    for ele in recv:
        print("length: %d" % len(ele))
        if len(ele) < 10:
            print(ele)
        else:
            print(ele[:10])


