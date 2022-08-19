# -*- coding: utf-8 -*-
import subprocess

class Ffmpeg:
    #提取视频音频
    def extract_audio(video, tmpAudio):
        ret = subprocess.run('ffmpeg -version', shell=True)
        if ret.returncode != 0:
            print("请先安装 ffmpeg 依赖 ，并设置环境变量")
            return
        ret = subprocess.run(['ffmpeg', '-i', video, '-vn', '-ar', "16000", tmpAudio], shell=False)
        if ret.returncode != 0:
            print("error:", ret)

