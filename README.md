start
`docker-compose up`

run command
`docker-compose exec ipfs_stack ipfs --version`

ipns publish 
`docker-compose exec ipfs_stack ipfs name publish --key=publishkey /ipfs/QmTA8Pod9JzZYz6gW629DByToceUU5ea5jCxEvY5SeWm6L`

cloudflare dnslink (beter than ipns)
`CF_API_TOKEN=get from 1password npx dnslink-cloudflare -d andrewtheguy.com -l /ipfs/bafybeigltgpaqm5liznsf7zlhtf4uoktjmf7wm7np2urawuz4dcanpt7m4 -r _dnslink.ipfs`