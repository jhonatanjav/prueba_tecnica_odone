#PRUEBA TECNICA PRÁCTICA DE ODONE

# 1 AGRUPACION DE OBJETOS:-----------------------------------------------------------------------------------------------

def agrupar_productos(productos):
   #DICCIONARIO PRODUCTOS
    agrupados = {}

        
    for i, producto in enumerate(productos, 1):
        fabricante = producto['Fabricante']
        categoria = producto['Categoría']
        genero = producto['Género']

        
        if fabricante not in agrupados:
            agrupados[fabricante] = {}
        if categoria not in agrupados[fabricante]:
            agrupados[fabricante][categoria] = {}
        if genero not in agrupados[fabricante][categoria]:
            agrupados[fabricante][categoria][genero] = []

   
        agrupados[fabricante][categoria][genero].append(f"Producto {i}")

    return agrupados
productos = [
    {"Nombre": "Zapatos XYZ", "Código de barras": 8569741233658, "Fabricante": "Deportes XYZ", "Categoría": "Zapatos", "Género": "Masculino"},
    {"Nombre": "Zapatos ABC", "Código de barras": 7452136985471, "Fabricante": "Deportes XYZ", "Categoría": "Zapatos", "Género": "Femenino"},
    {"Nombre": "Camisa DEF", "Código de barras": 5236412896324, "Fabricante": "Deportes XYZ", "Categoría": "Camisas", "Género": "Masculino"},
    {"Nombre": "Bolso KLM", "Código de barras": 5863219635478, "Fabricante": "Carteras Hi-Fashion", "Categoría": "Bolsos", "Género": "Femenino"},
]


resultado = agrupar_productos(productos)
print(resultado)

# 2 MANEJO DE ERRORES----------------------------------------------------------------------------------------------------------------------

#Se podria manejar el error utilizando try except
#ejemplo:

#diccionario = {"nombre": "Pedro", "edad":"20"}
#try:
    #print(diccionario["direccion"])      LA "direccion" SERIA LA CLAVE QUE NO EXISTE EN EL DICCIONARIO
#except KeyError:
    #print("La clave 'direccion' no existe en el diccionario.")

#JUSTIFICACION: try except comunmente se utiliza para que el programa no se detenga por un error, sino que se puede dar mensaje indicando sobre el error

#3 CALCULAR DESCUENTO APLICABLE:---------------------------------------------------------------------------------------------------------------------------------


def calcular_descuento(total_venta):
    
    if total_venta > 500:
        return 10  
    elif 100 <= total_venta <= 500:
        return 5  
    else:
        return 0  


# Ejemplo

try:
    total_venta = float(input("Ingresa el total de la venta: $"))
   
    descuento = calcular_descuento(total_venta)
    print(f"El porcentaje de descuento para una venta de ${total_venta:.2f} es de {descuento}%")
except ValueError:
    print("ingrese valor numerico para el total de la venta.")


#MANIPULACION DE DATOS CON PYTHON----------------------------------------------------------------------------
#     SELECT order_id, amount_total, customer_name
#     FROM orden_de_venta
#     WHERE amount_total > 1000;


#CONSULTA SQL-------------------------------------------------------------------------------------
#*SELECT DISTINCT
#    e.EmployeeID,
#    e.FirstName,
#    e.LastName,
#    o.OrderID,
#    p.ProductName,
#    c.CategoryName
#FROM Employees e
#JOIN Orders o ON e.EmployeeID = o.EmployeeID
#JOIN OrderDetails od ON o.OrderID = od.OrderID
#JOIN Products p ON od.ProductID = p.ProductID
#JOIN Categories c ON p.CategoryID = c.CategoryID
#WHERE c.CategoryName = 'Beverages';



#  Beverages en tabla categories