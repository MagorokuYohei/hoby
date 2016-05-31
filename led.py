from sense_hat import SenseHat
import time

def main():
	sense = SenseHat()
	"""
	sense.show_message("Hello World!!");
	sense.set_rotation(180)
	sense.show_message("Hello World!!");
	"""
	sense.flip_v()
	list = sense.get_pixels()
	#print list

	sense.set_pixel(0,0,255,0,0)
	sense.clear()
 	for i in range(0, 5):
		sense.show_letter(str(i))
		time.sleep(1)	
	sense.clear()	

if __name__=='__main__':
	main()
