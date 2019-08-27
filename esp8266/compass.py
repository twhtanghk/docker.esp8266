from hmc5883l import HMC5883L

sensor = HMC5883L(scl=5, sda=4)

def heading():
  x, y, z = sensor.read()
  return sensor.heading(x, y)
