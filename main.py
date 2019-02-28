from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2


dataset = "c_memorable_moments.txt"




def weight(id1, id2):
	print(id1," ",id2,"\n")
	file = open(dataset)
	counter = 0
	for line in file:
	    line = line.strip()
	    attributes = line.split(None, 2)
	    #print(attributes)
	    if(counter == id1 ):
	    	tags1 = attributes[2].split()
	    	print("ciao")
	    if(counter == id2 ):
	    	tags2 = attributes[2].split()
	    	print("ciao")

	    counter += 1

	print(tags1)
	print(tags2)

	counter = 0
	for i in tags1:
		if i in tags2:
			counter += 1

	w = min([counter, len(tags1)-counter, len(tags2)-counter])
	if(w is not 0):
		m = 1./w * 10000
	else:
		m = 9999999999
	file.close()
	return int(m)



def create_distance_callback(dist_matrix):
  # Create a callback to calculate distances between cities.

  def distance_callback(from_node, to_node):
    return int(dist_matrix[from_node][to_node])

  return distance_callback

def distance_callback(from_node, to_node):
	return int(weight(from_node,to_node))

# Distance callback

def main():

  print("weight",weight(5,6))
  # Cities

  #city_names = ["1", "2", "3"]
  city_names = [str(i) for i in range(1000)]
  # Distance matrix
  dist_matrix = [
    [0, 10, 1], #1
    [10, 0, 1], #2
    [ 1, 1, 0]] #3

  tsp_size = len(city_names)
  num_routes = 1
  depot = 0

  print("Algorithm starts")
  # Create routing model
  if tsp_size > 0:
    routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
    # Create the distance callback.
    dist_callback = create_distance_callback(dist_matrix)
    routing.SetArcCostEvaluatorOfAllVehicles(weight)
    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
      # Solution distance.
      print("Total distance: " + str(assignment.ObjectiveValue()) + " miles\n")
      # Display the solution.
      # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
      route_number = 0
      index = routing.Start(route_number) # Index of the variable for the starting node.
      route = ''
      while not routing.IsEnd(index):
        # Convert variable indices to node indices in the displayed route.
        route += str(city_names[routing.IndexToNode(index)]) + ' -> '
        index = assignment.Value(routing.NextVar(index))
      route += str(city_names[routing.IndexToNode(index)])
      print("Route:\n\n" + route)
    else:
      print('No solution found.')
  else:
    print('Specify an instance greater than 0.')

if __name__ == '__main__':
  main()