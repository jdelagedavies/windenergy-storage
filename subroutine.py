from typing import Any, Union


def calc_air_density(air_pressure, air_temperature, relative_humidity):
    # Assuming all values are in SI units
    saturation_vapor_pressure = 6.1078 * 10 ** (7.5 * air_temperature / (air_temperature + 237.3))
    water_vapor_pressure = saturation_vapor_pressure * relative_humidity
    dry_air_pressure = air_pressure - water_vapor_pressure
    DRY_AIR_SPECIFIC_GAS_CONSTANT = 287.058
    WATER_SPECIFIC_GAS_CONSTANT = 461.495
    air_density = (dry_air_pressure / (DRY_AIR_SPECIFIC_GAS_CONSTANT * air_temperature)) +\
                  (water_vapor_pressure / (WATER_SPECIFIC_GAS_CONSTANT * air_temperature))
    air_density: Union[float, Any] = round(air_density, 6)
    return air_density


def calc_wind_turbine_power(air_density, wind_speed):
    # Assuming all values are in SI units
    SWEEP_AREA = 21900  # For wind turbine SG 8.0-167 DD
    REAL_EFFICIENCY = 0.3  # Assumed for the time being due to the lack of available data
    available_wind_power = 0.5 * air_density * wind_speed ** 3 * SWEEP_AREA
    wind_turbine_power: Union[float, Any] = REAL_EFFICIENCY * available_wind_power
    wind_turbine_power = round(wind_turbine_power, 6)
    return wind_turbine_power
