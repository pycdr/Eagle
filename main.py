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

args = parser.parse_args()

if not is_url(args.url):
	console.log("[red]Error: please give a valid url.[/red]")
	if not args.url.startswith("https://") or not args.url.startswith("http://"):
		console.print("[yellow]maybe you meant http(s)://" + args.url + "[/yellow]")
	exit()

download = Downloader(args.url, 2**16, output = args.output)
progress = ProgressBar(download)

try:
	download.start()
except Exception as err:
	console.log("[red]", err, "[/red]")
	exit()
while not download.ready:
	sleep(.5)
progress.start()
