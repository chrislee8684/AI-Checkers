class node: #each state = node
    def __init__(self, row_move, column_move, piece, choice_num): #postion of legal move, piece that moves, and evaluation
        self.row_move = row_move
        self.column_move = column_move
        self.piece = piece
        self.choice_num = choice_num
        # self.eval = eval
        self.depth = 0
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        child.depth = self.depth+1

    def apply(self): #applies move to piece
        pass

    #def print_tree(self):
    #    print(self.row,self.column)


stasdart = node(0,0,0,0) #temp. start node
