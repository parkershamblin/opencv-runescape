import os


def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open("neg.txt", "w") as f:
        # loop over all the filenames
        for filename in os.listdir("negative"):
            f.write("negative/" + filename + "\n")


def train_cascade_classifier(
    trainPath="C:/Users/Parker/OneDrive - University of South Florida/Documents/GitHub/opencv/build/x64/vc15/bin/opencv_traincascade.exe",
    cascadeFolderPath="cascade/",
    vec="pos.vec",
    bg="neg.txt",
    w=24,
    h=24,
    precalcValBufSize=6000,
    precalcIdxBufSize=6000,
    numPos=40,
    numNeg=200,
    numStages=12,
    maxFalseAlarmRate=0.1,
    minHitRate=0.999,
):
    import random
    import subprocess
    n = random.randint(0, 1000)
    os.mkdir(f"cascade{n}/")
    subprocess.run(f"\"C:/Users/Parker/OneDrive - University of South Florida/Documents/GitHub/opencv/build/x64/vc15/bin/opencv_traincascade.exe\" -data cascade{n}/ -vec pos.vec -bg neg.txt  -w 24 -h 24 -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 40 -numNeg 200 -numStages 12 -maxFalseAlarmRate 0.1 -minHitRate 0.999")

