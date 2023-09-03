"""Unit tests for OreSat0 OD database."""

from oresat_od_db.oresat0 import OD_DB, BEACON_DEF

from . import TestConfig


class TestOreSat0(TestConfig):
    """Test the OreSat0 OD database."""

    def test_tpdo_sizes(self):
        """Validate OreSat0 TPDO sizes."""

        self._test_tpdo_sizes(OD_DB)

    def test_beacon(self):
        """Test all OreSat0 objects reference in the beacon definition exist in C3 OD."""

        self._test_beacon(OD_DB, BEACON_DEF)
