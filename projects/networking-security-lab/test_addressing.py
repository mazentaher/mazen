import unittest
from addressing import ipaddress, main


class AddressingLabTests(unittest.TestCase):
    def test_private_address_is_in_network(self):
        address = ipaddress.ip_address("192.168.1.20")
        network = ipaddress.ip_network("192.168.1.0/24")
        self.assertTrue(address.is_private)
        self.assertIn(address, network)

    def test_outside_address(self):
        address = ipaddress.ip_address("192.168.2.20")
        network = ipaddress.ip_network("192.168.1.0/24")
        self.assertNotIn(address, network)


if __name__ == "__main__":
    unittest.main()
