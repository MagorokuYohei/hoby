from sense_hat import SenseHat
import numpy as np

def get_mag():
	compass = sense.get_compass_raw()
	mag_y = compass['y']
	mag_x = compass['x']
	mag_z = compass['z']
	return mag_x, mag_y, mag_z	

def get_gyro():
	gyro = sense.get_gyroscope_raw()
	gyro_y = gyro['y']
	gyro_x = gyro['x']
	gyro_z = gyro['z']
	return gyro_x, gyro_y, gyro_z

def get_accel():
	accel = sense.get_accelerometer_raw()
	accel_y = accel['y']
	accel_x = accel['x']
	accel_z = accel['z']
	return accel_x, accel_y, accel_z



def main():
	sense.set_imu_config(True,True,True)	


	while(1):	
		mag_x, mag_y, mag_z = get_mag()
		gyro_x, gyro_y, gyro_z = get_gyro()
		accel_x, accel_y, accel_z = get_accel()
		hy = np.radians(40)
		hx = np.radians(30)
	
		sita = np.degrees( np.arctan2( (mag_x-hx), (mag_y-hy) ))

		print "Y %f"%mag_y
		print "X %f"%mag_x
		print "Z %f"%mag_z
		Azi = 90.0 - sita
		print sita
		print "********************"


if __name__=='__main__':
	sense = SenseHat()
	main()
