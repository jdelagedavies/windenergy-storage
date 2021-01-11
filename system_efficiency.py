from wind_turbine import WindTurbine
import pandas as pd

MODEL_NAME = "SG 8.0 167-DD"
HEIGHT = 167
SWEPT_AREA = 21900
turbine = WindTurbine(MODEL_NAME, HEIGHT, SWEPT_AREA)


def calc_system_efficiency():
    """
           Calculates the system's energy production efficiency as a percentage for every hour. The formula is based
           on a ratio between the absolute values of power output and input, respectively. This computation is only
           relevant for the charging and discharging state. All of the outputted values are stored in the eff.csv file.
           """
    median_power = turbine.MEDIAN_POWER
    for row in df.itertuples(index=False):
        STATE = row[2]
        STORAGE_POWER = row[1]
        TURBINE_POWER = row[0]

        if STATE == 'CHARGING' or STATE == 'DISCHARGING':
            efficiency = (abs(STORAGE_POWER) / abs(median_power - TURBINE_POWER)) * 100
            SYSTEM_EFFICIENCY.append(efficiency)
        else:
            SYSTEM_EFFICIENCY.append(None)


df = pd.read_csv('out.csv', usecols=['TURBINE POWER', 'STORAGE POWER', 'STATE'])
SYSTEM_EFFICIENCY = []
calc_system_efficiency()
df['SYSTEM EFFICIENCY'] = SYSTEM_EFFICIENCY
df.to_csv('eff.csv', index=False)
