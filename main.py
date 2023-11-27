


class Brand:
    def __init__(self, brand_id, brand_name, model_id):
        self.Brand_ID = brand_id
        self.Brand_Name = brand_name
        self.Model_ID = model_id

class ShippingtoBrand:
    def __init__(self, shipping_to_brand_id, brand_id, rma_id, send_date_of_packet):
        self.ShippingtoBrand_ID = shipping_to_brand_id
        self.Brand_ID = brand_id
        self.RMA_ID = rma_id
        self.SendDateofPacket = send_date_of_packet

class Technican:
    def __init__(self, technican_id, tech_name, tech_qual):
        self.Tachnican_ID = technican_id
        self.TechName = tech_name
        self.TechQual = tech_qual

class Customer:
    def __init__(self, customer_id, customer_name, customer_address, customer_phone, customer_email):
        self.Customer_ID = customer_id
        self.CustomerName = customer_name
        self.CustomerAddress = customer_address
        self.CustomerPhone = customer_phone
        self.CustomerEmail = customer_email

class Model:
    def __init__(self, model_id, model_name, brand_id, product_id):
        self.Model_ID = model_id
        self.ModelName = model_name
        self.Brand_ID = brand_id
        self.Product_ID = product_id

class Product:
    def __init__(self, product_id, model_id, technican_id, customer_id, rma_id, product_sold_date):
        self.Product_ID = product_id
        self.Model_ID = model_id
        self.Technican_ID = technican_id
        self.Customer_ID = customer_id
        self.RMA_ID = rma_id
        self.ProductSoldDate = product_sold_date

class ReturntoCustomer:
    def __init__(self, return_shipping_id, send_date_of_packet, customer_id, rma_id):
        self.ReturnShipping_ID = return_shipping_id
        self.SendDateofPacket = send_date_of_packet
        self.Customer_ID = customer_id
        self.RMA_ID = rma_id

class RMA:
    def __init__(self, rma_id, inspection_start_date, inspection_completion_date, product_defect, brand_id, model_id, product_id, check_issue, result_issue, technican_id):
        self.RMA_ID = rma_id
        self.InspactionStartDate = inspection_start_date
        self.InspecitonCompletionDate = inspection_completion_date
        self.Product_Defect = product_defect
        self.Brand_ID = brand_id
        self.Model_ID = model_id
        self.Product_ID = product_id
        self.CheckIssue = check_issue
        self.ResultIssue = result_issue
        self.Technican_ID = technican_id

