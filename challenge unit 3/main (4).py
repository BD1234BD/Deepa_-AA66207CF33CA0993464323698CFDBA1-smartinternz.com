







def LinearsearchProduct(ProductList, TargetProduct): 
  indices =[]

  for index, product in enumerate(ProductList):
   if product == TargetProduct: 
     indices.append(index)


  return indices


# Example usage:
products =["shoes", "boot","loafer","shoes","sadal","shoes"]
target ="shoes" 
target2 ="apple"
result=LinearsearchProduct(products,target)
print (result)


