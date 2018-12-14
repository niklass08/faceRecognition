import os
directory = './video'
print(os.listdir('./video'))

#iterating on file in directory
for filename in os.listdir(directory):
        os.system("ffmpeg -i "+directory+"/*.mp4 -vf fps=1 ./image/thumb%04d.jpg -hide_banner")
