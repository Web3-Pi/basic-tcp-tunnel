# SERVICE PUBLIC INTERFACE
# Provide a valid public IP used by this server
SERVICE_PUBLIC_IP = 'localhost'
SERVICE_PUBLIC_LISTEN_PORT = 6512

DEFAULT_ACCEPTED_USER = "aaa"

ACCEPT_TIMEOUT = 2.5

# TUNNEL
TUNNEL_KEEPALIVE_DELAY = 25.0
TUNNEL_INTERRUPT_POLL_DELAY = 4.0

# UPnP
PUBLIC_SERVICE = True
USE_UPNP = True and PUBLIC_SERVICE
UPNP_DISCOVERY_TIMEOUT = 0.5
UPNP_LEASE_TIME = 1 * 3600
