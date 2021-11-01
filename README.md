

# IPFS Desktop
https://github.com/ipfs-shipyard/ipfs-desktop

afterwards `ln -s /Applications/IPFS\ Desktop.app/Contents/Resources/app.asar.unpacked/node_modules/go-ipfs/go-ipfs/ipfs ~/bin/ipfs`

## disable localhost subdomain
```
ipfs config --json Gateway.PublicGateways '{
    "localhost": {
      "UseSubdomains": false,
      "Paths": ["/ipfs", "/ipns"]
    }
  }'
```

# keep alive
```
./refresh_contents.py keep_alive cid of directory
```
example:
```
./refresh_contents.py keep_alive QmU4LAxfpsY5A7pzYPetwLoAj8txmLKUUU2EeRaLQx2KsH --gateway=dweb.link -s
```


# generate m3u8
```
./refresh_contents.py m3u8 cid of directory
```
example:
```
./refresh_contents.py m3u8 QmU4LAxfpsY5A7pzYPetwLoAj8txmLKUUU2EeRaLQx2KsH --gateway=dweb.link
```

# play with docker
```
IPFS_PATH=/Volumes/andrew10/ipfs IPFS_DOCKER_EXPORT_PATH=$HOME docker-compose up
```
and then in another window
```
docker exec -it ipfs_host /bin/sh
```

#set ipfs path on shell
```shell
NEW_IPFS_PATH=/path source ~/bin/set_ipfs_path.sh
```

run `download-youtube-playlist.py socks5://127.0.0.1:19050`