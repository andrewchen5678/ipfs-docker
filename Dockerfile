FROM ipfs/go-ipfs:v0.7.0


FROM debian:buster 

COPY  --from=0 /usr/local/bin/ipfs /usr/local/bin/ipfs

RUN apt-get update && apt-get install -y \
  ca-certificates \
  fuse \
  telnet \
  && rm -rf /var/lib/apt/lists/*

# Swarm TCP; should be exposed to the public
EXPOSE 4001
# Daemon API; must not be exposed publicly but to client services under you control
EXPOSE 5001
# Web Gateway; can be exposed publicly with a proxy, e.g. as https://ipfs.example.org
EXPOSE 8080
# Swarm Websockets; must be exposed publicly when the node is listening using the websocket transport (/ipX/.../tcp/8081/ws).
EXPOSE 8081

# Create the fs-repo directory and switch to a non-privileged user.
ENV IPFS_PATH /data/ipfs
RUN mkdir -p $IPFS_PATH 

# Expose the fs-repo as a volume.
# start_ipfs initializes an fs-repo if none is mounted.
# Important this happens after the USER directive so permission are correct.
VOLUME $IPFS_PATH

CMD ["/bin/bash"]  