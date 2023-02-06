import os
import zipfile
from dotenv import load_dotenv
load_dotenv("C:\\Users\\User\\PycharmProjects\\Files\\.env")


class Col:

    def compress(self, file_names):

        path = "C:\\Users\\User\\PycharmProjects\\Files\\tools\\numbers\\"
        compression = zipfile.ZIP_DEFLATED

        zf = zipfile.ZipFile("new file.zip", mode="w")
        try:
            for file_name in file_names:
                # Add file to the zip file
                # first parameter file to zip, second filename in zip
                zf.write(path + file_name, file_name, compress_type=compression)

        except FileNotFoundError as e:
            print(e)
        finally:
            zf.close()
        return True
