# 基于PaddleOCR的字幕翻译工具</h1>
<p align="center">
<p align="left">
    <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache%202-dfd.svg" alt="jpg"></a>
    <a href=""><img src="https://img.shields.io/badge/Release-1.0.0-ffa.svg" alt="jpg"></a>
    <a href=""><img src="https://img.shields.io/badge/Python-3.8.18-aff.svg" alt="jpg"></a>
    <a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Windows%2C%20MacOS-pink.svg" alt="jpg"></a>
</p>

## PaddleOCR 简介

PaddleOCR旨在打造一套丰富、领先、且实用的OCR工具库，助力开发者训练出更好的模型，并应用落地。</p>

> 分享一些Paddle官方有趣的内容:
> - <a href="https://gitee.com/paddlepaddle/PaddleOCR/blob/release/2.6/doc/doc_ch/ppocr_introduction.md">PP-OCR 文本检测识别</a>
> - <a href="https://gitee.com/paddlepaddle/PaddleOCR/blob/release/2.6/ppstructure/README_ch.md">PP-Structure 文档分析</a>
> - <a href="https://gitee.com/paddlepaddle/PaddleOCR/blob/release/2.6/doc/doc_ch/algorithm_overview.md">前沿算法与模型</a>
> - <a href="https://gitee.com/paddlepaddle/PaddleOCR/tree/release/2.6/applications">部分场景应用</a>

官方示例:

<img src="./readme_img/test_add_91.jpg" width="1792" alt="jpg">

<img src="./readme_img/00006737.jpg" width="1792" alt="jpg">

> 更多内容可以参考<a href="https://gitee.com/paddlepaddle/PaddleOCR?_from=gitee_search#-%E6%96%87%E6%A1%A3%E6%95%99%E7%A8%8B">官方文档</a>

## 程序简介

这个程序主要使用了PaddleOCR的图片文本检测和识别功能。<br>
通过调用Opencv对视频的切帧能力```read()```将输入的视频进行间隔切帧并逐一返回给控制台，PaddleOCR从控制台收到帧图片后将其保存
```imwrite()```成```jpg```图片并读取图片信息检测识别图片内的字幕，将字幕写入文档供百度翻译API进行翻译。<br>
在调用百度翻译API后将翻译结果写入文档，利用```moviepy```库进行视频合成，将翻译的字幕按特定帧写入到画面底部并结合源视频画面、声
音合成新视频，达到目标。

## 快速开始

### 1. 运行环境搭建

#### 1.1 环境要求

- 用<strong><font color='#0073EB'>CPU</font></strong>的安装 paddlepaddle >= 2.1.2
- 用<strong><font color='#2ecf44'>GPU</font></strong>的安装 paddlepaddle-gpu >= 2.5.1
- 3.8 <= Python <= 3.12
- CUDA >= 11.2
- cuDNN >= 8.2.1
- TensorRT >= 8.2.4.2 (需要就装)

#### 1.2 环境安装

##### 1.2.1 安装paddlepaddle

> MacOS <font color="red">暂只支持</font>使用paddlepaddle。
  - 使用以下命令确认你的```Python```是 3.8/3.9/3.10/3.11/3.12。
    ``` shell
    python --version
    ```
  - 需要确认```pip```的版本是否满足要求，要求```pip```版本为 20.2.2 或更高版本。
    ```shell
    python -m pip --version
    ```
  - 需要确认```Python```和```pip```是 64bit，并且处理器架构是 x86_64（或称作 x64、Intel 64、AMD64）架构。下面的第一行输出的是”64bit”，第二行输出的是”x86_64”、”x64”或”AMD64”即可：
    ```shell
    python -c "import platform;print(platform.architecture()[0]);print(platform.machine())"
    ```
  - 默认提供的安装包需要计算机支持```MKL```,Windows 暂不支持```NCCL```，分布式等相关功能。
  - 下面使用```pip```进行安装。
    ```shell
    python -m pip install paddlepaddle==2.6.0 -i https://mirror.baidu.com/pypi/simple
    ```
  - 验证安装
    - 安装完成后可以进入```Python```使用以下语句检查是否安装成功。
      ```python
      import paddle
      paddle.utils.run_check()
      ```
    - 运行出现```PaddlePaddle is installed successfully!```则代表安装成功。
  - 卸载方法
    - 使用以下语句卸载paddlepaddle。
      ```shell
      python -m pip uninstall paddlepaddle
      ```
<br>

##### 1.2.2 安装paddlepaddle-gpu

