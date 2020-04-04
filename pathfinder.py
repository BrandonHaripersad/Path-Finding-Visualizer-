import pygame
import math


pygame.init()

WIDTH = 10
HEIGHT = 10
MARGIN = 1


class Node:

    def __init__(self, x, y, rect=None):
        self.x = x
        self.y = y
        self.rect = rect

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
        return False

def createNodeGrid(rows, cols):
    nodes = []
    i = 0
    p = 0
    while i < rows:
        nodes.insert(i,[])
        while p < cols:
            nodes[i].insert(p, Node(i,p))
            p = p + 1
        i = i + 1
        p = 0
    return nodes

def findPath(startNode, endNode, nodes):
    start = startNode
    end = endNode

    path = queue.Queue()
    path.put([])

    lastPath = []
    
    while not foundEnd(lastPath, endNode):
        lastPath = path.get()
        for i in ["L, R, U, D"]:
            if validMove(startNode, lastPath, nodes, i):
                node = getNode(startNode, lastPath, nodes, i)
                lastPath.apppend(node)
                path.put(lastPath)

    return path

def validMove(startNode, lastPath, nodes, dir):
    if len(lastPath) == 0:
        if dir == "L":
            if any(Node(startNode.x, startNode.y - 1) in node for node in nodes):
                return True
        if dir == "R":
            if Node(startNode.x, startNode.y + 1) in nodes[startNode.x]:
                return True
        if dir == "U":
            if Node(startNode.x + 1, startNode.y) in nodes[startNode.x + 1]:
                return True
        if dir == "D":
            if Node(startNode.x - 1, startNode.y) in nodes[startNode.x - 1]:
                return True
    else:
        lastNode = lastPath[-1]
        if dir == "L":
            if any(Node(lastNode.x, lastNode.y - 1) in node for node in nodes):
                return True
        if dir == "R":
            if any(Node(lastNode.x, lastNode.y + 1) in node for node in nodes):
                return True
        if dir == "U":
            if any(Node(lastNode.x + 1, lastNode.y) in node for node in nodes):
                return True
        if dir == "D":
            if any(Node(lastNode.x - 1, lastNode.y) in node for node in nodes):
                return True
    return False

def getNode(startNode, lastPath, nodes, dir):
    if len(lastPath) == 0:
        if dir == "L":
            return nodes[startNode.x][startNode.y - 1]
        if dir == "R":
            return nodes[startNode.x][startNode.y + 1]
        if dir == "U":
            return nodes[startNode.x + 1][startNode.y]
        if dir == "D":
            return nodes[startNodes.x - 1][startNode.y]
    else:
        lastNode = lastPath[-1]
        if dir == "L":
            return nodes[lastNode.x][lastNode.y - 1]
        if dir == "R":
            return nodes[lastNode.x][lastNode.y + 1]
        if dir == "U":
            return nodes[lastNode.x + 1][lastNode.y]
        if dir == "D":
            return nodes[lastNode.x - 1][lastNode.y]

def isStartNode(self, x, y):
    pass   

def endNode(x, y):
    pass

def drawGrid(nodes, win):
    rect_list = []
    i = 0
    for row in nodes:
        rect_list.insert(i, [])
        for col in row:
            cord = [(MARGIN + WIDTH) * col.x + MARGIN, (MARGIN + HEIGHT) * col.y + MARGIN, WIDTH, HEIGHT]
            rect = pygame.draw.rect(win, (255, 0, 0), [(MARGIN + WIDTH) * col.x + MARGIN, (MARGIN + HEIGHT) * col.y + MARGIN, WIDTH, HEIGHT])
            rect_list[i].insert(col.y, rect)
            col.rect = cord
            pygame.display.update()
        i = i + 1
    return rect_list


# Pygame and window set up below

def intilization():
    pygame.display.set_caption("Path Finder")

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def main():
    win = pygame.display.set_mode((1000, 1000))
    intilization() 
    T = createNodeGrid(5, 5)
    rect_list = drawGrid(T, win)
    print(rect_list)
    print(T)
    print(T[0][0])
    print(validMove(T[0][0], [], T, "L"))
    game_loop()
   
    pygame.display.update()

  
if __name__=="__main__":
    main()