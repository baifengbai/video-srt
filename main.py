import os
import sys

from common.logger import logger
from tencent.config import Config
from ffmpeg.ffmpeg import Ffmpeg
from cos.cos import Cos
from tencent.tencent_cli import new_audio_file
from tool.to_srt import to_srt,make_srt
def main():
    if len(sys.argv) < 1:
        logger.info('enter the video path:')
        logger.info('python main.py [video_path]')
        sys.exit(0)
    video_path = sys.argv[1]
    tmpAudio = Config.OUTPUT_PATH + video_path.split("/")[-1].split(".")[0] + ".wav"
    Ffmpeg.extract_audio(video_path, tmpAudio)
    Cos.upload_file(tmpAudio)
    objectName = tmpAudio.split('/')[-1]
    audio_url = "https://asr-****-****-**********.cos.ap-shanghai.myqcloud.com/" + objectName
    src_txt = new_audio_file("16k_zh", audio_url)
    srt_txt = to_srt(src_txt)
    file_name = Config.OUTPUT_PATH + video_path.split("/")[-1].split(".")[0] + ".srt"
    make_srt(srt_txt, file_name)

if __name__ == '__main__':
    main()
