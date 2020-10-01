# -*- coding: utf-8 -*-

from upload_s3 import UploadS3


BASE_FOLDER = '/folder/base'
BACKET_NAME = 'bucket_name'
BASE_OUTPUT_S3 = "key_file"

dataFile = {}

#Local de saída do arquivo no s3
dataFile['output'] = '{0}/'.format(BASE_OUTPUT_S3)

#Local dos certificados na sua maquina
dataFile['output_local'] = BASE_FOLDER

#Add nome do bucket
dataFile ['bucket_name'] = BACKET_NAME



print('\n\n\n #######-> UPLOAD')
output = dataFile['output']
output_local = dataFile['output_local']
bucket = dataFile['bucket_name']

_uploadS3 = UploadS3(destinationFolder=output, pathFileConvert=output_local, bucketName=bucket)
_uploadS3.upload_files()
    



    
