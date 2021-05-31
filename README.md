# Denmark_2021
This repository contains data and processing scripts for an initial analysis into the regional wind energy potential for Denmark.

# Data 
Jake Badger, Patrick Volker and Marc Imberger simulated the yield and atmospheric circulation of the German Bight for the "AGORA Energiewende: Making the most of Offshore Wind" study using WRF - EWP. Hourly ouputs at a daily frequency for the year 2006 were saved to disk. Using this data, we have extracted hourly wind speed timeseries from the Atmospheric circulation simulations without any wind parks and those with different areas and turbine densities within these areas ( see Agora study for more details.

# Data extraction location 
Latitude : 56.343175 deg, or 56 deg 20 min 35.43 sec
Longitude: 6.541659 deg, or 6 deg 32 min 29.972 sec

# Scripts:
1. PP_Windspeed.py - calculates wind speed and wind direction.
