class Physics():
	def __init__(self):
		#----------------------- Constants -----------------------||
		#speed of light
		self.c = 2.99792458 * (10 ** 8)# metres per second
		# Earth's gravity
		self.g = 9.81# metres per second
		return
	#----------------------- Forces and Motion -----------------------||
	# Einstein's Theory of Relativity
	def energy(m):
		# energy = mass * speed of light squared
		# e = m * math.pow(c,2)
		e = m * (self.c ** 2)
		return e

	def acceleration(velocity, velocity2, time):
		# acceleration = change in velocity ÷ time
		# a = (v-u) / t
		a = (velocity - velocity2) / time
		return a

	# Newton's Second Law of Motion
	def force(m,a):
		F = m * a
		return F

	def speed(distance,time):
		# speed = distance ÷ time.
		s = distance / time
		return s

	def weight(self, mass):
		w = mass * self.gravity
		return w
	     
	def density(mass,volume):
		d = mass / volume
		return d

	def momentum(mass, velocity):
		p = mass * velocity
		return p

	def pressure(force,area):
		# pressure = force ÷ area
		p = force / area
		return p

	'''
	(mv - mu) = F x t.     change in momentum = Force x time.
	m = F x d.     moment = force x perpendicular distance from pivot
	'''
	#----------------------- Electro-Magnetism -----------------------||

	'''
	Maxwell's Equations
	Gauss's law: Electric charges produce an electric field. ...
	Gauss's law for magnetism: There are no magnetic monopoles. ...
	Faraday's law: Time-varying magnetic fields produce an electric field.
	Ampère's law: Steady currents and time-varying electric fields (the latter due to Maxwell's correction) produce a magnetic field.
	'''

	#Electricity

	def power(voltage, current):
		#P = V x I
		P = voltage * current
		return P

	def power(voltage, current):
		#V = I x R.    voltage = current x resistance
		V = current * resistance
		return V

	#Q = I x t.     charge = current x time
	#E = V x Q.     energy = voltage x charge
	#E = V x I x t.     energy = voltage x current x time

	#Transformer Equation
	#Total cost  =  number of units x cost per unit.



	#----------------------- Energy -----------------------||
	'''
	Efficiency (%)  =  (useful energy out ÷ total energy in) x 100.
	GPE = mgh.      GPE = mass x gravity x height.
	KE  =  ½mv2.     Kinetic Energy = 0·5 x mass x velocity2.
	W = F x d.      work done = force x distance.   
	W = E.      work done = energy transferred.
	P = E ÷ t.      power = energy ÷ time.            
	E = c x m x θ.   energy = specific heat capacity x mass x change in temperature.
	'''





	#----------------------- Waves -----------------------||
	# v = f x λ.     velocity  =  frequency  x  wavelength


	'''
	engineering forces:
		friction
	 	leverage
	'''

	# l (string theory)

	'''
	Gravity
	Electro-Magnetism
		Electricity and magnetism
	Weak Nuclear
		Responsible for the radioactive decay of subatomic particles
	Strong Nuclear
		Binds the component particles of an atom's nucleus

	maxwell's equations - the equations of light

	antimatter
		positron (anti-electron) has a positive charge
		CERN has detected anti-helium 
		when antimatter and matter combine, they create a huge force
	'''



	'''
	particle zoo - the standard model
	string theory is the bit below this
	string field theory - michio kaku
	sparticles: super particles
	'''

if __name__ == '__main__':
	#print('The speed of light:',c,'m/s')
	#print('Gravity: ',g,'m/s')
	p = Physics()
	print(p.c)