"""
Nose tests for flask_brevets.py mongoDB interactions

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
import logging
import copy
import brevets_db


def test_brevet_1():

    brevet_1_in = {'begin_date': '2028-05-20T00:00',
                    'brevet_dist_km': '600',
                    'checkpoint_0': {'miles': '62.137100', 'km': '100', 'location': 'jeff', 'open': '2021-01-01T02:56', 'close': '2021-01-01T06:40', 'notes': ''},
                    'checkpoint_1': {'miles': '124.274200', 'km': '200', 'location': 'dunam', 'open': '2021-01-01T05:53', 'close': '2021-01-01T13:20', 'notes': ''},
                    'checkpoint_10': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_11': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_12': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_13': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_14': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_15': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_16': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_17': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_18': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_19': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_2': {'miles': '186.411300', 'km': '300', 'location': '', 'open': '2021-01-01T09:00', 'close': '2021-01-01T20:00', 'notes': ''},
                    'checkpoint_3': {'miles': '248.548400', 'km': '400', 'location': '', 'open': '2021-01-01T12:08', 'close': '2021-01-02T03:00', 'notes': ''},
                    'checkpoint_4': {'miles': '310.685500', 'km': '500', 'location': '', 'open': '2021-01-31T12:08', 'close': '2021-02-01T03:00', 'notes': ''},
                    'checkpoint_5': {'miles': '372.822600', 'km': '600', 'location': 'eeee', 'open': '2021-01-31T12:08', 'close': '2021-02-01T03:00', 'notes': ''},
                    'checkpoint_6': {'miles': '621.371000', 'km': '1000', 'location': '', 'open': '2021-02-01T09:05', 'close': '2021-02-03T03:00', 'notes': ''},
                    'checkpoint_7': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_8': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''},
                    'checkpoint_9': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}}

    brevet_1_out = copy.deepcopy(brevet_1_in)
    brevet_1_out['name'] = 'mybrevet'

    brevets_db.insert(brevet_1_in)
    query = brevets_db.display()
    assert(query == brevet_1_out)

def test_brevet_2():

    brevet_2_in = {'begin_date': '2023-10-01T13:05', 
                 'brevet_dist_km': '1000', 
                 'checkpoint_0': {'miles': '0.000000', 'km': '0', 'location': 'paris', 'open': '2023-10-01T00:00', 'close': '2023-10-01T01:00', 'notes': ''},
                 'checkpoint_1': {'miles': '62.137100', 'km': '100', 'location': 'berlin', 'open': '2023-10-01T02:56', 'close': '2023-10-01T06:40', 'notes': ''}, 
                 'checkpoint_2': {'miles': '155.342750', 'km': '250', 'location': 'mars', 'open': '2023-10-01T07:27', 'close': '2023-10-01T16:40', 'notes': ''}, 
                 'checkpoint_3': {'miles': '201.945575', 'km': '325', 'location': 'space', 'open': '2023-10-01T09:47', 'close': '2023-10-01T21:40', 'notes': ''}, 
                 'checkpoint_4': {'miles': '421.289538', 'km': '678', 'location': 'nowhere', 'open': '2023-10-01T21:35', 'close': '2023-10-02T22:50', 'notes': ''}, 
                 'checkpoint_5': {'miles': '552.398819', 'km': '889', 'location': 'here', 'open': '2023-10-02T05:07', 'close': '2023-10-03T17:17', 'notes': ''}, 
                 'checkpoint_6': {'miles': '692.828665', 'km': '1115', 'location': 'there', 'open': '2023-10-02T09:05', 'close': '2023-10-04T03:00', 'notes': ''}, 
                 'checkpoint_7': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_8': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_9': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_10': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_11': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_12': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_13': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_14': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_15': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_16': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_17': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_18': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}, 
                 'checkpoint_19': {'miles': '', 'km': '', 'location': '', 'open': '', 'close': '', 'notes': ''}}

    brevet_2_out = copy.deepcopy(brevet_2_in)
    brevet_2_out['name'] = 'mybrevet' 
    
    brevets_db.insert(brevet_2_in)
    query = brevets_db.display()
    assert(query == brevet_2_out)
