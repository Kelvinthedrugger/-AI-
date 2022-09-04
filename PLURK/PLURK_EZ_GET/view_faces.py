import pickle

# load the file
with open("face_list.pkl", "rb") as f:
    fs = pickle.load(f)
    f.close()

# user input: input the indices in cmd
import sys
print(sys.argv[1:])
for idx in list(map(int, sys.argv[1:])):
    print(f"{idx}: {fs[idx]}")

