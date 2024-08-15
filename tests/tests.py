import unittest
from renold import (
    get_chain_options,
    ChainCriteria,
    ProductRange,
    Standard,
    ChainOptionsResponse,
)
from pprint import pprint
import logging
import http.client as http_client

http_client.HTTPConnection.debuglevel = 1
# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class TestRenoldChainSelector(unittest.TestCase):

    def test_valid(self):
        criteria: ChainCriteria = {
            "power_value_type": "InputPower",
            "power_value": 10,
            "speed_value_type": "InputSpeed",
            "speed_value": 1_000,
            "start_speed": 1,
            "finish_speed": 1000,
            "speed_increment": 10,
            "target_working_life": 15_000,
            "working_life_tolerance": 100,
            "driving_sprocket_teeth": 19,
            "driven_sprocket_teeth": 19,
            "centre_distance_rounding_mode": "EvenNumberOfLinks",
            "centre_distance": 900,
            "number_of_links": 0,
            "user_supplied_number_of_links": False,
            "driving_machine_characteristics": "SlightShocks",
            "driven_machine_characteristics": "ModerateShocks",
            "lubrication_regime": "Insufficient",
            "environment_condition": "Normal",
            "environment_domain": "Indoor",
            "product_range_id": ProductRange.SYNERGY,
            "chain_standard_id": Standard.BRITISH,
            "unit": "Metric",
        }

        r = get_chain_options(criteria)
        pprint(r.status_code)
        self.assertEqual(r.status_code, 200)
        data: ChainOptionsResponse = r.json()
        pprint(data)
