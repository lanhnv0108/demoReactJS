from flask import Flask, jsonify, request
import os
import BusinessObjects as bo
import DataObjects as do

app = Flask(__name__)

db_ip = os.getenv('db_ip') #'10.0.2.15'
ConnectionData = {}
ConnectionData['user'] = 'postgres'
ConnectionData['password'] = 'postgres'
ConnectionData['host'] = str(db_ip)
ConnectionData['port'] = '5432'
ConnectionData['database'] = 'thigiuaki'

@app.route('/')
def hello():    
    #return 'this is backend'
    c1 = bo.Customer(1, 'DAU xanh', 'Peter', '566 Nui Thanh', 'Danang', '50000', 'Vietnam')
    return c1.City

@app.route('/customer_insert')
def test_insert():
    #ConnectionString = 'database=northwind user=postgres password=postgres host=10.0.2.15 port=5432'
    c2 = do.Customer(ConnectionData)
    c1 = bo.Customer(1, 'Lanh', 'Nguyen', '566 Nui Thanh', 'Danang', '50000', 'Vietnam')
    s1 = c2.insert(c1)
    return s1
    
@app.route('/ca_insert')
def test_insertca():
    #ConnectionString = 'database=northwind user=postgres password=postgres host=10.0.2.15 port=5432'
    c2 = do.Categories(ConnectionData)
    c1 = bo.Categories(1 , 'hello' , 'dadadad')
    s1 = c2.insert(c1)
    return s1

# CUSTOMER API
# Insert
@app.route('/customer/insert', methods=['POST'])
def user_insert():
    data = request.json
    c1 = bo.Customer(data['CustomerID'], 
                            data['CustomerName'],
                            data['ContactName'], 
                            data['Address'], 
                            data['City'], 
                            data['PostalCode'], 
                            data['Country'])
    c2 = do.Customer(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200



#Show all item from Customer
@app.route('/customer/all_Customer')
def get_all_user():
    result = do.Customer(ConnectionData).get_all()
    return jsonify(result), 200
# --------------------

# Delete customer
@app.route('/customer/delete/<int:customer_id>' , methods=['DELETE'])
def delete_user_by_id(customer_id):
    c = bo.Customer(CustomerID = customer_id)
    result = do.Customer(ConnectionData).delete(c)
    return jsonify({'message': result[0]}),result[1]
#  Update customer

@app.route('/customer/update/<int:customer_id>' , methods=['PUT'])
def update_coustomer(customer_id):
    data = request.json
    c = bo.Customer(CustomerID =  customer_id , CustomerName=data['CustomerName'], ContactName=data['ContactName'], Address=data['Address'], City = data['City'],  PostalCode=data['PostalCode'], Country=data['Country'])
    result = do.Customer(ConnectionData).update(c)
    return jsonify({'message': result[0]}),result[1]

#Show some row by ID
@app.route('/customer/get/<int:user_id>')
def get_user_by_id(user_id):
    c = bo.Customer(CustomerID = user_id)
    result = do.Customer(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}) , result[0]
    return jsonify(result[0].to_json()) , 200
    

# Categories API
@app.route('/categories/all')
def get_all_ca():
    result = do.Categories(ConnectionData).get_all()
    return jsonify(result), 200
    
@app.route('/category/insert', methods=['POST'])
def insert_category():
    data = request.json
    category = bo.Categories(category_name=data['category_name'], description=data['description'])
    result = do.Categories(ConnectionData).insert(category)
    return jsonify({'message': result}), 200

@app.route('/category/get/<int:category_id>')
def get_category_by_id(category_id):
    category = bo.Categories(CategoryID=category_id)
    result = do.Categories(ConnectionData).get_by_id(category)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/category/update/<int:category_id>', methods=['PUT'])
def update_category_by_id(category_id):
    data = request.json
    category = bo.Categories(CategoryID=category_id, CategoryName=data['category_name'], Description=data['description'])
    result = do.Categories(ConnectionData).update(category)
    return jsonify({'message': result[0]}), result[1]

@app.route('/category/delete/<int:category_id>', methods=['DELETE'])
def delete_category_by_id(category_id):
    c = bo.Categories(CategoryID=category_id)
    result = do.Categories(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]
#*******************************************************************
# Shipper 


@app.route('/shipper/all')
def get_all_shipper():
    c = do.Shippers(ConnectionData).get_all()
    return jsonify(c), 200

@app.route('/shipper/get/<int:shipper_id>')
def get_shipper_by_id(shipper_id):
    shipper = bo.Shippers(ShipperID=shipper_id)
    result = do.Shippers(ConnectionData).get_by_id(shipper)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200
@app.route('/shipper/insert', methods=['POST'])
def insert_shipper():
    data = request.json
    shipper = bo.Shippers(ShipperName=data['shipper_name'], Phone=data['phone'])
    result = do.Shippers(ConnectionData).insert(shipper)
    return jsonify({'message': result}), 200

@app.route('/shipper/update/<int:shipper_id>', methods=['PUT'])
def update_shipper_by_id(shipper_id):
    data = request.json
    shipper = bo.Shippers(ShipperID=shipper_id, ShipperName=data['shipper_name'], Phone=data['phone'])
    result = do.Shippers(ConnectionData).update(shipper)
    return jsonify({'message': result[0]}), result[1]

