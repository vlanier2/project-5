"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
import logging
import acp_times
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)
log = logging.getLogger(__name__)

#####
# TEST OF SIMPLE BREVET ACROSS ONLY ONE SPEED BRACKET
# NO ODDITIES PRESENT
#####

def test_example_one_200km_brevet():
    """
    Tests a 200km brevet with controls at
    60km 120km 175km and 205km finish.
    This is example one from 
    https://rusa.org/pages/acp-brevet-control-times-calculator
    """
    control_locations = [0, 60, 120, 175, 205]
    times = acp_times.get_times_from_list(
        control_locations, 
        200, 
        arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'))

    truth_open = {
        0   : arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'),
        60  : arrow.get('2000-01-01 01:46:00', 'YYYY-MM-DD HH:mm:ss'),
        120 : arrow.get('2000-01-01 03:32:00', 'YYYY-MM-DD HH:mm:ss'),
        175 : arrow.get('2000-01-01 05:09:00', 'YYYY-MM-DD HH:mm:ss'),
        205 : arrow.get('2000-01-01 05:53:00', 'YYYY-MM-DD HH:mm:ss')
    }

    truth_close = {
        0   : arrow.get('2000-01-01 01:00:00', 'YYYY-MM-DD HH:mm:ss'),
        60  : arrow.get('2000-01-01 04:00:00', 'YYYY-MM-DD HH:mm:ss'),
        120 : arrow.get('2000-01-01 08:00:00', 'YYYY-MM-DD HH:mm:ss'),
        175 : arrow.get('2000-01-01 11:40:00', 'YYYY-MM-DD HH:mm:ss'),
        205 : arrow.get('2000-01-01 13:30:00', 'YYYY-MM-DD HH:mm:ss')
    }

    for control in times:
        log.debug(f"test for {control}")
        log.debug(f"{times[control]['open_time']} == {truth_open[control]}")
        assert(times[control]['open_time'] == truth_open[control])
        log.debug(f"{times[control]['close_time']} == {truth_close[control]}")
        assert(times[control]['close_time'] == truth_close[control])

#####
# TEST OF LONGER BREVET ACROSS MULTIPLE SPEED BRACKETS
# NO ODDITIES PRESENT
#####

def test_example_two_600km_brevet():
    """
    Tests a 600km brevet with controls every 50km
    and 609km finish.
    This is example two from 
    https://rusa.org/pages/acp-brevet-control-times-calculator
    """
    control_locations = [0, 100, 200, 350, 550, 609]

    times = acp_times.get_times_from_list(
        control_locations, 
        600, 
        arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'))

    truth_open = {
        0   : arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'),
        100 : arrow.get('2000-01-01 02:56:00', 'YYYY-MM-DD HH:mm:ss'),
        200 : arrow.get('2000-01-01 05:53:00', 'YYYY-MM-DD HH:mm:ss'),
        350 : arrow.get('2000-01-01 10:34:00', 'YYYY-MM-DD HH:mm:ss'),
        550 : arrow.get('2000-01-01 17:08:00', 'YYYY-MM-DD HH:mm:ss'),
        609 : arrow.get('2000-01-01 18:48:00', 'YYYY-MM-DD HH:mm:ss')
    }

    truth_close = {
        0   : arrow.get('2000-01-01 01:00:00', 'YYYY-MM-DD HH:mm:ss'),
        100 : arrow.get('2000-01-01 06:40:00', 'YYYY-MM-DD HH:mm:ss'),
        200 : arrow.get('2000-01-01 13:20:00', 'YYYY-MM-DD HH:mm:ss'),
        350 : arrow.get('2000-01-01 23:20:00', 'YYYY-MM-DD HH:mm:ss'),
        550 : arrow.get('2000-01-02 12:40:00', 'YYYY-MM-DD HH:mm:ss'),
        609 : arrow.get('2000-01-02 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    }

    for control in times:
        log.debug(f"test for {control}")
        log.debug(f"{times[control]['open_time']} == {truth_open[control]}")
        assert(times[control]['open_time'] == truth_open[control])
        log.debug(f"{times[control]['close_time']} == {truth_close[control]}")
        assert(times[control]['close_time'] == truth_close[control])

#####
# TEST OF CONTROL AT 890KM ON A 1000KM BREVET
# NO ODDITIES PRESENT
#####

def test_example_three_1000km_brevet():
    """
    Tests a 1000km brevet with one control at 890km. 
    Test include largest range of minimum and maximum speeds.
    This is example three from 
    https://rusa.org/pages/acp-brevet-control-times-calculator
    """
    control_locations = [0, 890, 1000]

    times = acp_times.get_times_from_list(
        control_locations, 
        1000, 
        arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'))

    truth_open = {
        0    : arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'),
        890  : arrow.get('2000-01-02 05:09:00', 'YYYY-MM-DD HH:mm:ss'),
        1000 : arrow.get('2000-01-02 09:05:00', 'YYYY-MM-DD HH:mm:ss')
    }

    truth_close = {
        0    : arrow.get('2000-01-01 01:00:00', 'YYYY-MM-DD HH:mm:ss'),
        890  : arrow.get('2000-01-03 17:23:00', 'YYYY-MM-DD HH:mm:ss'),
        1000 : arrow.get('2000-01-04 03:00:00', 'YYYY-MM-DD HH:mm:ss')
    }

    for control in times:
        log.debug(f"test for {control}")
        log.debug(f"{times[control]['open_time']} == {truth_open[control]}")
        assert(times[control]['open_time'] == truth_open[control])
        log.debug(f"{times[control]['close_time']} == {truth_close[control]}")
        assert(times[control]['close_time'] == truth_close[control])

#####
# TEST OF ODDITY - CONTROLS NEAR START ( < 60km)
# CLOSING TIME IS RELAXED. BASED ON 20km/hr plus 1hr
#####

def test_oddity_control_near_start_600km_brevet():
    """
    Tests a 600km brevet with one control at 890km. 
    Test include largest range of minimum and maximum speeds.
    This is example three from 
    https://rusa.org/pages/acp-brevet-control-times-calculator
    """
    control_locations = [0, 1, 10, 60, 65, 400, 609]

    times = acp_times.get_times_from_list(
        control_locations, 
        600, 
        arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'))

    truth_open = {
        0    : arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'),
        1    : arrow.get('2000-01-01 00:02:00', 'YYYY-MM-DD HH:mm:ss'),
        10   : arrow.get('2000-01-01 00:18:00', 'YYYY-MM-DD HH:mm:ss'),
        60   : arrow.get('2000-01-01 01:46:00', 'YYYY-MM-DD HH:mm:ss'),
        65   : arrow.get('2000-01-01 01:55:00', 'YYYY-MM-DD HH:mm:ss'),
        400  : arrow.get('2000-01-01 12:08:00', 'YYYY-MM-DD HH:mm:ss'),
        609  : arrow.get('2000-01-01 18:48:00', 'YYYY-MM-DD HH:mm:ss')
    }

    truth_close = {
        0    : arrow.get('2000-01-01 01:00:00', 'YYYY-MM-DD HH:mm:ss'),
        1    : arrow.get('2000-01-01 01:03:00', 'YYYY-MM-DD HH:mm:ss'),
        10   : arrow.get('2000-01-01 01:30:00', 'YYYY-MM-DD HH:mm:ss'),
        60   : arrow.get('2000-01-01 04:00:00', 'YYYY-MM-DD HH:mm:ss'),
        65   : arrow.get('2000-01-01 04:20:00', 'YYYY-MM-DD HH:mm:ss'),
        400  : arrow.get('2000-01-02 02:40:00', 'YYYY-MM-DD HH:mm:ss'),
        609  : arrow.get('2000-01-02 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    }

    for control in times:
        log.debug(f"test for {control}")
        log.debug(f"{times[control]['open_time']} == {truth_open[control]}")
        assert(times[control]['open_time'] == truth_open[control])
        log.debug(f"{times[control]['close_time']} == {truth_close[control]}")
        assert(times[control]['close_time'] == truth_close[control])

#####
# FRACTIONAL KM TEST
#####

def test_fractional_km_300km_brevet():
    """
    Tests a 300km brevet with controls at
    0, 34.556, 242.41, 242.89, 309.22, 309.99
    """
    control_locations = [0, 34.556, 242.41, 242.89, 309.22, 309.99]

    times = acp_times.get_times_from_list(
        control_locations, 
        300, 
        arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'))

    truth_open = {
        0       : arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'),
        34.556  : arrow.get('2000-01-01 01:02:00', 'YYYY-MM-DD HH:mm:ss'),
        242.41  : arrow.get('2000-01-01 07:12:00', 'YYYY-MM-DD HH:mm:ss'),
        242.89  : arrow.get('2000-01-01 07:14:00', 'YYYY-MM-DD HH:mm:ss'),
        309.22  : arrow.get('2000-01-01 09:00:00', 'YYYY-MM-DD HH:mm:ss'),
        309.99  : arrow.get('2000-01-01 09:00:00', 'YYYY-MM-DD HH:mm:ss')
    }

    truth_close = {
        0       : arrow.get('2000-01-01 01:00:00', 'YYYY-MM-DD HH:mm:ss'),
        34.556  : arrow.get('2000-01-01 02:45:00', 'YYYY-MM-DD HH:mm:ss'),
        242.41  : arrow.get('2000-01-01 16:08:00', 'YYYY-MM-DD HH:mm:ss'),
        242.89  : arrow.get('2000-01-01 16:12:00', 'YYYY-MM-DD HH:mm:ss'),
        309.22  : arrow.get('2000-01-01 20:00:00', 'YYYY-MM-DD HH:mm:ss'),
        309.99  : arrow.get('2000-01-01 20:00:00', 'YYYY-MM-DD HH:mm:ss')
    }

    for control in times:
        log.debug(f"test for {control}")
        log.debug(f"{times[control]['open_time']} == {truth_open[control]}")
        assert(times[control]['open_time'] == truth_open[control])
        log.debug(f"{times[control]['close_time']} == {truth_close[control]}")
        assert(times[control]['close_time'] == truth_close[control])

#####
# PRESSURE TEST - CONTROLS AT VARIED TIMES
# DIFFERENT START TIME - INCLUDES ODDITY
#####

def test_varied_1000km_brevet():
    """
    Tests a 1000km brevet with controls at
    0, 25, 118, 342, 600, 663, 1036, 1200
    brevet starts at 22:08.
    """
    control_locations = [00, 25, 118, 342, 600, 663, 1036, 1200]

    times = acp_times.get_times_from_list(
        control_locations, 
        1000, 
        arrow.get('2000-01-01 22:08:00', 'YYYY-MM-DD HH:mm:ss'))

    truth_open = {
        0    : arrow.get('2000-01-01 22:08:00', 'YYYY-MM-DD HH:mm:ss'),
        25   : arrow.get('2000-01-01 22:52:00', 'YYYY-MM-DD HH:mm:ss'),
        118  : arrow.get('2000-01-02 01:36:00', 'YYYY-MM-DD HH:mm:ss'),
        342  : arrow.get('2000-01-02 08:27:00', 'YYYY-MM-DD HH:mm:ss'),
        600  : arrow.get('2000-01-02 16:56:00', 'YYYY-MM-DD HH:mm:ss'),
        663  : arrow.get('2000-01-02 19:11:00', 'YYYY-MM-DD HH:mm:ss'),
        1036 : arrow.get('2000-01-03 07:13:00', 'YYYY-MM-DD HH:mm:ss'),
        1200 : arrow.get('2000-01-03 07:13:00', 'YYYY-MM-DD HH:mm:ss')
    }

    truth_close = {
        0    : arrow.get('2000-01-01 23:08:00', 'YYYY-MM-DD HH:mm:ss'),
        25   : arrow.get('2000-01-02 00:23:00', 'YYYY-MM-DD HH:mm:ss'),
        118  : arrow.get('2000-01-02 06:00:00', 'YYYY-MM-DD HH:mm:ss'),
        342  : arrow.get('2000-01-02 20:56:00', 'YYYY-MM-DD HH:mm:ss'),
        600  : arrow.get('2000-01-03 14:08:00', 'YYYY-MM-DD HH:mm:ss'),
        663  : arrow.get('2000-01-03 19:39:00', 'YYYY-MM-DD HH:mm:ss'),
        1036 : arrow.get('2000-01-05 01:08:00', 'YYYY-MM-DD HH:mm:ss'),
        1200 : arrow.get('2000-01-05 01:08:00', 'YYYY-MM-DD HH:mm:ss')
    }

    for control in times:
        log.debug(f"test for {control}")
        log.debug(f"{times[control]['open_time']} == {truth_open[control]}")
        assert(times[control]['open_time'] == truth_open[control])
        log.debug(f"{times[control]['close_time']} == {truth_close[control]}")
        assert(times[control]['close_time'] == truth_close[control])


