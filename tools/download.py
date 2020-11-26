from urllib.request import urlopen
from threading import Thread

class Downloader:
	def __init__(self, url, block_size, output = None):
		self.url = url
		self.out_path = output or url.split("/")[-1]
	def start(self):
		self.downloaded_size = 0
		self.out_file = open(self.out_path, "wb")
		self.download = True
		self.thread = Thread(self.get)
		self.thread.start()
	def get(self):
		self.uopen = urlopen(self.url)
		self.size = int(self.uopen.info().getheaders("Content-Lenght")[0])
		while self.download:
			buff = self.uopen.read(self.block_size)
			if not buff:
				break
			self.downloaded_size += len(buff)
			f.write(buff)
		self.out_file.close()
