from rich.progress import Progress

class ProgressBar:
	def __init__(self, downloader_obj, console):
		self.dl_obj = downloader_obj
		self.progress = Progress(console = console, transient = True)
	def start(self):
		self.csize = 0
		self.task = self.progress.add_task("[green] downloading...", total = self.dl_obj.size)
		while not self.dl_obj.finished:
			adv = self.dl_obj.downloaded_size - self.csize
			self.progress.update(self.task, advance = adv)
			self.csize = self.dl_obj.downloaded_size
