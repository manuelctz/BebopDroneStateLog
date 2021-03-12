from pyparrot.Bebop import Bebop


class Drone:
	def __init__(self):
		self.drone = Bebop()

	def take_off(self):
		### Connect to Bebop drone and take off ###
		success = self.drone.connect1(10)
		print(success)
		self.drone.safe_takeoff(2)

	def step(self, roll, pitch, yaw, vertical_movement, duration):
		### Moves the Bebop drone given input parameters ###
		self.drone.fly_direct(self, roll, pitch, yaw, vertical_movement, duration)

	def square(self):
		### Move the drone in a square pattern###
		#move left and wait 1 second
		self.drone.fly_direct(self, roll=-15, pitch=0, yaw=0, vertical_movement=0, duration=1)
		self.drone.smart_sleep(1)
		#move forward and wait 1 second
		self.drone.fly_direct(self, roll=0, pitch=15, yaw=0, vertical_movement=0, duration=1)
		self.drone.smart_sleep(1)
		#move right and wait 1 second
		self.drone.fly_direct(self, roll=15, pitch=0, yaw=0, vertical_movement=0, duration=1)
		self.drone.smart_sleep(1)
		#move back and wait 1 second
		self.drone.fly_direct(self, roll=0, pitch=-15, yaw=0, vertical_movement=0, duration=1)
		self.drone.smart_sleep(1)

	def zigzag(self):
		### Move the drone in a 3D zigzag pattern###
		#move left-forward-up and wait 1 second
		self.drone.fly_direct(self, roll=-15, pitch=15, yaw=0, vertical_movement=15, duration=1)
		self.drone.smart_sleep(1)
		#move right-forward-down and wait 1 second
		self.drone.fly_direct(self, roll=15, pitch=15, yaw=0, vertical_movement=-15, duration=1)
		self.drone.smart_sleep(1)
		#move left and wait 1 second
		self.drone.fly_direct(self, roll=-15, pitch=0, yaw=0, vertical_movement=0, duration=1)
		self.drone.smart_sleep(1)
		#move right-back-up and wait 1 second
		self.drone.fly_direct(self, roll=15, pitch=-15, yaw=0, vertical_movement=15, duration=1)
		self.drone.smart_sleep(1)
		#move left-back-down and wait 1 second
		self.drone.fly_direct(self, roll=-15, pitch=-15, yaw=0, vertical_movement=-15, duration=1)
		self.drone.smart_sleep(1)

	def disconnect(self):
		### Disconect Bebop drone ###
		self.drone.disconnect()

	def land(self):
		### Disconnect Bebop drone and land ###
		success = self.drone.connect1(10)
		print(success)
		self.drone.ask_for_state_update()
		self.drone.safe_land(5)
		self.drone.disconnect()


if __name__ == "__main__":
    
    uav = Drone()
    uav.take_off()
    uav.square()
    uav.land()
