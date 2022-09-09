import numpy as np
class layout:
    
    def __init__(self, file_path):
        
        self.layout_mat = self.__read_layout_file(file_path)
        self.length_layout = self.layout_mat.shape[0]
        self.width_layout = self.layout_mat.shape[1]
        self.rack_position_list = self.__positions_with_racks(self.layout_mat)
        self.pos_to_product_dict = {}

    def __read_layout_file(self, file_path):
        # read file layout file and converts it to a numpy matrix
        with open(file_path, 'r') as f:
            text = f.read()
        text_split = [[int(c) for c in line] for line in text.split('\n')]
        return np.array(text_split)

    def __positions_with_racks(self, layout_mat):
        #return a list of tuples (i,j) indicating position of racks
        rows, columns = np.where(layout_mat == 1)
        return [(i,j) for i,j in zip(rows, columns)]


