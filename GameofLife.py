class Life:

	def __init__(self, X = 10, Y = 10, T = 25): #X, Y = rows and columns, T = max iterations
		self.X = X
		self.Y = Y
		self.T = T;
		self.state = [[0] * X for i in range(Y)] #create empty arrays for initial and old game states
		self.stateNew = self.state #array stores 0 for dead or 1 for life to simplify summing neighbours
		#self.state[5][5] = 1; self.state[6][3] = 1; self.state[6][5] = 1; self.state[7][4] = 1; self.state[7][5] = 1 #plugging in some values to create a glider
		self.state[5][5] = 1; self.state[5][6] = 1; self.state[5][7] = 1#plugging in some values to create a blinker
		Life.output(self.state,X,Y) #output initial state

		Life.main(self) #execute main loop
	def countNeighbours(self,x,y):
		
		
		i = [x-1,x,x+1] #coordinates of neighbours to sum
		j = [y-1,y,y+1]
		
		for c in range(3): #if the coordinates spill over the edge of the grid, adjust them to loop them around for infinite grid
			if i[c] == self.X: i[c] = 0
			if i[c] < 0: i[c] = self.X-1
			if j[c] == self.Y: j[c] = 0
			if j[c] < 0: j[c] = self.Y-1
		
		neigh = 0 #placeholder for neighbour count

		for ic in i: #sum neighbouring cells for number of living neighbours
			for jc in j:
				if ic != x or jc != y: #condition to avoid counting centre cell
					neigh += self.state[jc][ic]
		
		return neigh

	
	def output(state,X,Y): # create output, X for living cell, . for dead/empty
		out = ''
		
		for m in range(X):
			for n in range(Y):
				if state[n][m] == 1: out += 'X '
				else: out += '. '
				
		
			out += '\n'
		
		print(out)
		
	def main(self):

		for t in range(self.T):
		
			self.stateNew = [[0] * self.X for i in range(self.Y)] #reset new array
			for m in range(self.X):
				for n in range(self.Y):
				
					neigh = Life.countNeighbours(self,m,n) # fetch number of neighbouring cells
				
					if(neigh==3 or (neigh == 2 and self.state[n][m] == 1)): self.stateNew[n][m] = 1 #all scenarios/rules captured within this line
		
			Life.output(self.stateNew,self.X,self.Y)
			self.state = self.stateNew # relegate new state to old state in preparation for next loop

Life()
