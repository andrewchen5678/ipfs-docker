#docker (not recommended)
start
`docker-compose up`

run command
`docker-compose exec ipfs_stack ipfs --version`

ipns publish 
`docker-compose exec ipfs_stack ipfs name publish --key=publishkey /ipfs/changeme`

#homebrew (recommended)
brew install ipfs
ipfs init

cloudflare dnslink (better than ipns)
`CF_API_TOKEN=getfrom1password npx dnslink-cloudflare -d andrewtheguy.com -l /ipfs/changeme -r _dnslink.ipfs`