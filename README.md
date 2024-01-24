# ����PaddleOCR����Ļ���빤��</h1>
<p align="center">
<p align="left">
    <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache%202-dfd.svg" alt="jpg"></a>
    <a href=""><img src="https://img.shields.io/badge/Release-1.0.0-ffa.svg" alt="jpg"></a>
    <a href=""><img src="https://img.shields.io/badge/Python-3.8.18-aff.svg" alt="jpg"></a>
    <a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Windows%2C%20MacOS-pink.svg" alt="jpg"></a>
</p>

## PaddleOCR ���

PaddleOCRּ�ڴ���һ�׷ḻ�����ȡ���ʵ�õ�OCR���߿⣬����������ѵ�������õ�ģ�ͣ���Ӧ����ء�</p>

> ����һЩPaddle�ٷ���Ȥ������:
> - <a href="https://gitee.com/paddlepaddle/PaddleOCR/blob/release/2.6/doc/doc_ch/ppocr_introduction.md">PP-OCR �ı����ʶ��</a>
> - <a href="https://gitee.com/paddlepaddle/PaddleOCR/blob/release/2.6/ppstructure/README_ch.md">PP-Structure �ĵ�����</a>
> - <a href="https://gitee.com/paddlepaddle/PaddleOCR/blob/release/2.6/doc/doc_ch/algorithm_overview.md">ǰ���㷨��ģ��</a>
> - <a href="https://gitee.com/paddlepaddle/PaddleOCR/tree/release/2.6/applications">���ֳ���Ӧ��</a>

�ٷ�ʾ��:

<img src="./readme_img/test_add_91.jpg" width="1792" alt="jpg">

<img src="./readme_img/00006737.jpg" width="1792" alt="jpg">

> �������ݿ��Բο�<a href="https://gitee.com/paddlepaddle/PaddleOCR?_from=gitee_search#-%E6%96%87%E6%A1%A3%E6%95%99%E7%A8%8B">�ٷ��ĵ�</a>

## ������

���������Ҫʹ����PaddleOCR��ͼƬ�ı�����ʶ���ܡ�<br>
ͨ������Opencv����Ƶ����֡����```read()```���������Ƶ���м����֡����һ���ظ�����̨��PaddleOCR�ӿ���̨�յ�֡ͼƬ���䱣��
```imwrite()```��```jpg```ͼƬ����ȡͼƬ��Ϣ���ʶ��ͼƬ�ڵ���Ļ������Ļд���ĵ����ٶȷ���API���з��롣<br>
�ڵ��ðٶȷ���API�󽫷�����д���ĵ�������```moviepy```�������Ƶ�ϳɣ����������Ļ���ض�֡д�뵽����ײ������Դ��Ƶ���桢��
���ϳ�����Ƶ���ﵽĿ�ꡣ

## ���ٿ�ʼ

### 1. ���л����

#### 1.1 ����Ҫ��

- ��<strong><font color='#0073EB'>CPU</font></strong>�İ�װ paddlepaddle >= 2.1.2
- ��<strong><font color='#2ecf44'>GPU</font></strong>�İ�װ paddlepaddle-gpu >= 2.5.1
- 3.8 <= Python <= 3.12
- CUDA >= 11.2
- cuDNN >= 8.2.1
- TensorRT >= 8.2.4.2 (��Ҫ��װ)

#### 1.2 ������װ

##### 1.2.1 ��װpaddlepaddle

> MacOS <font color="red">��ֻ֧��</font>ʹ��paddlepaddle��
  - ʹ����������ȷ�����```Python```�� 3.8/3.9/3.10/3.11/3.12��
    ``` shell
    python --version
    ```
  - ��Ҫȷ��```pip```�İ汾�Ƿ�����Ҫ��Ҫ��```pip```�汾Ϊ 20.2.2 ����߰汾��
    ```shell
    python -m pip --version
    ```
  - ��Ҫȷ��```Python```��```pip```�� 64bit�����Ҵ������ܹ��� x86_64������� x64��Intel 64��AMD64���ܹ�������ĵ�һ��������ǡ�64bit�����ڶ���������ǡ�x86_64������x64����AMD64�����ɣ�
    ```shell
    python -c "import platform;print(platform.architecture()[0]);print(platform.machine())"
    ```
  - Ĭ���ṩ�İ�װ����Ҫ�����֧��```MKL```,Windows �ݲ�֧��```NCCL```���ֲ�ʽ����ع��ܡ�
  - ����ʹ��```pip```���а�װ��
    ```shell
    python -m pip install paddlepaddle==2.6.0 -i https://mirror.baidu.com/pypi/simple
    ```
  - ��֤��װ
    - ��װ��ɺ���Խ���```Python```ʹ������������Ƿ�װ�ɹ���
      ```python
      import paddle
      paddle.utils.run_check()
      ```
    - ���г���```PaddlePaddle is installed successfully!```�����װ�ɹ���
  - ж�ط���
    - ʹ���������ж��paddlepaddle��
      ```shell
      python -m pip uninstall paddlepaddle
      ```