@app.route('/shipper/delete/<int:shipper_id>', methods=['DELETE'])
def delete_shipper_by_id(shipper_id):
    c = bo.Shipper(ShipperID=shipper_id)
    result = do.Shippers(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]

# Supplier

@app.route('/supplier/insert', methods=['POST'])
def supplier_insert():
    data = request.json
    c1 = bo.Suppliers(SupplierName=data['SupplierName'], ContactName=data['ContactName'], Address=data['Address'], City=data['City'], PostalCode=data['PostalCode'], Country=data['Country'], Phone=data['Phone'])
    c2 = do.Suppliers(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/supplier/all')
def get_all_supplier():
    result = do.Suppliers(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/supplier/get/<int:supplier_id>')
def get_supplier_by_id(supplier_id):
    c = bo.Suppliers(SupplierID=supplier_id)
    result = do.Suppliers(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/supplier/update/<int:supplier_id>', methods=['PUT'])
def update_supplier_by_id(supplier_id):
    data = request.json
    c = bo.Suppliers(SupplierID=supplier_id, SupplierName=data['SupplierName'], ContactName=data['ContactName'], Address=data['Address'], City=data['City'], PostalCode=data['PostalCode'], Country=data['Country'], Phone=data['Phone'])
    result = do.Suppliers(ConnectionData).update(c)
    return jsonify({'message': result[0]}), result[1]

@app.route('/supplier/delete/<int:supplier_id>', methods=['DELETE'])
def delete_supplier_by_id(supplier_id):
    c = bo.Suppliers(SupplierID=supplier_id)
    result = do.Suppliers(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]
    
# Products:
@app.route('/product/insert', methods=['POST'])
def product_insert():
    data = request.json
    c1 = bo.Products(ProductID=data['product_name'], Unit=data['Unit'], Price=data['price'], SupplierID=data['supplier_id'], CategoryID=data['category_id'])
    c2 = do.Products(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/product/all')
def get_all_product():
    result = do.Products(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/product/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_product(product_id):
    if request.method == 'GET':
        # Get a product
        c = bo.Products(ProductID=product_id)
        result = do.Products(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        # Update a product
        data = request.json
        c = bo.Products(ProductID=product_id, ProductName=data['product_name'], Unit=data['unit'], Price=data['price'], SupplierID=data['supplier_id'], CategoryID=data['category_id'])
        result = do.Products(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        # Delete a product
        c = bo.Products(ProductID=product_id)
        result = do.Products(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]

# Orders API

@app.route('/order/all')
def get_all_order():
    result = do.Orders(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/order/insert', methods=['POST'])
def order_insert():
    data = request.json
    c1 = bo.Orders(OrderID=data['customer_id'], EmployeeID=data['employee_id'], OrderDate=data['order_date'], ShipperID=data['shipper_id'])
    c2 = do.Orders(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/order/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_order(order_id):
    if request.method == 'GET':
        # Get an order
        c = bo.Orders(OrderID=order_id)
        result = do.Orders(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        # Update an order
        data = request.json
        c = bo.Orders(OrderID=order_id, CustomerID=data['customer_id'], EmployeeID=data['employee_id'], OrderDate=data['order_date'], ShipperID=data['shipper_id'])
        result = do.Orders(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        # Delete an order
        c = bo.Orders(OrderID=order_id)
        result = do.Orders(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]


# Employee 

@app.route('/employee/all')
def get_all_employee():
    result = do.Employees(ConnectionData).get_all()
    return jsonify(result), 200


@app.route('/employee/insert', methods=['POST'])
def employee_insert():
    data = request.json
    c1 = bo.Employee(LastName=data['last_name'], FirstName=data['first_name'], BirthDate=data['birth_date'], Photo=data['photo'], Notes=data['notes'])
    c2 = do.Employee(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200


@app.route('/employee/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_employee(employee_id):
    if request.method == 'GET':
        # Get an employee
        c = bo.Employees(EmployeeID=employee_id)
        result = do.Employees(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        # Update an employee
        data = request.json
        c = bo.Employees(EmployeeID=employee_id, LastName=data['last_name'], FirstName=data['first_name'], BirthDate=data['birth_date'], Photo=data['photo'], Notes=data['notes'])
        result = do.Employees(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        # Delete an employee
        c = bo.Employees(EmployeeID=employee_id)
        result = do.Employees(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]
# Order Detail
@app.route('/order_detail/insert', methods=['POST'])
def order_detail_insert():
    data = request.json
    c1 = bo.OrderDetails(OrderDetailID=data['order_id'], ProductID=data['product_id'], Quantity=data['quantity'])
    c2 = do.OrderDetails(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/order_detail/all')
def get_all_order_detail():
    result = do.OrderDetails(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/order_detail/<int:order_detail_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_order_detail(order_detail_id):
    if request.method == 'GET':
        # Get an order detail
        c = bo.OrderDetails(OrderDetailID=order_detail_id)
        result = do.OrderDetails(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        # Update an order detail
        data = request.json
        c = bo.OrderDetails(OrderDetailID=order_detail_id, OrderID=data['order_id'], ProductID=data['product_id'], Quantity=data['quantity'])
        result = do.OrderDetails(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        # Delete an order detail
        c = bo.OrderDetails(OrderDetailID=order_detail_id)
        result = do.OrderDetails(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
    