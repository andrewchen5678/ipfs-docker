#!/usr/bin/env python3
import sys,json,os

# generate m3u from slate host get collection api result
if __name__ == '__main__':
    data = sys.stdin.read()
    result = json.loads(data)
    objects = result['collection']['objects']
    a = sorted(objects, key=lambda x: x['filename'])
    gateway = 'ipfs.io'

    with open(f"./test/{result['collection']['slatename']}.m3u8", "w") as f:
        print('#EXTM3U',file=f)
        for pair in a:
            cid=pair['cid']
            path=pair['filename']
            filename, file_extension = os.path.splitext(path)
            if file_extension.lower() not in ['.mp3','.m4a']:
                continue
            print(f'#EXTINF:-1,{filename}', file=f)
            print(f'https://{gateway}/ipfs/{cid}', file=f)
