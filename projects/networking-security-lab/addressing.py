#!/usr/bin/env python3
"""Explain IPv4 network membership for addresses supplied by the user."""

import argparse
import ipaddress


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect an IPv4 address and network.")
    parser.add_argument("address")
    parser.add_argument("network", help="CIDR network, e.g. 192.168.1.0/24")
    args = parser.parse_args()
    address = ipaddress.ip_address(args.address)
    network = ipaddress.ip_network(args.network, strict=False)
    print(f"Address: {address}")
    print(f"Network: {network}")
    print(f"Version: IPv{address.version}")
    print(f"Private: {address.is_private}")
    print(f"In network: {address in network}")


if __name__ == "__main__":
    main()
