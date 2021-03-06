# coursera_tools



## rename.py

用于处理下载好的 coursera 课程。

文件目录结构如下：

- 1 introduction-tensorflow（**course**）
  - 1_a-new-programming-paradigm（**class**）
    - 01_a-new-programming-paradigm（**section**）
      - mp4 文件
      - txt  字幕文件（包括多国语言）
      - srt 字幕文件（包括多国语言）
    - 02_weekly-exercise-your-first-neural-network
  - 2_introduction-to-computer-vision
  - 3_enhancing-vision-with-convolutional-neural-networks
  - 4_using-real-world-images



层次关系是 course -> class -> section -> file，例如 `1 introduction-tensorflow\1_a-new-programming-paradigm\01_a-new-programming-paradigm\01_introduction-a-conversation-with-andrew-ng.mp4`。

处理的目的是：

1. 删除 `.` 开头的 mp4 文件

2. 删除 txt 字幕文件，因为 txt 字幕文件没有时间轴

3. srt  字幕文件，只保留 `en.srt` 和 `zh-CN.srt` 结尾的字幕文件，删除其他语言的字幕文件

4. 修改剩下文件的文件名，去掉文件名的空格，根据 course、class、section 的序号，给文件名添加序号。包括 mp4 文件和 srt 文件。

   例子：
   
   - 源文件名：
   
   ```
   1 introduction-tensorflow\1_a-new-programming-paradigm\01_a-new-programming-paradigm\01_introduction-a-conversation-with-andrew-ng.mp4
   ```
   
   - 修改后的文件名：
   
   ```
   1 introduction-tensorflow\1_a-new-programming-paradigm\01_a-new-programming-paradigm\1.1.1 introduction a conversation with andrew ng.mp4
   ```



## make_target_dir.py

创建目标文件夹，用于存放添加字幕后的视频。



## create_bilingual_srt.py

把中文字幕和英文字幕合并，创建双语字幕。

- 英文字幕 1.2.1.2 an introduction to computer vision.en.srt
- 中文字幕 1.2.1.2 an introduction to computer vision.zh-CN.srt
- 双语字幕 1.2.1.2 an introduction to computer vision.bilingual.srt

实际上，是把英语字幕的内容，直接添加到中文字幕内容的后面即可。



# 字幕翻译项目

字幕翻译项目：请查看这里：[https://github.com/zhangxiann/Tensorflow-In-Practice](https://github.com/zhangxiann/Tensorflow-In-Practice)