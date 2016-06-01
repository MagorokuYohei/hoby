from sense_hat import SenseHat
import numpy as np
import time


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

	deg_x, deg_y, deg_z =0,0,0

	while(1):	
		mag_x, mag_y, mag_z = get_mag()
		gyro_x, gyro_y, gyro_z = get_gyro()
		accel_x, accel_y, accel_z = get_accel()
		
		sita = np.degrees( np.arctan2(accel_x, (np.sqrt(accel_y*accel_y + accel_z*accel_z))))
		print sita
		psai = np.degrees( np.arctan2(accel_y, (np.sqrt(accel_x*accel_x + accel_z*accel_z))))
		print psai

		deg_x += np.degrees(gyro_x)*0.1
		deg_y += np.degrees(gyro_y)*0.1
		deg_z += np.degrees(gyro_z)*0.1
		print "gyro**************"
		print deg_x
		print deg_y
		print deg_z
		print "********************"
		time.sleep(0.1)

if __name__=='__main__':
	sense = SenseHat()
	main()
