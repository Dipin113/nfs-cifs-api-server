FROM debian:bookworm-slim AS builder

RUN sudo apt update && sudo apt install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    nfs-kernel-server samba rpcbind curl ca-certificates \
    && python3 -m pip install --no-cache-dir fastapi uvicorn \
    && apt autoremove -y && apt clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY nfs_api /app/nfs_api
COPY exports /etc/exports
COPY smb.conf /etc/samba/smb.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

FROM debian:bookworm-slim

COPY --from=builder /usr /usr
COPY --from=builder /lib /lib
COPY --from=builder /lib64 /lib64
COPY --from=builder /etc/exports /etc/exports
COPY --from=builder /etc/samba /etc/samba
COPY --from=builder /app /app

RUN mkdir -p /exports/data && chmod 777 /exports/data && mkdir -p /run/samba

EXPOSE 2049 111/tcp 111/udp 445 139 8000

VOLUME ["/exports/data"]

WORKDIR /app
CMD ["/app/entrypoint.sh"]
