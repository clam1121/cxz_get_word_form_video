import ffmpeg
import opencc
import requests
import hashlib
import time
import re
import os
import nltk
from funasr import AutoModel
from nltk.tokenize import sent_tokenize

# 配置参数
access_key = '2b17b479-8c9f-4229-ae41-039de55aba26'
access_secret = 'Bh0VmueQMWY_HTWn1@RVM2#j8wOY6EQB&9SPfpqm*tVIOAYx'
nonce = 'qwertyuiopasdfghjklzxcvbnm'
timestamp = str(int(time.time() * 1000))

# 拼接签名字符串
stringA = access_key + access_secret + nonce + timestamp
sign = hashlib.md5(stringA.encode('utf-8')).hexdigest()

# 请求头
headers = {
    'accessKey': access_key,
    'signature': sign,
    'timestamp': timestamp,
    'nonce': 'qwertyuiopasdfghjklzxcvbnm',
    'Content-Type': 'application/json'
}

api_url = "https://www.sh.smartedu.cn/wisdom-edu-resource-center/api-service/api/third/common/getEncryptUrl"

data = {
    "consumerId": "1691364333902364679",
    'url': '1'
}


video_file_path = r"D:\fdu\shanghaidianjiaoguan\get_words_from_video\video"
words_file_path = r"D:\fdu\shanghaidianjiaoguan\get_words_from_video\words"

def download_video(url, filename):
    print(url)
    try:
        # 发送HTTP GET请求
        response = requests.get(url,stream=True)

        # 检查请求是否成功
        if response.status_code == 200:
            # 打开一个文件来保存视频
            with open(filename, 'wb') as file:
                # 逐块写入视频数据
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            print(f"视频已成功下载并保存为 {filename}")
        else:
            print(f"下载失败，状态码：{response.status_code}")
            print(response)
    except requests.exceptions.RequestException as e:
        print(f"请求过程中出现错误：{e}")

def get_video_from_baseurl(basename, baseurl, video_file):
    data['url'] = baseurl[0:-1]
    print(data)
    response = requests.post(api_url, json=data, headers=headers)
    response_data = response.json()
    print(response_data)
    EncryptUrl = response_data['data']
    download_video(EncryptUrl, video_file + '\\' + 'temp')
    return EncryptUrl

def get_words_from_video(video_file, videoname, txt_file, EncryptUrl):
    # audio_path = video_file + '\\' + 'extracted_audio.wav'
    # video_path = video_file + '\\' + videoname + '.mp4'
    # txt_path = txt_file + '\\' + videoname[0: -2] + '.txt'

    audio_path = os.path.join(video_file, "extracted_audio.wav")
    video_path = os.path.join(video_file, "temp")
    print(video_path)
    txt_path = os.path.join(txt_file, videoname[0: -2] + '.txt')
    file_1 = open(txt_path, "w")
    ffmpeg.input(video_path).output(audio_path).run()

    model = AutoModel(model="paraformer-zh", vad_model="fsmn-vad", punc_model="ct-punc",
                      # spk_model="cam++",
                      )
    res = model.generate(input=audio_path,
                         batch_size_s=300,
                            hotword='魔搭')
    file_1.write(EncryptUrl + '\n')
    file_1.write(res[0]['text'])
    os.remove(audio_path)
    os.remove(video_path)

def work_pipeline():
    file_video = open(r"D:\fdu\shanghaidianjiaoguan\get_video\physics.txt")
    file_url = open(r"D:\fdu\shanghaidianjiaoguan\get_video\physics_url.txt")

    while(1):
        video_name = file_video.readline()
        video_url = file_url.readline()

        if not video_url:
            break

        #将内容下载到目的文件夹
        EncryptUrl = get_video_from_baseurl(video_name,video_url,video_file_path)
        get_words_from_video(video_file_path, video_name, words_file_path, EncryptUrl)

work_pipeline()