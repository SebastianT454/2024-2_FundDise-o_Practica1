# Clase Nodo y Lista Enlazada 

class LlNode:
  def __init__(self, index):
    #self.value = value
    self.index = index
    self.next = None

  def incrementIndex(self, amount = 1):
     self.index += amount

class LinkedList:
  def __init__(self):
    self.head = None
    self.size = -1

  def append(self, Node):
    if not self.head:
        self.size += 1
        self.head = LlNode(self.size)
        return
    
    if not Node.next:
        self.size += 1
        Node.next = LlNode(self.size)
        return
    
    self.append(Node.next)

  def traverse(self, CurrentNode):
      if not self.head:
          return
      
      print(f"Nodo Posicion: {CurrentNode.index}.")

      if not CurrentNode.next:
          print("-----------------------")
          return
      
      self.traverse(CurrentNode.next)

# Funcionalidades

# Utils.

def generateNodes(ll, Amount):
   for _ in range(Amount):
      ll.append(ll.head)

def updateNodeIndex(CurrentNode):
   CurrentNode.incrementIndex()

   if not CurrentNode.next:
      return
   
   updateNodeIndex(CurrentNode.next)


# 1) Insertar en el medio sin librerias recursivamente.

def e1(ll, CurrentNode, RequiredNodePos, LastNode = 0, PosNode = -1):
    # Recorrido recursivo hasta que se cumpla la condicion.
    # Complejidad O(1)

    if not ll.head:
        return
    
    if PosNode == RequiredNodePos:
        print("Mitad de la lista enlazada encontrada:", ll.size // 2, "//", "Tamano lista enlazada:", ll.size)
        NewNode = LlNode(PosNode)

        LastNode.next = NewNode
        NewNode.next = CurrentNode

        # Actualizar los indices a partir del nuevo nodo.
        updateNodeIndex(NewNode)
        return
    
    LastNode = CurrentNode
    
    e1(ll, CurrentNode.next, RequiredNodePos, LastNode, PosNode + 1)

# Generando un Objeto de Lista Enlazada y objetos de Nodo.
LinkedList_Obj = LinkedList()
generateNodes(LinkedList_Obj, 6)

# Insertando y actualizando indices a partir de e1 y imprimirlo.

e1(LinkedList_Obj, LinkedList_Obj.head, LinkedList_Obj.size // 2)
LinkedList_Obj.traverse(LinkedList_Obj.head)

# 2) Insertar al inicio sin librerias recursivamente.

def e2(ll):
    # Se cambia el head y luego se actualizan los indices.
    # Complejidad O(1)

    if not ll.head:
        return
    
    Head = ll.head

    ll.head = LlNode(0)
    ll.head.next = Head

    # Actualizar los indices a partir del nuevo nodo.
    updateNodeIndex(ll.head.next)
    return

# Generando un Objeto de Lista Enlazada y objetos de Nodo.
LinkedList_Obj = LinkedList()
generateNodes(LinkedList_Obj, 3)

# Cambiando el Head de la lista enzada, actualizar indices y imprimirlo.

e2(LinkedList_Obj)
LinkedList_Obj.traverse(LinkedList_Obj.head)

# 3) Insertar al inicio con un ciclo.

def e3(ll):
    # Se cambia el head y luego se actualizan los indices.
    # Complejidad O(n)

    if not ll.head:
        return
    
    Head = ll.head

    ll.head = LlNode(0)
    ll.head.next = Head

    # Actualizar los indices a partir del nuevo nodo.
    curNode = ll.head.next

    while curNode.next:
       curNode.incrementIndex()
       curNode = curNode.next

    curNode.incrementIndex()

    return

# Generando un Objeto de Lista Enlazada y objetos de Nodo.
LinkedList_Obj = LinkedList()
generateNodes(LinkedList_Obj, 9)

# Cambiando el Head de la lista enzada, actualizar indices y imprimirlo.

e3(LinkedList_Obj)
LinkedList_Obj.traverse(LinkedList_Obj.head)