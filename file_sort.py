import os, shutil

fromdir = "C:/Users/azanz/OneDrive/Desktop/image_files"
# os.mkdir("C:/Users/azanz/OneDrive/Desktop/images")
todir = "C:/Users/azanz/OneDrive/Desktop/images"
listoffiles = os.listdir(fromdir)
print(listoffiles)

for filename in listoffiles:
    root, ext = os.path.splitext(filename)
    # print(root, ext)
    if ext == "":
        continue
    if ext in [".gif", ".png", ".jfif", ".jpg", ".pdf"]:
        path1 = fromdir + "/" + filename
        path2 = todir + "/" + "image_files"
        path3 = todir + "/" + "image_files" + "/" + filename
        # print(path1)
        # print(path3)

        if os.path.exists(path2):
            print("moving", filename)
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("moving", filename)
            shutil.move(path1, path3)