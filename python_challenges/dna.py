class DNA:
    def __init__(self, strand):
        self.strand = strand
        self.length = len(strand)
    
    def hamming_distance(self, other):
        if not isinstance(other, str):
            return NotImplemented
        
        min_length = min(len(other), self.length)
        
        distance = 0
        for i in range(min_length):
            if self.strand[i] != other[i]:
                distance += 1
        
        return distance
