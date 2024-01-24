# coding = utf-8
import os
import cv2
import tkinter as tk
import datetime
import requests
import random
from hashlib import md5
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from paddleocr import PaddleOCR
import traceback
from tqdm import tqdm

root = tk.Tk()
root.title('Subtitle Translation Tool', )
root.geometry('400x300')

appid = []
appkey = []
video_path = []

tk.Label(root, text='智能外文字幕翻译合成工具', font='./font/HarmonyOS_Sans_SC_Regular.ttf').pack()

# 第一行框架：app_id 输入框
frame1 = tk.Frame(root)
frame1.pack(padx=10, pady=15)
label1 = tk.Label(frame1, text="百度翻译API编号:", font="./font/HarmonyOS_Sans_SC_Regular.ttf")
label1.pack(side="left")
entry1 = tk.Entry(frame1)
entry1.pack(side="left")

# 第二行框架：secret_key 输入框
frame2 = tk.Frame(root)
frame2.pack(padx=10, pady=15)
label2 = tk.Label(frame2, text="百度翻译API密钥:", font="./font/HarmonyOS_Sans_SC_Regular.ttf")
label2.pack(side="left")
entry2 = tk.Entry(frame2)
entry2.pack(side="left")

# 第三行框架：视频文件输入框
frame3 = tk.Frame(root)
frame3.pack(padx=10, pady=15)
label3 = tk.Label(frame3, text="视频文件绝对路径:", font="./font/HarmonyOS_Sans_SC_Regular.ttf")
label3.pack(side="left")
entry3 = tk.Entry(frame3)
entry3.pack(side="left")


# 按钮互动
def close_window():
    appid.append(entry1.get())
    appkey.append(entry2.get())
    video_path.append(entry3.get())
    root.destroy()
    print(appid, appkey, video_path)


def open_license():
    license_path = r'C:\Users\23581\PycharmProjects\paddle\subtitle_translation\readme_img\LICENSE.txt'
    os.startfile(license_path)


# 第四行按钮：enter
frame4 = tk.Frame(root)
frame4.pack(padx=10, pady=10)
button1 = tk.Button(frame4, text="确定", font="./font/HarmonyOS_Sans_SC_Regular.ttf", command=close_window)
button1.pack(side=tk.LEFT, padx=10)
button2 = tk.Button(frame4, text="开源协议", font="./font/HarmonyOS_Sans_SC_Regular.ttf", command=open_license)
button2.pack(side=tk.RIGHT, padx=10)

# 底栏Copyright
label4 = tk.Label(root, text=f"Powered By PaddleOCR & OpenCV   Version : 1.0.0",
                  font=("./font/HarmonyOS_Sans_SC_Regular.ttf", 10))
label4.pack(side=tk.BOTTOM)
label5 = tk.Label(root, text=f"Designed By JXX {datetime.datetime.now().strftime('%Y')}",
                  font=("./font/HarmonyOS_Sans_SC_Regular.ttf", 10))
label5.pack(side=tk.BOTTOM)

root.mainloop()


class SubtitleTranslation:
    def __init__(self):
        self.appid = appid[0]
        self.secret_key = appkey[0]
        self.movie_path = video_path[0]

    def read_movie(self):
        if self.movie_path == '':
            print("视频文件绝对路径为空,将退出程序!")
            exit(0)
        movie_path = self.movie_path
        img = []
        video = cv2.VideoCapture(movie_path)
        if video.isOpened():
            time = 15  # 采样间隔，每隔timeF帧提取一张图片
            count = 1
            for _ in tqdm(range(int(video.get(cv2.CAP_PROP_FRAME_COUNT)))):
                success, frame = video.read()
                if count % time == 0:
                    img.append(frame)
                count += 1
                cv2.waitKey(1)
            video.release()
            print("movie open ok !")
            return img
        else:
            print(f"movie open error\n{traceback.print_exc()}")
            exit(0)

    def movie_to_text(self):
        if self.movie_path == '':
            print("视频文件绝对路径为空,将退出程序!")
            exit(0)
        imgs = SubtitleTranslation.read_movie(self)
        for img in tqdm(list(imgs), desc="识别进度", unit="帧"):
            cv2.imwrite('./infer/infer.jpg', img)
            img_content = './infer/infer.jpg'
            ocr = PaddleOCR(use_angle_cls=True,
                            lang="ch")  # need to run only once to download and load model into memory
            result = ocr.ocr(img_content, cls=True)
            # 显示结果
            result = result[0]
            try:
                txts = [line[1][0] for line in result]
            except TypeError as err:
                continue
            with open('./infer/result.txt', 'a') as f:
                for txt in txts:
                    f.write(f"{txt}\n")
                f.close()

    def translate_text(self):
        if self.appid == '':
            print("百度翻译API编号为空,将退出程序!")
            exit(0)
        elif self.secret_key == '':
            print("百度翻译API秘钥为空,将退出程序!")
            exit(0)
        #  Set your own appid/appkey.
        appid = self.appid
        appkey = self.secret_key
        # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
        from_lang = 'en'
        to_lang = 'zh'
        endpoint = 'http://api.fanyi.baidu.com'
        path = '/api/trans/vip/translate'
        url = endpoint + path

        # Generate salt and sign
        def make_md5(s, encoding='utf-8'):
            return md5(s.encode(encoding)).hexdigest()

        lines = open('./infer/result.txt', 'r').readlines()
        num = 1
        for line in lines:
            query = line
            print(f"正在翻译第{num}行,共{len(lines)}行")
            salt = random.randint(32768, 65536)
            sign = make_md5(appid + query + str(salt) + appkey)
            # Build request
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
            # Send request
            r = requests.post(url, params=payload, headers=headers)
            result = r.json()
            trans = result['trans_result'][0]['dst']
            with open('./translate/trans.txt', 'a') as f:
                f.write(f"{trans}\n")
                f.close()
            num += 1
        appid.pop()
        appkey.pop()

    def add_text_subtitles(self):
        try:
            if self.movie_path == '':
                print("视频文件绝对路径为空,将退出程序!")
                exit(0)
            input_video = self.movie_path
            output_video = './output_video.mp4'
            subtitle_file = './translate/trans.txt'
            video = VideoFileClip(input_video)
            subtitles = []

            with open(subtitle_file, 'r', encoding='gbk') as file:
                subtitle_lines = file.readlines()
                for idx, line in enumerate(subtitle_lines):
                    text_clip = TextClip(line, fontsize=10, color='white', size=(video.w, None)).set_position(
                        'bottom').set_duration(0.5)
                    subtitles.append(text_clip.set_start(0.5 * idx))

            composed_subtitles = CompositeVideoClip(subtitles).set_duration(video.duration)
            final = CompositeVideoClip([video, composed_subtitles])
            final.write_videofile(output_video, codec='libx264', fps=video.fps)
            video_path.pop()
            return {'code': 1000, 'msg': '视频输出完毕!'}
        except Exception as err:
            video_path.pop()
            return {'code': 2333, 'msg': str(err)}

    def exit_program(self):
        if self.add_text_subtitles()['code'] == 1000:
            exit(0)
        elif self.add_text_subtitles()['code'] == 2333:
            print("遇到错误:\n" + self.add_text_subtitles()['msg'])


if __name__ == '__main__':
    st = SubtitleTranslation()
    st.movie_to_text()
    st.translate_text()
    st.add_text_subtitles()
    st.exit_program()
