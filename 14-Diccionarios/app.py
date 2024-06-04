cliente = {'nombre':'Jose', 'apellido':'Diaz', 'peso':88, 'talla':1.75}
print(type(cliente))
consulta = (cliente['apellido'])
print(consulta)

#otro ejemplo
dic = {'c1':55, 'c2':[30,40,50],'c3':{'s1':100, 's2':200}}
print(dic['c3']['s2'])

#mostrar las propiedades y agreagar el metodo
dic2 = {'c1':['a','b','c'],'c2':['d','f','g']}
print(dic2['c1'][0].upper())




#agregar elementos a un diccionario
dic3 = {1:'a',2:'b'}
print(dic3)

dic3[3] = 'c'
print(dic3)

#modificar
dic3[2] = 'B'
print(dic3)

print(dic3.keys())
print(dic3.values())
print(dic3.items())