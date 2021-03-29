# -*- coding: utf-8 -*-
"""wikigame3.ipynb

Author: Rohan Dawar
Email: dawar.rohan1@gmail.com

## WHAT THIS SCRIPT DOES:
Given a home wikipedia article with the format '/wiki/{article name}' in the variable home
Given a target wikipedia article with the format '/wiki/{article name}' in the variable target
Begins a Breadth First Search (BFS) with 'children' nodes consisting of valid wikipedia articles directly linked in the 'parent' node
Once target is found, return number of articles searched and the chain of articles back to the home article
"""

base_url = 'https://en.wikipedia.org'

home = '/wiki/Sydney'

target = '/wiki/Melbourne'

# Dependencies
import requests
from bs4 import BeautifulSoup
from os import system, name

def clear():
	'''
	Function to clear output on windows, mac, unix systems once target is found
	'''
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
	try:
		from IPython.display import clear_output
		clear_output()


def parse2node(element):
'''
  Given: BS4 'a' element
  Return: node string of /wiki Article
  '''
  filterTypes = ['.jpg', '.ogg', '.svg', '.png', '.tif', '.gif', '.ogv', 'jpeg', '.oga']
  node = element['href']
  if node[:5] == '/wiki' and node[-4:].lower() not in filterTypes:
    return node

def get_children(ext):
  '''
  Given: wikipedia url extension
  Return: list of child wiki article hrefs, if no child articles, return empty list
  '''
  try:
    r = requests.get(base_url + ext)
    soup = BeautifulSoup(r.text, 'html.parser')
    s = soup.find_all('a', href=True)
    q = [i for i in list(map(parse2node, s)) if i]
    return q
  except:
    return []

class Node:
  instances, checked = [], []                 # list of all Node instances, list of Node names checked
  def __init__(self, name, parent):
    self.__class__.instances.append(self)
    self.name = name                          # the name (wikilink str of the node itself)
    self.parent = parent                      # the parent node (None if home)

def find_parent_chain(node):
	'''
	Recursive fn appending to parentchain list until home (current parent = None)
	'''
  currentparent = node.parent
  if currentparent:
    parentchain.append(currentparent.name)
    find_parent_chain(currentparent)

def check_node(node, target, count):
	'''
	Checks if node is target, if so finds parent chain and stops function with global flag
	Otherwise adds node name to list of checked nodes
	'''
  global flag
  if node.name == target:
    clear()
    global parentchain
    parentchain = []
    flag = node
    find_parent_chain(flag)
    print(f"Target found {flag.name}, Chain Back Home: {parentchain}, Checked {count} Pages")
    return flag
  else:
    print(f'{count} {node.name}')
    Node.checked.append(node.name)   # add node name to list of checked nodes

def main(home, target):
	'''
	Main loop kicks of Node.instances which will loop until target is found or all layers of children are searched
	If not flag: list comprehension that creates new node, appending to Node.instances and gets children of that node
	'''
  global flag
  flag = None
  Node(home, None)

  for count, node in enumerate(Node.instances):
    if node.name not in Node.checked:
      f = check_node(node, target, count)
      if not flag:
        [Node(child, node) for child in get_children(node.name) if child not in Node.checked]
      else:
        return

  if not flag:
    print('Target not found')

main(home, target)