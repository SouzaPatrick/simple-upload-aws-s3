# -*- coding: utf-8 -*-

from upload_s3 import UploadS3


dataFile = {
        "file_name": "aula-5-módulo-9-tolerância-geométrica-de-orientação.mp4",
        "base_output_s3": "googleads",
    }


BASE_FOLDER = '/tmp/convert/'
BACKET_NAME = 'adgroup.files'


#Local de saída do arquivo no s3
dataFile['output'] = '{0}/'.format(dataFile['base_output_s3'])
del dataFile['base_output_s3']

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
    



    