from tools.download import Downloader
from tools.progressbar import ProgressBar
from rich.console import Console
from argparse import ArgumentParser
from validators import url as is_url
from time import sleep

console = Console()
parser = ArgumentParser(description = "Eagle - a download manager based on CLI")

parser.add_argument("url",
	help = "the url that file will be downloaded from")
parser.add_argument("-o", "--output", required = False,
	help = "the path where the file will be saved there")
parser.add_argument("-b", "--block", required = True,
	help = "the block size for download process")

args = parser.parse_args()

if not is_url(args.url):
	console.log("[red]Error: please give a valid url.[/red]")
	if not args.url.startswith("https://") or not args.url.startswith("http://"):
		console.print("[yellow]maybe you meant http(s)://" + args.url + "[/yellow]")
	exit()
if not args.block.isnumeric():
	console.log("[red]Error: please give a valid block size.[/red]")
	exit()

download = Downloader(args.url, int(args.block), console, output = args.output)
progress = ProgressBar(download, console)

try:
	download.start()
	while not download.ready and not download.finished:
		sleep(.5)
	if download.ready and not download.finished:
		progress.start()
except Exception as err:
	console.log("[red]"+str(err)+"[/red]")
	exit()
