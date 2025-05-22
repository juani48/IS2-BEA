from core.service.mercado_pago.config import make_preferences, make_preferences_test

def execute(machine_id, machine_model, unit_price):
    return make_preferences(machine_id, machine_model, unit_price)

def execute():
    return make_preferences_test()



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
