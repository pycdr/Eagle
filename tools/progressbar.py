from rich.progress import Progress
from rich.console import Console

class ProgressBar:
	def __init__(self, downloader_obj):
		self.dl_obj = downloader_obj
		self.console = Console()
		self.progress = Progress(console = self.console, transient = True)
	def start(self):
		self.csize = 0
		self.task = self.progress.add_task("[green] downloading...", total = self.dl_obj.size)
		while not self.dl_obj.finished:
			adv = self.dl_obj.downloaded_size - self.csize
			self.progress.update(self.task, advance = adv)
			self.csize = self.dl_obj.downloaded_size
