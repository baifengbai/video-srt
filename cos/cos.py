# -*- coding: utf-8 -*-
import subprocess

class Cos:
    #上传文件到cos
    def upload_file(tmpAudio):
        objectName = tmpAudio.split('/')[-1]
        ret = subprocess.run(['coscmd', '-s', 'upload', tmpAudio, objectName], shell=False)
        if ret.returncode != 0:
            print("error:", ret)
