# Nhóm 3 chú lùn
# Nguyễn Văn Lành 
# Hồ Thị Như Quỳnh 
# Nguyễn Hữu Thiên Quốc Bảo

# Entity

# API
## Customer
### Get all customer
* Request
    * Method: GET
    * Endpoint: /customer/all_Customer
* Response: [Customer]
### Add a customer
* Request
    * Method: POST
    * Endpoint: /customer/insert
* Response: Message
### Update a customer
* Request:
    * Method: PUT
    * Endpoint: /customer/update/<int:customer_id>
* Response: Message

### Delete a customer
* Request:
    * Method: DELETE
    * Endpoint: /customer/delete/<int:customer_id>
* Response: message

#
## Categories
### Get all Categories
* Request
    * Method: GET
    * Endpoint: /category/all
    * Params: None
    * Body: None
* Response: [Categories]
### Add a Categories
* Request
    * Method: POST
    * Endpoint: /category/insert
* Response: Message
### Update a Categories
* Request:
    * Method: PUT
    * Endpoint: /category/update/<int:category_id>
* Response: Message

### Delete a Categories
* Request:
    * Method: DELETE
    * Endpoint: /category/delete/<int:category_id>
* Response: message

#
## Shipper
### Get all Shipper
* Request
    * Method: GET
    * Endpoint: /shipper/all
    * Params: None
    * Body: None
* Response: [Categories]
### Add a Shipper
* Request
    * Method: POST
    * Endpoint: /shipper/all
* Response: Message
### Update a Shipper
* Request:
    * Method: PUT
    * Endpoint: /shipper/update/<int:shipper_id>
* Response: Message

### Delete a Shipper
* Request:
    * Method: DELETE
    * Endpoint: /shipper/update/<int:shipper_id>
* Response: message


#
## Supplier
### Get all Supplier
* Request
    * Method: GET
    * Endpoint: supplier/all
    * Params: None
    * Body: None
* Response: [Categories]
### Add a Supplier
* Request
    * Method: POST
    * Endpoint: /supplier/insert
* Response: Message
### Update a Supplier
* Request:
    * Method: PUT
    * Endpoint: /supplier/update/<int:supplier_id>
* Response: Message

### Delete a Supplier
* Request:
    * Method: DELETE
    * Endpoint: /supplier/delete/<int:supplier_id>
* Response: message


#
## Products
### Get all Products
* Request
    * Method: GET
    * Endpoint: /product/all
    * Params: None
    * Body: None
* Response: [Categories]
### Add a Products
* Request
    * Method: POST
    * Endpoint: /product/insert
* Response: Message
### Update a Products
* Request:
    * Method: PUT
    * Endpoint: /product/<int:product_id>', methods=['GET', 'PUT', 'DELETE']
* Response: Message

### Delete a Products
* Request:
    * Method: DELETE
    * Endpoint: /product/<int:product_id>', methods=['GET', 'PUT', 'DELETE']
* Response: message

#
## Order
### Get all Order
* Request
    * Method: GET
    * Endpoint: /order/all
    * Params: None
    * Body: None
* Response: [Categories]
### Add a Order
* Request
    * Method: POST
    * Endpoint: /order/insert
* Response: Message
### Update a Order
* Request:
    * Method: PUT
    * Endpoint: /order/<int:order_id>', methods=['GET', 'PUT', 'DELETE']
* Response: Message

### Delete a Order
* Request:
    * Method: DELETE
    * Endpoint: /order/<int:order_id>', methods=['GET', 'PUT', 'DELETE']
* Response: message


#
## Employee
### Get all Employee
* Request
    * Method: GET
    * Endpoint: /employee/all
    * Params: None
    * Body: None
* Response: [Categories]
### Add a Employee
* Request
    * Method: POST
    * Endpoint: /employee/insert
* Response: Message
### Update a Employee
* Request:
    * Method: PUT
    * Endpoint: /employee/<int:employee_id>', methods=['GET', 'PUT', 'DELETE']
* Response: Message

### Delete a Employee
* Request:
    * Method: DELETE
    * Endpoint: /employee/<int:employee_id>', methods=['GET', 'PUT', 'DELETE']
* Response: message

#
## Order Detail
### Get all Order Detail
* Request
    * Method: GET
    * Endpoint: /order_detail/all
    * Params: None
    * Body: None
* Response: [Categories]
### Add a Order Detail
* Request
    * Method: POST
    * Endpoint: /order_detail/insert
* Response: Message
### Update a Order Detail
* Request:
    * Method: PUT
    * Endpoint: /order_detail/<int:order_detail_id>', methods=['GET', 'PUT', 'DELETE']
* Response: Message

### Delete a Order Detail
* Request:
    * Method: DELETE
    * Endpoint: /order_detail/<int:order_detail_id>', methods=['GET', 'PUT', 'DELETE']
* Response: message



