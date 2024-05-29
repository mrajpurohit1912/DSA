from typing import List

class Graph:
    def __init__(self,edges) -> None:
        self.edges = edges
        self.graph_dict = {}

        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]


        print("Graph Dict: " , self.graph_dict)

    def get_paths(self,st,endss,path=[]):
        #print(type(path),type([start]))
        # print([path])
        # print([st])
        path = path + [st]

        if st == endss:
            return path
        
        if st not in self.graph_dict:
            return []

if __name__ == '__main__':
    routes = [("Mumbai","Paris"),
              ("Mumbai","Dubai"),
              ("Paris","Dubai"),
              ("Paris","New York"),
              ("Dubai","New York"),
              ("New York","Toranto"),
              ]
    
    first_graph = Graph(routes)

    sta = "Toranto"
    en = "Mumbai"
    
    print(first_graph.get_paths(st=sta,endss=en))


# from typing import List
# def get_list_length(data: List) -> int:
#   """
#   This function takes a List as input and returns its length.

#   Args:
#       data: The input data, which must be a List.

#   Returns:
#       The length (number of elements) of the input List.

#   Raises:
#       TypeError: If the input data is not a List.
#   """


#   if not isinstance(data, list):
#     raise TypeError("Input data must be a List")
  



#   return len(data)

# lst = []
  
# print(get_list_length(lst))