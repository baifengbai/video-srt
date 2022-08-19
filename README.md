1.字幕视频自动生成字幕

该项目通过使用腾讯云AI录音文件识别让无字幕视频自动生成字幕

2.依赖

(1)需下载安装ffmpeg，并设置环境变量

(2)借助腾讯云COS获取音频URL，需在本下载并安装COSCMD工具

  链接为：https://cloud.tencent.com/document/product/436/10976

(3)使用腾讯云ASR录音文件识别服务
  
  链接为：https://cloud.tencent.com/document/product/1093/37822
  
3.执行脚本

python main 录音文件

例：
python main.py audio/test.mov

