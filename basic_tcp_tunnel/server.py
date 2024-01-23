import os
import sys

if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in sys.path:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import colorama

from basic_tcp_tunnel.tunnel_server.tunnelservice import TunnelService


def main():
    colorama.init()

    service = TunnelService()
    service.run_forever()


if __name__ == "__main__":
    main()
