assert 1 == 1, 'This should not fail'


# python -O main.py
# it would ignore assert
def apply_discount(price, discount):
    updated_price = price * (1 - discount)
    assert 0 <= updated_price <= price, 'price should be greater or equal to 0 and less or equal to original price'
    return updated_price


apply_discount(1, 0.2)
apply_discount(1, 2)
