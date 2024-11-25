# 说明
弹幕姬的插件[RE-TTSCat](https://github.com/Elepover/RE-TTSCat)中大部份tts都失效了、之前找到的[re-ttscat-edge-tts-server](https://github.com/ganlvtech/re-ttscat-edge-tts-server)项目又报错、遂自己写了一个基于[edge-tts](https://github.com/rany2/edge-tts)的服务、提供get的http请求用于弹幕姬读出弹幕使用。

# 使用方法
1. 去Releases下载最新的edge-tts-api.exe
2. 启动edge-tts-api.exe
3. 在弹幕姬RE-TTSCat中自定义TTS引擎URL填入 `http://127.0.0.1:5000/tts?text=$TTSTEXT&voice=zh-CN-XiaoxiaoNeural`
4. 参数说明:

    text : 需要转换的文本内容

    voice : TTS引擎语音包、可以参照[这里](https://github.com/rany2/edge-tts/tree/master?tab=readme-ov-file#changing-the-voice)

# 安装依赖
```bash
pip install Flask[async]
```
```bash
pip install edge-tts
```