<br>

##### 1.2.2 ��װpaddlepaddle-gpu

> MacOS <font color="red">��ֻ֧��</font>ʹ��paddlepaddle��
  - ʹ����������ȷ�����```Python```�� 3.8/3.9/3.10/3.11/3.12��
    ``` shell
    python --version
    ```
  - ��Ҫȷ��```pip```�İ汾�Ƿ�����Ҫ��Ҫ��```pip```�汾Ϊ 20.2.2 ����߰汾��
    ```shell
    python -m pip --version
    ```
  - ��Ҫȷ��```Python```��```pip```�� 64bit�����Ҵ������ܹ��� x86_64������� x64��Intel 64��AMD64���ܹ�������ĵ�һ��������ǡ�64bit�����ڶ���������ǡ�x86_64������x64����AMD64�����ɣ�
    ```shell
    python -c "import platform;print(platform.architecture()[0]);print(platform.machine())"
    ```
  - Ĭ���ṩ�İ�װ����Ҫ�����֧��```MKL```,Windows �ݲ�֧��```NCCL```���ֲ�ʽ����ع��ܡ�
  - �����GPU���豸����Ҫȷ��Ӳ���汾һһ��Ӧ�����ｨ��ʹ��CUDA 11.6��Ϊ�Ƚ��ȶ�����Ӧ����cuDNN 8.4.0������Ҫ����������Ҫ��װTensorRT 8.4.0.6������Ҳ����paddle�ٷ��İ汾��Ӧ���������GPU ������������ 3.5 ��Ӳ���豸��

    |         CUDA�汾         | cuDNN�汾 |  TensorRT�汾  |
    |:----------------------:|:-------:|:------------:|
    |          11.2          |  8.2.1  |   8.2.4.2    |
    |          11.6          |  8.4.0  |   8.4.0.6    |
    |          11.7          |  8.4.1  |   8.4.2.4    |
    |          11.8          |  8.6.0  |   8.5.1.7    |
    |          12.0          |  8.9.1  |   8.6.1.6    |
    > ע��Ŀǰ�ٷ������� windows ��װ�������� CUDA 11.2/11.6/11.7/11.8/12.0������ʹ������ cuda �汾����ͨ��Դ�����б��롣���ɲο� NVIDIA �ٷ��ĵ��˽� CUDA��CUDNN �� TensorRT �İ�װ���̺����÷��������<a href="https://docs.nvidia.com/cuda/cuda-installation-guide-linux/">CUDA</a>��<a href="https://docs.nvidia.com/deeplearning/sdk/cudnn-install/">cuDNN</a>��<a href="https://developer.nvidia.com/tensorrt">TensorRT</a>��
  - ��Բ�ͬ�汾��CUDAʹ��```pip```���а�װ:
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
  - ��֤��װ
    - ��װ��ɺ���Խ���```Python```ʹ������������Ƿ�װ�ɹ���
      ```python
      import paddle
      paddle.utils.run_check()
      ```
    - ���г���```PaddlePaddle is installed successfully!```�����װ�ɹ���
  - ж�ط���
    - ʹ���������ж��paddlepaddle-gpu��
      ```shell
      python -m pip uninstall paddlepaddle-gpu
      ```

### 2. �����ⰲװ

- ʹ��```Python```�������´��밲װ������
  ```shell
  python -m pip install -r requirement.txt
  ```

### 3. ���빦��ʵ��

- ����Ϊ�˷���Ͳ�ʹ�÷ɽ���paddlenlp�ˣ�ͬʱΪ�˼����������ֱ�ӵ��ðٶȷ��뿪��ƽ̨��API��ÿ��ÿ����߿���ӵ��100���ַ�����Ѷ�ȣ�һ�㹻���ˡ�
- ��¼<a href="https://fanyi-api.baidu.com/">�ٶȷ��뿪��ƽ̨</a>��ȷ���Ѿ�ʵ����֤����ѿ�ͨ<a href="https://fanyi-api.baidu.com/product/11">ͨ���ı�����</a>����
- ��֮ͨ�����<a href="https://fanyi-api.baidu.com/api/trans/product/desktop">�������̨</a>����ҳ��׶˿��Կ����Լ���������Ϣ������:
    > <strong><font color="#0073EB">|</font> ������Ϣ</strong><br>
      APP ID: 2024XXXXXXXX<br>
      ��Կ: XXXXXXXXXXXX
