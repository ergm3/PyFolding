# constants
IDEAL_GAS_CONSTANT_KCAL = 1.987204118E-3
TEMPERATURE_CELSIUS = 25.

# calculated constants
TEMPERATURE_KELVIN = 273.15 + TEMPERATURE_CELSIUS
RT = IDEAL_GAS_CONSTANT_KCAL * TEMPERATURE_KELVIN

# error
FITTING_PENALTY = 1e10

if __name__ == "__main__":
	pass