> MacOS <font color="red">暂只支持</font>使用paddlepaddle。
  - 使用以下命令确认你的```Python```是 3.8/3.9/3.10/3.11/3.12。
    ``` shell
    python --version
    ```
  - 需要确认```pip```的版本是否满足要求，要求```pip```版本为 20.2.2 或更高版本。
    ```shell
    python -m pip --version
    ```
  - 需要确认```Python```和```pip```是 64bit，并且处理器架构是 x86_64（或称作 x64、Intel 64、AMD64）架构。下面的第一行输出的是”64bit”，第二行输出的是”x86_64”、”x64”或”AMD64”即可：
    ```shell
    python -c "import platform;print(platform.architecture()[0]);print(platform.machine())"
    ```
  - 默认提供的安装包需要计算机支持```MKL```,Windows 暂不支持```NCCL```，分布式等相关功能。
  - 针对有GPU的设备，需要确保硬件版本一一对应，这里建议使用CUDA 11.6因为比较稳定，对应的是cuDNN 8.4.0，如需要加速推理需要安装TensorRT 8.4.0.6，这里也给出paddle官方的版本对应表格，适用于GPU 运算能力超过 3.5 的硬件设备。

    |         CUDA版本         | cuDNN版本 |  TensorRT版本  |
    |:----------------------:|:-------:|:------------:|
    |          11.2          |  8.2.1  |   8.2.4.2    |
    |          11.6          |  8.4.0  |   8.4.0.6    |
    |          11.7          |  8.4.1  |   8.4.2.4    |
    |          11.8          |  8.6.0  |   8.5.1.7    |
    |          12.0          |  8.9.1  |   8.6.1.6    |
    > 注：目前官方发布的 windows 安装包仅包含 CUDA 11.2/11.6/11.7/11.8/12.0，如需使用其他 cuda 版本，请通过源码自行编译。您可参考 NVIDIA 官方文档了解 CUDA、CUDNN 和 TensorRT 的安装流程和配置方法，请见<a href="https://docs.nvidia.com/cuda/cuda-installation-guide-linux/">CUDA</a>，<a href="https://docs.nvidia.com/deeplearning/sdk/cudnn-install/">cuDNN</a>，<a href="https://developer.nvidia.com/tensorrt">TensorRT</a>。
  - 针对不同版本的CUDA使用```pip```进行安装:
    ```shell
    # CUDA 11.2
    python -m pip install paddlepaddle-gpu==2.6.0.post112 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
    ```
    ```shell
    # CUDA 11.6
    python -m pip install paddlepaddle-gpu==2.6.0.post116 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
    ```
    ```shell
    # CUDA 11.7
    python -m pip install paddlepaddle-gpu==2.6.0.post117 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
    ```
    ```shell
    # CUDA 11.8
    python -m pip install paddlepaddle-gpu==2.6.0 -i https://mirror.baidu.com/pypi/simple
    ```
    ```shell
    # CUDA 12.0
    python -m pip install paddlepaddle-gpu==2.6.0.post120 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
    ```
  - 验证安装
    - 安装完成后可以进入```Python```使用以下语句检查是否安装成功。
      ```python
      import paddle
      paddle.utils.run_check()
      ```
    - 运行出现```PaddlePaddle is installed successfully!```则代表安装成功。
  - 卸载方法
    - 使用以下语句卸载paddlepaddle-gpu。
      ```shell
      python -m pip uninstall paddlepaddle-gpu
      ```

### 2. 三方库安装

- 使用```Python```运行以下代码安装三方库
  ```shell
  python -m pip install -r requirement.txt
  ```

### 3. 翻译功能实现

- 这里为了方便就不使用飞桨的paddlenlp了，同时为了简便容易配置直接调用百度翻译开放平台的API，每人每月最高可以拥有100万字符的免费额度，一般够用了。
- 登录<a href="https://fanyi-api.baidu.com/">百度翻译开放平台</a>，确保已经实名认证，免费开通<a href="https://fanyi-api.baidu.com/product/11">通用文本翻译</a>服务。
- 开通之后进入<a href="https://fanyi-api.baidu.com/api/trans/product/desktop">管理控制台</a>，在页面底端可以看到自己的申请信息，例如:
    > <strong><font color="#0073EB">|</font> 申请信息</strong><br>
      APP ID: 2024XXXXXXXX<br>
      密钥: XXXXXXXXXXXX
- 下面直接附上百度官方提供的API调用```Python```代码，如果用作测试使用请替换代码中的```appid```和```appkey```为自己的信息。
  ```python
  # -*- coding: utf-8 -*-
  # This code shows an example of text translation from English to Simplified-Chinese.
  # This code runs on Python 2.7.x and Python 3.x.
  # You may install `requests` to run this code: pip install requests
  # Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

  import requests
  import random
  import json
  from hashlib import md5

  # Set your own appid/appkey.
  appid = 'INPUT_YOUR_APPID'
  appkey = 'INPUT_YOUR_APPKEY'

  # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
  from_lang = 'en'
  to_lang =  'zh'

  endpoint = 'http://api.fanyi.baidu.com'
  path = '/api/trans/vip/translate'
  url = endpoint + path

  query = 'Hello World! This is 1st paragraph.\nThis is 2nd paragraph.'

  # Generate salt and sign
  def make_md5(s, encoding='utf-8'):
      return md5(s.encode(encoding)).hexdigest()

  salt = random.randint(32768, 65536)
  sign = make_md5(appid + query + str(salt) + appkey)

  # Build request
  headers = {'Content-Type': 'application/x-www-form-urlencoded'}
  payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

  # Send request
  r = requests.post(url, params=payload, headers=headers)
  result = r.json()

  # Show response
  print(json.dumps(result, indent=4, ensure_ascii=False))
  ```

- 运行结果如下:
  ```
  {
    "from": "en",
    "to": "zh",
    "trans_result": [
        {
            "src": "Hello World! This is 1st paragraph.",
            "dst": "你好，世界！这是第一段。"
        },
        {
            "src": "This is 2nd paragraph.",
            "dst": "这是第2段。"
        }
    ]
  }
  ```
  
- 如果你的运行结果也是这样就可以了。

### 4. 程序运行

#### 4.1 框架

- 程序框架图如下:
  ```
  `---subtitle_translation
      |
      `---font
      |   |---HarmonyOS_Sans_SC_Regular.ttf  // 界面字体
      |
      `---infer
      |   |---infer.jpg                      // 推理图片
      |   |---result.txt                     // 推理文本
      |
      `---translate
      |   |---trans.txt                      // 翻译文本
      |
      `---readme_img
      |   |---00006737.jpg
      |   |---test_add_91.jpg
      |
      |---input.mp4                          // 输入视频
      |---output_video.mp4                   // 输出视频
      |---main.py                            // 主程序
      |---LICENSE
      |---README.md
  ```

- 代码框架图如下:
  ```
  `---SubtitleTranslation
      |
      `---read_movie          // 读取视频
      |
      `---movie_to_text       // 检测识别文本
      |
      `---translate_text      // 翻译文本
      |
      `---add_text_subtitles  // 添加字幕
  ```

#### 4.2 运行

1. 执行下面的代码运行程序:
   ```shell
   python main.py
   ```
2. 输入自己百度翻译开放平台的```appid```,```appkey```以及自己准备好的视频的地址，点击确定等待运行结束即可。

### 5. 运行可能遇到的问题

1. 当运行```PaddleOCR```时可能会提示```cannot load cuDNN_cnn_infer64_8.dll.  Error code 193```，这可能是由于你安装的CUDA、cuDNN的版本过高导致的，
请确认你的CUDA和cuDNN安装的版本是否对应，如果还是报错可以降低cuDNN的版本进行重新安装，因为cuDNN可能运行不稳定。
2. 当运行```moviepy```时可能会遇到报错:
   ```
   OSError: MoviePy Error: creation of None failed because of the following error:
   [WinError 2] 系统找不到指定的文件. . .
   This error can be due to the fact that ImageMagick is not installed on your computer, or (for Windows users) that you didn't specify the path to the ImageMagick binary in file conf.py, or that the path you specified is incorrect
   ```
   这是由于```moviepy```库缺少```ImageMagick```模块导致的，可以到<a href="https://www.imagemagick.org/script/download.php/#windows">ImageMagick官网</a>下载```ImageMagick```，
   在安装时注意要勾选```Install development headers and libraries for C and C++```选项，安装后设置```MAGICK_HOME```环境变量，值为```ImageMagick```的安装路径，并将安装路径加入系统变量```path```。
   安装成功之后，修改```moviepy```模块下的```config_defaults.py```文件，修改后的内容如下:
   ```python
   FFMPEG_BINARY = os.getenv('FFMPEG_BINARY', 'ffmpeg-imageio')
   # IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')
   # 修改为刚刚ImageMagic的安装路径
   IMAGEMAGICK_BINARY = r"D:\你安装ImageMagick的文件夹\magick.exe"
   ```
   如有不清楚的地方可以看<a href='https://blog.csdn.net/weixin_42081389/article/details/104322629'>原文</a>，这个方法参考了CSDN上一个博主的文章。