from core.service.mercado_pago.config import make_preferences, make_preferences_test, config_get_payment, config_get_merchant_order

def execute(client_id, machine_id, start_day, machine_model, unit_price):
    return make_preferences(client_id, machine_id, start_day, machine_model, unit_price)

def execute():
    return make_preferences_test()

def get_payment(id):
    return config_get_payment(id)

def get_merchant_order(id):
    return config_get_merchant_order(id)



# url de vuelta 

# collection_id=112006940331
# collection_status=approved
# payment_id=112006940331
# status=approved
# external_reference=null
# payment_type=account_money
# merchant_order_id=31207000692
# preference_id=2447327823-f9f12169-6453-46c2-a318-6f1bbc32e1f6
# site_id=MLA
# processing_mode=aggregator
# merchant_account_id=null
