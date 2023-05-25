from parking_payment_machine import money_balance
#單元測試
#找零功能測試
def test_unit_money_balance1():
    assert money_balance(50,30)==20#投入50 停車費30 找20
def test_unit_money_balance2():
    assert money_balance(100,100)==0#投入100 停車費100 找0
def test_unit_money_balance3():
    assert money_balance(50,100)==False 