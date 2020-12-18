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
    return c1.CustomerName

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
@app.route('/user/insert', methods=['POST'])
def user_insert():
    data = request.json
    c1 = bo.Customer(data['CustomerID'], data['CustomerName'], data['ContactName'], data['Address'], data['City'], data['PostalCode'], data['Country'])
    c2 = do.Customer(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/test_send_receive', methods=['POST'])
def test_send_receive():
    x = request.json['x']
    y = x + 1
    result = {}
    result['y'] = y
    return jsonify(result), 200

#Show all item from Customer
@app.route('/customer/all_Customer')
def get_all_user():
    result = do.Customer(ConnectionData).get_all()
    return jsonify(result), 200
# --------------------
@app.route('/categories/all_Categories')
def get_all_ca():
    result = do.Categories(ConnectionData).get_all()
    return jsonify(result), 200
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
# CUSTOMER
@app.route('/customer/get/<int:user_id>')
def get_user_by_id(user_id):
    c = bo.Customer(CustomerID = user_id)
    result = do.Customer(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}) , result[0]
    return jsonify(result[0].to_json()) , 200
# Categories
@app.route('/categories/get/<int:user_id>')
def get_ca_by_id(user_id):
    c = bo.Customer(CustomerID = user_id)
    result = do.Customer(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}) , result[0]
    return jsonify(result[0].to_json()) , 200

#*********************************
@app.route('/user/get_by_id', methods=['POST'])
def user_get_by_id():
    user_id = request.json['user_id']
    result = {}
    result['user_id'] = 1
    return jsonify(result), 200



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
    