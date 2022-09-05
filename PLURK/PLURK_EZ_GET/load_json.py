import json

from pathlib import Path

basedir = Path("faces")

def func(fname):
    if not fname.endswith(".json"):
        fname += ".json"
    nn = basedir/fname
    if not nn.is_file():
        return None
    with open(f"{nn}", "r") as f:
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
        #print(fname)
        return fname


if __name__ == "__main__":
    import sys
    #recv = [func(ele) for ele in sys.argv[1:]]
    g = G()
    recv = [func(g.get_fname(int(ele))) for ele in sys.argv[1:]]
    for ele, fname in zip(recv, sys.argv[1:]):
        print(g.ret[int(fname)][1])
        if ele is None:
            print(ele)
        elif len(ele) < 5:
            print("length: %d" % len(ele))
            print(ele)
        else:
            print("length: %d" % len(ele))
            print(ele[:5])

