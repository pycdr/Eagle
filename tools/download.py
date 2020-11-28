from urllib.request import urlopen
from threading import Thread

class Downloader:
	def __init__(self, url, block_size, console, output = None):
		self.url = url
		self.ready = False
		self.out_path = output or url.split("/")[-1]
		self.block_size = block_size
		self.console = console
	def start(self):
		self.downloaded_size = 0
		self.out_file = open(self.out_path, "wb")
		self.download = True
		self.thread = Thread(target = self.get)
		self.thread.start()
		self.finished = False
	def get(self):
		try:
			self.uopen = urlopen(self.url)
			try:
				self.size = int(self.uopen.getheader("Content-Length"))
			except TypeError:
				self.console.log("[red]Error: error while getting file size[/red]")
			self.ready = True
			while self.download:
				buff = self.uopen.read(self.block_size)
				if not buff:
					break
				self.downloaded_size += len(buff)
				self.out_file.write(buff)
		except Exception as err:
			self.console.log("[red]"+str(err)+"[/red]")
			return
		finally:
			self.out_file.close()
			self.finished = True
