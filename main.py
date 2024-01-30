
import argparse
from datetime import datetime, timedelta
from urllib.request import urlopen
from urllib.error import URLError

import config

parser = argparse.ArgumentParser(description='Data loader from hub1.emsd.ru')
parser.add_argument('--date', type=list, default=None, help='Date of data.')
parser.add_argument('station', type=str, help='Name of station.')
parser.add_argument('channels', type=list, help='List of channels.')

args = parser.parse_args()

print(args.date)

def get_yesterday() -> datetime:
    return datetime.utcnow() - timedelta(days=1)

def generate_mask(station_name: str, net: str, loc: str, channel: str) -> str:
    return f'{station_name}{net}{loc}{channel}'
    
def generate_url(mask: str, url: str, date: datetime) -> str:
    return url.format(mask=mask, date=date)



for mask in config.MASKS:
    url = config.HUB1_URL.format(mask=mask, date=get_yesterday())
    response = urlopen(url)
    with open(f"{get_yesterday():%Y%m%d0000}.mseed", "ab") as file:
        file.write(response.read())
