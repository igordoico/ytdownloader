import youtube_dl


def downloader(url):
    youtube_dl.YoutubeDL().download([url])


if __name__ == '__main__':
    url = input("Cole a URL do youtube\n", )
    downloader(url)
