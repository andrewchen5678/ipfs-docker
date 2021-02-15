

# IPFS Desktop (recommended)
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

ipns publish 
`docker-compose exec ipfs_stack ipfs name publish --key=publishkey /ipfs/changeme`

cloudflare dnslink (better than ipns)
```
CF_API_TOKEN=getfrom1password npx dnslink-cloudflare -d andrewtheguy.com -l /ipfs/changeme -r _dnslink.webdrive
```

# docker (for testing only)
start
`docker-compose up`

run command
`docker-compose exec ipfs_stack ipfs --version`

