import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:

                local_path = os.path.join(root, filename)

                relative_path  = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
def main():
    access_token = 'sl.BDZ0raydEbNp0DlswFfWvD2ayopWZyj7wCxKNCI8_PdwehWoRjUDdHK1L8_HCCxy1G9XVURtcO7oI_FkhIhknytq3bZ3S6nC-8HuiFMAjjiVUIA9wgItfktlitepoPPFL_l_v9U  '
    transferData = TransferData(access_token)

    file_from = str(input("Enter the source destination: "))
    file_to = input("Enter the entire file path: ")  # The full path to upload the file to, including the file name

    transferData.upload_file(file_from, file_to)
    print("Files has been uploaded")

main()