import numpy as np


class numpy_map():

    def __init__(self, init_value=0, dtype=int):
        self.dtype = dtype
        self.init_value = init_value
        self.height = 4
        self.width = 4
        self.nmap = np.full((self.height,self.width), init_value, dtype=dtype)
        self.start = (1,1)
    
    def _is_in_range(self, key):
        return not (key[0] < -self.start[0] or key[0] >= self.height - self.start[0]
                    or key[1] < -self.start[1] or key[1] >= self.width - self.start[1])

    def __getitem__(self, key):
        if not self._is_in_range(key):
            return self.init_value
        return self.nmap[key[O]+self.start[0], key[1]+self.start[1]]
    
    def __setitem__(self, key, item):
        resized = False
        while not resized:
            if key[0] < -self.start[0]:
                self.nmap = np.append(np.full((self.height,self.width),
                                              self.init_value,
                                              dtype=self.dtype),
                                      self.nmap,
                                      axis=0)
                self.start = (self.start[0]+self.height, self.start[1])
                self.height *= 2
            
            elif key[0] >= self.height - self.start[0]:
                self.nmap = np.append(self.nmap,
                                      np.full((self.height,self.width),
                                              self.init_value,
                                              dtype=self.dtype),
                                      axis=0)
                self.height *= 2
            
            elif key[1] < -self.start[1]:
                self.nmap = np.append(np.full((self.height,self.width),
                                              self.init_value,
                                              dtype=self.dtype),
                                      self.nmap,
                                      axis=1)
                self.start = (self.start[0], self.start[1]+self.width)
                self.width *= 2
            
            elif key[1] >= self.width - self.start[1]:
                self.nmap = np.append(self.nmap,
                                      np.full((self.height,self.width),
                                              self.init_value,
                                              dtype=self.dtype),
                                      axis=1)
                self.width *= 2
            
            else:
                resized = True
        self.nmap[key[0]+self.start[0], key[1]+self.start[1]] = item
    
    def __repr__(self):
        return str(self.nmap)
    
    def pretty_str(self):
        return "\n".join(map(lambda x: "".join(x), self.nmap))
                

        