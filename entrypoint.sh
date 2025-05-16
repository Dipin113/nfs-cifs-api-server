#!/bin/bash

rpcbind
exportfs -r
service nfs-kernel-server start

mkdir -p /run/samba
smbd --foreground &

uvicorn nfs_api.main:app --host 0.0.0.0 --port 8000
