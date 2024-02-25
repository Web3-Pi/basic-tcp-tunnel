import os
import sys

from basic_tcp_tunnel.config.conf import TUNNEL_ESTABLISH_PORT, PROXY_ESTABLISH_PORT
from basic_tcp_tunnel.config.srvconf import SERVICE_PUBLIC_LISTEN_PORT, UPNP_LEASE_TIME
from basic_tcp_tunnel.tunnel_server.upnp.upnpportmapper import BasicUPnPPortMapper
from basic_tcp_tunnel.tunnel_server.upnp.upnpservice import BasicUPnPService

if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in sys.path:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import colorama

from basic_tcp_tunnel.tunnel_server.servertunnelservice import ServerTunnelService


def test_upnp():
    port = 12850
    rule = "test rule 0"
    upnp = BasicUPnPPortMapper()

    print("Entering test upnp zone")
    upnp.initialize(0.5)

    print(f"Adding {port} with rule: {rule}")
    res = upnp.add_simple_mapping_rule(port, rule, UPNP_LEASE_TIME)

    if not res:
        print("Whatever that failed")


def main():
    colorama.init()

    service = ServerTunnelService()
    service.run_forever()


if __name__ == "__main__":
    test_upnp()
    # main()
