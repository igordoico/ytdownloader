import youtube_dl
import pyffmpeg


def downloader(url):
    url = url.strip()
    youtube_dl.YoutubeDL(params={
        'listformats': True,
        'download_archive': 'output'
    }).download([url])
    fm = input('Digite o codigo do melhor formato de audio + melhor formato de video \nExemplo: 137+258\n')

    youtube_dl.YoutubeDL(params={
        'format': fm,
        'ffmpeg_location': './ffmpeg/bin/'
    }).download([url])

if __name__ == '__main__':
    url = input("Cole a URL do youtube\n", )
    downloader(url)
