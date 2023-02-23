"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

### TABLES

BREVETS_SPEED_TABLE = {
   0    : {'minimum' : 15, 'maximum' : 34},
   200  : {'minimum' : 15, 'maximum' : 32},
   400  : {'minimum' : 15, 'maximum' : 30},
   600  : {'minimum' : 11.428, 'maximum' : 28},
   1000 : {'minimum' : 13.333, 'maximum' : 26}
}

HARDCODED_TIME_LIMITS = {
   200  : {"hours" : 13, "minutes" : 30},
   300  : {"hours" : 20, "minutes" : 0},
   400  : {"hours" : 27, "minutes" : 0},
   600  : {"hours" : 40, "minutes" : 0},
   1000 : {"hours" : 75, "minutes" : 0}
}

### HELPER FUNCTIONS

def get_speed(control_location_km, maximum_or_minimum):
   """
   Get the speed associated with the given control location
   in kilometers - Specifying maximum or minimum speed.
   """
   for control_cutoff in BREVETS_SPEED_TABLE:
      if control_location_km <= control_cutoff:
         return BREVETS_SPEED_TABLE[control_cutoff][maximum_or_minimum]
   return False

def minimum_speed(control_location_km):
   """
   Get the minimum speed for the given control location
   """
   return get_speed(control_location_km, 'minimum')

def maximum_speed(control_location_km):
   """
   Get the maximum speed for the given control location
   """
   return get_speed(control_location_km, 'maximum')

def get_time_pair(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   returns a dictionary with both the opening and closing time for the
   given control distance. Times are arrow datetime objects.
   return format:
   {
      'open_time'  : <time>
      'close_time' : <time>
   }
   """
   return {
      'open_time'  : open_time(control_dist_km, brevet_dist_km, brevet_start_time),
      'close_time' : close_time(control_dist_km, brevet_dist_km, brevet_start_time)
      }

def get_times_from_list(control_dists_km, brevet_dist_km, brevet_start_time):
   """
   returns a dictionary containing all starting and ending times from the given
   list of control distances. Function assumes control distances are in increasing
   order.
   return format:
   {
      <dist1> : 
      {
         'open_time'  : <time>
         'close_time' : <time>
      },

      <dist2> :
      {
         'open_time'  : <time>
         'close_time' : <time>
      }
   }
   """
   start_times_dict = dict()
   for control_dist_km in control_dists_km:
      start_times_dict[control_dist_km] = get_time_pair(control_dist_km,
                                          brevet_dist_km, brevet_start_time)
   return start_times_dict

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
      brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600,
         or 1000 (the only official ACP brevet distances)
      brevet_start_time:  An arrow object
   Returns:
      An arrow object indicating the control open time.
      This will be in the same time zone as the brevet start time.
   """

   control_dist_km = round(control_dist_km)

   # consider opening time adjustment from rulebook
   if control_dist_km >= brevet_dist_km: control_dist_km = brevet_dist_km

   # calculate time offset standard method with maximum speed
   hour_offset = 0
   minute_offset = 0
   for control_cutoff in reversed(BREVETS_SPEED_TABLE):
      cuttoff_diff = control_dist_km - control_cutoff
      if cuttoff_diff > 0:
         max_speed = BREVETS_SPEED_TABLE[control_cutoff]['maximum']
         time_hours = cuttoff_diff / max_speed
         fractional_part = time_hours % 1
         minute_offset += (fractional_part * 60)
         hour_offset += (time_hours // 1)
         control_dist_km -= cuttoff_diff

         print(cuttoff_diff, control_dist_km, hour_offset, minute_offset)

   return brevet_start_time.shift(hours=hour_offset, minutes=round(minute_offset))


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
         brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600, or 1000
         (the only official ACP brevet distances)
      brevet_start_time:  An arrow object
   Returns:
      An arrow object indicating the control close time.
      This will be in the same time zone as the brevet start time.
   """

   control_dist_km = round(control_dist_km)

   # consider hard-coded closing times from rulebook
   if control_dist_km >= brevet_dist_km:
      time_adjustment = HARDCODED_TIME_LIMITS[brevet_dist_km]
      return brevet_start_time.shift(hours=time_adjustment['hours'], 
                                     minutes=time_adjustment['minutes'])

   if control_dist_km == 0: # by rule the closing time of 0 is +1hr
      return brevet_start_time.shift(hours=1)

   # consider closing time relaxation for controls within 60km of start
   if control_dist_km <= 60:
      time_hours = control_dist_km / 20
      minute_offset = round((time_hours % 1) * 60)
      hour_offset = 1 + (time_hours // 1)
      return brevet_start_time.shift(hours=hour_offset, minutes=minute_offset)
   
   # calculate time offset standard method with minimum speed
   hour_offset = 0
   minute_offset = 0
   for control_cutoff in reversed(BREVETS_SPEED_TABLE):
      cuttoff_diff = control_dist_km - control_cutoff
      if cuttoff_diff > 0:
         min_speed = BREVETS_SPEED_TABLE[control_cutoff]['minimum']
         time_hours = cuttoff_diff / min_speed
         fractional_part = time_hours % 1
         minute_offset += (fractional_part * 60)
         hour_offset += (time_hours // 1)
         control_dist_km -= cuttoff_diff

   return brevet_start_time.shift(hours=hour_offset, minutes=round(minute_offset))