- ����ֱ�Ӹ��ϰٶȹٷ��ṩ��API����```Python```���룬�����������ʹ�����滻�����е�```appid```��```appkey```Ϊ�Լ�����Ϣ��
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

- ���н������:
  ```
  {
    "from": "en",
    "to": "zh",
    "trans_result": [
        {
            "src": "Hello World! This is 1st paragraph.",
            "dst": "��ã����磡���ǵ�һ�Ρ�"
        },
        {
            "src": "This is 2nd paragraph.",
            "dst": "���ǵ�2�Ρ�"
        }
    ]
  }
  ```
  
- ���������н��Ҳ�������Ϳ����ˡ�

### 4. ��������

#### 4.1 ���

- ������ͼ����:
  ```
  `---subtitle_translation
      |
      `---font
      |   |---HarmonyOS_Sans_SC_Regular.ttf  // ��������
      |
      `---infer
      |   |---infer.jpg                      // ����ͼƬ
      |   |---result.txt                     // �����ı�
      |
      `---translate
      |   |---trans.txt                      // �����ı�
      |
      `---readme_img
      |   |---00006737.jpg
      |   |---test_add_91.jpg
      |
      |---input.mp4                          // ������Ƶ
      |---output_video.mp4                   // �����Ƶ
      |---main.py                            // ������
      |---LICENSE
      |---README.md
  ```

- ������ͼ����:
  ```
  `---SubtitleTranslation
      |
      `---read_movie          // ��ȡ��Ƶ
      |
      `---movie_to_text       // ���ʶ���ı�
      |
      `---translate_text      // �����ı�
      |
      `---add_text_subtitles  // �����Ļ
  ```

#### 4.2 ����

1. ִ������Ĵ������г���:
   ```shell
   python main.py
   ```
2. �����Լ��ٶȷ��뿪��ƽ̨��```appid```,```appkey```�Լ��Լ�׼���õ���Ƶ�ĵ�ַ�����ȷ���ȴ����н������ɡ�

### 5. ���п�������������

1. ������```PaddleOCR```ʱ���ܻ���ʾ```cannot load cuDNN_cnn_infer64_8.dll.  Error code 193```��������������㰲װ��CUDA��cuDNN�İ汾���ߵ��µģ�
��ȷ�����CUDA��cuDNN��װ�İ汾�Ƿ��Ӧ��������Ǳ�����Խ���cuDNN�İ汾�������°�װ����ΪcuDNN�������в��ȶ���
2. ������```moviepy```ʱ���ܻ���������:
   ```
   OSError: MoviePy Error: creation of None failed because of the following error:
   [WinError 2] ϵͳ�Ҳ���ָ�����ļ�. . .
   This error can be due to the fact that ImageMagick is not installed on your computer, or (for Windows users) that you didn't specify the path to the ImageMagick binary in file conf.py, or that the path you specified is incorrect
   ```
   ��������```moviepy```��ȱ��```ImageMagick```ģ�鵼�µģ����Ե�<a href="https://www.imagemagick.org/script/download.php/#windows">ImageMagick����</a>����```ImageMagick```��
   �ڰ�װʱע��Ҫ��ѡ```Install development headers and libraries for C and C++```ѡ���װ������```MAGICK_HOME```����������ֵΪ```ImageMagick```�İ�װ·����������װ·������ϵͳ����```path```��
   ��װ�ɹ�֮���޸�```moviepy```ģ���µ�```config_defaults.py```�ļ����޸ĺ����������:
   ```python
   FFMPEG_BINARY = os.getenv('FFMPEG_BINARY', 'ffmpeg-imageio')
   # IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')
   # �޸�Ϊ�ո�ImageMagic�İ�װ·��
   IMAGEMAGICK_BINARY = r"D:\�㰲װImageMagick���ļ���\magick.exe"
   ```
   ���в�����ĵط����Կ�<a href='https://blog.csdn.net/weixin_42081389/article/details/104322629'>ԭ��</a>����������ο���CSDN��һ�����������¡