from ftplib import FTP
import ffmpeg


def grabVideo():
    fileName = '*'
    with open(fileName, 'wb') as fp:
        print(ftp.retrbinary('RETR ' + fileName, fp.write, 1000000))


def encodeVideo():
    print('Encoding the Video')
    path = '*'
    stream = ffmpeg.input(path)
    stream = ffmpeg.hflip(stream)
    stream = ffmpeg.output(stream, 'video.mp4', format='mp4')
    ffmpeg.run(stream)
    print('Finished Encoding Video')


ftp = FTP('*')
print(ftp.login(user='*', passwd='*'))

print(ftp.pwd())
print('Grabbing the video')
grabVideo()
print('Encoding the Video')
encodeVideo()
print('Finished cleaning up')    
ftp.quit()
