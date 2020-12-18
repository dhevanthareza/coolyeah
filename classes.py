class Product:
  productName: str
  price: int
  purchasePrice: int
  stock: int
  
  def __init__(self, productName: str, price: int, purchasePrice: int, stock: int):
    self.productName = productName
    self.price = price
    self.purchasePrice = purchasePrice
    self.stock = stock
  def addStock(self):
    self.stock += 1
  def reduceStock(self):
    self.stock = self.stock - 1

Piatos = Product('piatos', 15000, 10000, 10)
print(Piatos.productName) #piatos
print(Piatos.price) #15000
print(Piatos.purchasePrice) #10000
print(Piatos.stock) #10

Piatos.addStock()
print(Piatos.stock) # 11
  