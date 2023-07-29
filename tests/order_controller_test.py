# import unittest
# from app import app, db
# from controllers.order_controller import Order , order_blueprint
# from controllers.item_controller import Item
# from controllers.order_item_controller import Order_Item

# class TestOrder(unittest.TestCase):

#     def setUp(self):
#         self.order1 = Order(id = 1,customer_name="George",customer_phone=1234567890,customer_address="Bon Gait",order_delivered=False)
#         self.order2 = Order(id = 2,customer_name="Nick",customer_phone=9809878987,customer_address="Princess Street",order_delivered=False)
#         self.order3 = Order(id = 3,customer_name="Bill",customer_phone=3241234123,customer_address="Princess Street North",order_delivered=False)


#         self.item1 = Item(id=1,item_name="Kebab",item_price=10)
#         self.item2 = Item(id=2,item_name="Fish and Chips",item_price=15)
#         self.item3 = Item(id=3,item_name="Club",item_price=7)
    
#         self.order_item_one = Order_Item(id=1,order_id=1,item_id=2)
#         self.order_item_two = Order_Item(id=2,order_id=1,item_id=3)

#     def test_show_all_orders(self):
#         print(self.order_item_one.order_id)
#         pass


