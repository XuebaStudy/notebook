!!! abstract
    1.本项目核心来源于CTF比赛：Hackergame 2021 的 p😭q  (generate_sound_visualization.py)  
    2.原始动机在于希望他人愿意欣赏[魔女之旅的ED(piano)](/Belief/charactors/灰之魔女伊蕾娜)  
    3.主要使用了 python 与 [ffmpeg](https://en.wikipedia.org/wiki/FFmpeg){:target="_blank"} 进行处理

### 1. 使用 python 音频处理库 librosa 将 mp3文件 转换为 gif频谱动图
(文件较大时需要一定时间)
```python
    from array2gif import write_gif  # version: 1.0.4
    import librosa  # version: 0.10.2.post1
    import numpy  # version: 1.26.4

    num_freqs = 32
    quantize = 2
    min_db = -60
    max_db = 30
    fft_window_size = 2048
    frame_step_size = 512
    window_function_type = 'hann'
    color_pixel = (30, 144, 255)  # DodgerBlue
    white_pixel = (255, 255, 255)  # Colors etc. can be modified by yourself

    def convert_to_gif(src, dst):
        y, sample_rate = librosa.load(src)

        spectrogram = numpy.around(
            librosa.power_to_db(
                librosa.feature.melspectrogram(
                    y=y, sr=sample_rate, n_mels=num_freqs,
                    n_fft=fft_window_size,
                    hop_length=frame_step_size,
                    window=window_function_type
                )
            ) / quantize
        ) * quantize

        gif_data = [
            numpy.kron(
                numpy.array([
                    [
                        color_pixel if freq % 2 and i < round(
                            frame[freq // 2]) else white_pixel
                        for i in reversed(
                            range(min_db, max_db + 1, quantize))
                    ]
                    for freq in range(num_freqs * 2 + 1)
                ]),
                numpy.ones([quantize, quantize, 1])
            )
            for frame in spectrogram.transpose()
        ]

        write_gif(gif_data, dst, fps=sample_rate/frame_step_size)

    if __name__ == '__main__':
        convert_to_gif('input.mp3', 'output.gif')  # sample rate is 22050 Hz
```
### 2. 使用 ffmpeg 将 mp3文件 与 gif文件 合成为 mp4文件  
- 在命令行用`ffmpeg -i input.mp3` 与 `ffmpeg -i output.gif` 分别求出时长：duration_of_mp3 、duration_of_gif  

- 使用  
`ffmpeg -i output.gif -i input.mp3 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2, fps=25, setpts=PTS*(duration_of_mp3/duration_of_gif)" -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest output.mp4`  
命令生成 mp4文件 (命令中的 duration_of_mp3/duration_of_gif 需要根据第一步修改，如 223/192 )
??? note "参数解释"
    - scale=trunc(iw/2)\*2:trunc(ih/2)\*2：确保视频的宽高是偶数，以避免编码问题。
    - fps=25：设置目标帧率为 25 FPS（你可以调整这个值）。
    - setpts=PTS*(duration_of_mp3/duration_of_gif)：自动计算并调整帧时间戳，以使 GIF 播放时长等于 MP3 的时长。
    - -c:v libx264：使用 H.264 编码器压缩视频。
    - -pix_fmt yuv420p：设置像素格式为 yuv420p。
    - -c:a aac：使用 AAC 编码器压缩音频。
    - -b:a 192k：设置音频比特率为 192 kbps。
    - -shortest：确保视频的时长不超过 MP3 的时长。
### 3. 效果展示
<div style="text-align: center;">
    <video src="/assets/video/ilyina_ed.mp4" controls="controls"></video>
    <br>
    <span style="font-size: 16px; color: #555;">The sound is from <a href="/Belief/charactors/灰之魔女伊蕾娜">《魔女の旅々》ED</a></span>
</div>


