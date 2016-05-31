from sense_hat import SenseHat

def main():
	sense = SenseHat()
	temp = sense.get_temperature()
	print "temp_from_temperat:%s"%temp
	print "temp_from_humidity:%s"%sense.get_temperature_from_humidity()
	print "temp_from_pressure:%s"%sense.get_temperature_from_pressure()
if __name__=='__main__':
	main()
