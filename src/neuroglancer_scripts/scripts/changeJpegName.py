import os
import sys

# root = 'D:\WorkSpace\otherWorkSpace\\neuroglancer-scripts\src\\neuroglancer_scripts\scripts\jpeg'
#root = '/home/leinao/install/neuroglancer-scripts/src/neuroglancer_scripts/scripts/jpeg/'

root = sys.argv[1]
print(sys.argv[1])

print(os.listdir(root))

# for folder in os.listdir(root):
#     f = root + "\\" + folder
#     print(f)
#     for s1 in os.listdir(f):
#         f1 = f + "\\" + s1
#         print(f1)
#         for s2 in os.listdir(f1):
#             f2 = f1 + "\\" + s2
#             for s3 in os.listdir(f2):
#                 f3 = f2 + "\\" + s3
#                 ss = s1+"_" + s2 + "_" + s3
#                 # open(f + "\\" + ss, 'wb').write(open(f3, 'rb').read())
#                 os.symlink(f3, f + "\\" + ss)
#                 print(f + "\\" + ss)

for folder in os.listdir(root):
    f = root + "/" + folder
    print(f)
    for s1 in os.listdir(f):
        f1 = f + "/" + s1
        print(f1)
        for s2 in os.listdir(f1):
            f2 = f1 + "/" + s2
            for s3 in os.listdir(f2):
                f3 = f2 + "/" + s3
                ss = s1+"_" + s2 + "_" + s3
                # open(f + "/" + ss, 'wb').write(open(f3, 'rb').read())
                os.symlink(f3, f + "/" + ss)
                print(f + "/" + ss)
