import whisper
import ffmpeg
import opencc
import os
import nltk
from funasr import AutoModel
from nltk.tokenize import sent_tokenize
# # 加载 Whisper 模型
# model = whisper.load_model("base")
#
# # 输入视频文件路径
# video_path = r"D:\fdu\shanghaidianjiaoguan\get_words_from_video\Test.mp4"
#
# # 使用 ffmpeg 将视频中的音频提取出来
# audio_path = r"D:\Fdu_test\extracted_audio.wav"
#
# ffmpeg.input(video_path).output(audio_path).run()
# # input = ffmpeg.input(video_path)
# # input.output(audio_path).run()Y
# # 使用 Whisper 进行转录
# result = model.transcribe(audio_path)
#
# # 输出转录结果
# print(result["text"])
#
# nltk.download('punkt')
#
# # 确保文件路径正确
# video_path = r"D:\fdu\shanghaidianjiaoguan\video\test.mp4"
# audio_path = r"D:\fdu\shanghaidianjiaoguan\video\extracted_audio.wav"
#
# # 确保 ffmpeg 可执行文件路径正确
# ffmpeg_executable = r'C:\ffmpeg\bin\ffmpeg.exe'  # 如果 ffmpeg 不在 PATH 中
#
# # 使用 ffmpeg 将视频中的音频提取出来
# ffmpeg.input(video_path).output(audio_path).run(cmd=ffmpeg_executable)
#
# # 加载 Whisper 模型
# model = whisper.load_model("base")
#
# # 使用 Whisper 进行转录
# result = model.transcribe(audio_path)
#
# # 获取转录的繁体中文文本
# traditional_text = result["text"]
#
# # 使用 opencc 将繁体中文转换为简体中文
# converter = opencc.OpenCC('t2s')
# simplified_text = converter.convert(traditional_text)
# print(simplified_text)
#
# # 使用 NLTK 添加标点符号
# sentences = sent_tokenize(simplified_text)
# #punctuated_text = '。'.join(sentences) + '。'  # 加上句号作为结尾
#
# # 输出简体中文带标点符号的转录结果
# # 添加逗号或句号
# print(sentences)
# processed_text = ""
# for i, sentence in enumerate(sentences):
#     # 在每个句子后添加逗号，除了最后一个句子
#     if i < len(sentences) - 1:
#         processed_text += sentence + "，"
#     # 在最后一个句子后添加句号
#     else:
#         processed_text += sentence + "。"
#
# print(processed_text)

# paraformer-zh is a multi-functional asr model
# use vad, punc, spk or not as you need
# audio_path = r"D:\fdu\shanghaidianjiaoguan\video\extracted_audio.wav"
# model = AutoModel(model="paraformer-zh",  vad_model="fsmn-vad",  punc_model="ct-punc",
#                   # spk_model="cam++",
#                   )
# res = model.generate(input=audio_path,
#                      batch_size_s=300,
#                      hotword='魔搭')
# print(res[0]['text'])
