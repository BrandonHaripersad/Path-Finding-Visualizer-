import pygame
import math
import random
import copy
try:
   import queue
except ImportError:
   import Queue as queue

pygame.init()

WIDTH = 5
HEIGHT = 5
MARGIN = 1

win = pygame.display.set_mode((600, 600))
walls = []

class Node:

    def __init__(self, x, y, rect=None, wall=False):
        self.x = x
        self.y = y
        self.rect = rect
        self.wall = wall

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

def createWalls(nodes, walls):
    random.seed(1)
    for row in nodes:
        for col in row:
            value = random.random()
            if value < 0.3:
                col.wall = True
                walls.append(col)
    return walls

def findPath(startNode, endNode, nodes):
    start = startNode
    end = endNode

    if start.wall == True:
        walls.remove(start)
        start.wall = False

    if end.wall == True:
        walls.remove(end)
        end.wall = False

    pygame.draw.rect(win, pygame.Color("#ff6361"), end.rect)
    pygame.display.update()

    path = queue.Queue()
    path.put([])
    
    lastPath = []
    put = []
    traversed = []

    while not foundEnd(lastPath, endNode):
        if path.empty():
            print("No Path")
            break
        lastPath = path.get()
        # drawPath(lastPath)
        for i in ["L", "R", "U", "D"]:
            if validMove(startNode, lastPath, nodes, traversed, walls, i):
                node = getNode(startNode, lastPath, nodes, i)
                traversed.append(node)
                pygame.draw.rect(win, pygame.Color("#58508d"), node.rect)
                pygame.display.update()
                put = lastPath.copy()
                put.append(node)
                path.put(put)
                put = []
                pygame.draw.rect(win, pygame.Color("#ff6361"), start.rect)
                pygame.display.update()
            else:
                continue

    pygame.draw.rect(win, pygame.Color("#58508d"), start.rect)
    pygame.display.update()
    
    for i in lastPath:
        pygame.draw.rect(win, pygame.Color("#ffa600"), i.rect)
        pygame.display.update()

    return lastPath

def foundEnd(lastPath, endNode):
    if len(lastPath) == 0:
        return False
    elif lastPath[-1] == endNode:
        return True
    else:
        return False

def validMove(startNode, lastPath, nodes, traversed, walls, dir):
    if len(lastPath) == 0:
        if dir == "L":
            if Node(startNode.x, startNode.y - 1) in nodes[startNode.x] and not(Node(startNode.x, startNode.y - 1) in walls):
                return True
        if dir == "R":
            if Node(startNode.x, startNode.y + 1) in nodes[startNode.x] and not(Node(startNode.x, startNode.y + 1) in walls):
                return True
        if dir == "U":
            if Node(startNode.x - 1, startNode.y) in nodes[startNode.x + 1] and not(Node(startNode.x - 1, startNode.y) in walls):
                return True
        if dir == "D":
            if Node(startNode.x + 1, startNode.y) in nodes[startNode.x - 1] and not(Node(startNode.x + 1, startNode.y) in walls):
                return True
    else:
        lastNode = lastPath[-1]
        if dir == "L":
            if any(Node(lastNode.x, lastNode.y - 1) in node for node in nodes) and not(Node(lastNode.x, lastNode.y - 1) in lastPath) and not(Node(lastNode.x, lastNode.y - 1) in traversed) and not(Node(lastNode.x, lastNode.y - 1) in walls):
                return True
        if dir == "R":
            if any(Node(lastNode.x, lastNode.y + 1) in node for node in nodes) and not(Node(lastNode.x, lastNode.y + 1) in lastPath) and not(Node(lastNode.x, lastNode.y + 1) in traversed) and not(Node(lastNode.x, lastNode.y + 1) in walls):
                return True
        if dir == "U":
            if any(Node(lastNode.x - 1, lastNode.y) in node for node in nodes) and not(Node(lastNode.x - 1, lastNode.y) in lastPath) and not(Node(lastNode.x - 1, lastNode.y) in traversed) and not(Node(lastNode.x - 1, lastNode.y) in walls):
                return True
        if dir == "D":
            if any(Node(lastNode.x + 1, lastNode.y) in node for node in nodes) and not(Node(lastNode.x + 1, lastNode.y) in lastPath) and not(Node(lastNode.x + 1, lastNode.y) in traversed) and not(Node(lastNode.x + 1, lastNode.y) in walls):
                return True
    return False

def getNode(startNode, lastPath, nodes, dir):
    if len(lastPath) == 0:
        if dir == "L":
            return nodes[startNode.x][startNode.y - 1]
        if dir == "R":
            return nodes[startNode.x][startNode.y + 1]
        if dir == "U":
            return nodes[startNode.x - 1][startNode.y]
        if dir == "D":
            return nodes[startNode.x + 1][startNode.y]
    else:
        lastNode = lastPath[-1]
        if dir == "L":
            return nodes[lastNode.x][lastNode.y - 1]
        if dir == "R":
            return nodes[lastNode.x][lastNode.y + 1]
        if dir == "U":
            return nodes[lastNode.x - 1][lastNode.y]
        if dir == "D":
            return nodes[lastNode.x + 1][lastNode.y]

def drawGrid(nodes, win):
    for row in nodes:
        for col in row:
            cord = [(MARGIN + WIDTH) * col.x + MARGIN, (MARGIN + HEIGHT) * col.y + MARGIN, WIDTH, HEIGHT]
            col.rect = cord
            if col.wall == True:
                 pygame.draw.rect(win, pygame.Color("#000000"), [(MARGIN + WIDTH) * col.x + MARGIN, (MARGIN + HEIGHT) * col.y + MARGIN, WIDTH, HEIGHT])
                 pygame.display.update()
            else:
                pygame.draw.rect(win, pygame.Color("#003f5c"), [(MARGIN + WIDTH) * col.x + MARGIN, (MARGIN + HEIGHT) * col.y + MARGIN, WIDTH, HEIGHT])
                pygame.display.update()

def drawPath(path):
    for i in path:
        pygame.draw.rect(win, (50, 25, 75), i.rect)
        pygame.display.update()

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
    intilization() 
    T = createNodeGrid(100, 100)
    createWalls(T, walls)
    drawGrid(T, win)
    findPath(T[0][0], T[49][99], T)
    game_loop()
   
    pygame.display.update()

  
if __name__=="__main__":
    main()