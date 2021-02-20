

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

cloudflare dnslink (better than ipns)
```
CF_API_TOKEN=getfrom1password npx dnslink-cloudflare -d andrewtheguy.com -l /ipfs/changeme -r _dnslink.webdrive
```

# docker (will be separate environment)
start
`docker-compose up`

clean up
`rm -rf ./ipfsdata/*`

run command
`docker-compose exec ipfs_host ipfs --version`

ipns publish 
`docker-compose exec ipfs_host ipfs name publish --key=publishkey /ipfs/changeme`
