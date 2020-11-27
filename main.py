from tools.download import Downloader
from tools.progressbar import ProgressBar
from rich.console import Console
from argparse import ArgumentParser
from validators import url as is_url

console = Console()
parser = ArgumentParser(description = "Eagle - a download manager based on CLI")

parser.add_argument("url", required = False,
	help = "the url that file will be downloaded from")
parser.add_argument("-o", "--output", required = False,
	help = "the path where the file will be saved there")

args = parser.parse_args()

if not args.url:
	console.log("[red]Error: please give url to download from it![/red]")
	exit()
if not is_url(args.url):
	console.log("[red]Error: please give a valid url.[/red]")
	if not url.startswith("https://") or not url.startswith("http://"):
		console.print("[yellow]maybe you meant http[s]://" + url + "[/yellow]")
	exit()

download = Downloader(url, 2**16, output = args.output)
progress = ProgessBar(download)

download.start()
progress.start()
