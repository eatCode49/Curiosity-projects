import os, shutil

# Getting files from the directory
path = r"C:\Users\user\Downloads"
files = os.listdir(path)

# Image functions start form here
extensionofImage = ["jpg", "png", "jpeg", "gif", "bmp", "tiff", "tif", "webp", "heif", "heic", "psd", "raw", "ico", "exr", "dds", "tga", "ai", "svg"]

def images(path):
    if os.path.exists(f"{path}/image"):
        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:].lower()

            if os.path.isdir(f"{path}/{extension}"):
                continue

            if extension not in extensionofImage:
                continue
            
            if not os.path.exists(f"{path}/image/{extension}"):
                os.makedirs(f"{path}/image/{extension}")

            for imext in extensionofImage:
                if extension == imext:
                    if os.path.exists(f"{path}/image/{extension}"):
                        if os.path.exists(f"{path}/image/{extension}/{file}"):
                            continue
                        shutil.move(f"{path}/{file}", f"{path}/image/{extension}")
    else:
        os.mkdir(f"{path}/image")
        for file in files:
            filename, extension = os.path.splitext(file)
            extension  = extension[1:]

            if os.path.exists(f"{path}/{extension}/{file}"):
                continue

            for imext in extensionofImage:
                if imext == extension:
                    if os.path.exists(f"{path}/image/{extension}"):
                        if os.path.exists(f"{path}/image/{extension}/{file}"):
                            continue
                        shutil.move(f"{path}/{file}", f"{path}/image/{extension}")
                    else:
                        os.mkdir(f"{path}/image/{extension}")
                        shutil.move(f"{path}/{file}", f"{path}/image/{extension}")
# Image function stops here


def external_dir(path):
    files = os.listdir(path)
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.isdir(f"{path}/{extension}"):
            pass

        if os.path.exists(f"{path}/{extension}/{file}"):
            continue

        if os.path.exists(f"{path}/{extension}"):
            shutil.move(f"{path}/{file}", f"{path}/{extension}")
        else:
            os.mkdir(f"{path}/{extension}")
            shutil.move(f"{path}/{file}", f"{path}/{extension}")

images(path)
external_dir(path)