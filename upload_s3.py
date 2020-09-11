import boto3
import os
import progressbar

class UploadS3:
    def __init__(self, destinationFolder, pathFileConvert, bucketName):
        self.output = destinationFolder
        self.input_file = pathFileConvert
        self._S3 = boto3.resource('s3')
        self.bucket = bucketName

    def upload_files(self):
        files = os.listdir(self.input_file)
        
        with progressbar.ProgressBar(max_value=len(files)) as bar:
            for indice, file in enumerate(files):
                pathFile = self.input_file+file
                keyFile =  self.output + file
                self._S3.meta.client.upload_file(pathFile, self.bucket, keyFile)
                bar.update(indice+1)