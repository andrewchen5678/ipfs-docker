#!/usr/bin/env python3
from argparse import ArgumentParser
from multiprocessing import Pool
from subprocess import Popen, PIPE, DEVNULL
from pathlib import Path

parser = ArgumentParser(
    description=f"keep live"
)
subparsers = parser.add_subparsers(help="Command")
parser.set_defaults(command=lambda _: parser.print_help())

cmd_test_gateway = subparsers.add_parser(
    "keep_alive",
    description="downloading folder through a gateway as tar archive",
    epilog="keep_alive"
)
cmd_test_gateway.add_argument(
    "cid", help="cid of folder")


def download_with_curl(gateway,hash):

    # or api way
    url = f"https://{gateway}/api/v0/get?arg={hash}&archive=true"
    print('api ' + url)

    Path(f"./test/{gateway}").mkdir(parents=True, exist_ok=True)

    with open(f"./test/{gateway}/{hash}.log", "wb") as f:
        p = Popen(["curl", '-f', '-X','POST', url] , stdout=DEVNULL, stderr=f)
        p.wait() # wait for process to finish; this also sets the returncode variable inside 'res'
        #print(p.returncode)
        if p.returncode != 0:
            #print('chafa')
            raise Exception(f"{url} download failed, exit code {p.returncode}")
        else:
            print(f'finished downloading through {url}')

def run_test_gateway(args):
    """
    test downloading through gateways
    """
    if __name__ == '__main__':
        gateways = [
            'ipfs.io', # the default one I use first
            'dweb.link',
            #'cloudflare-ipfs.com', wonky
            'jacl.tech', # pinning also works :)
            #'gateway.pinata.cloud',
        ]


        with Pool(5) as p:
            arr = [(gateway, args.cid,) for gateway in gateways]
            r = p.starmap_async(download_with_curl, arr)
            r.get()



cmd_test_gateway.set_defaults(command=run_test_gateway)

# Finally, use the new parser
all_args = parser.parse_args()
# Invoke whichever command is appropriate for the arguments
all_args.command(all_args)
