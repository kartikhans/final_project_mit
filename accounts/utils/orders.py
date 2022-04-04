from accounts.models import Orders, OrderStatus


def place_order(data):
    user = data.get('user')
    product = data.get('product')

    order_obj = Orders(user=user, product=product)
    order_obj.save()
    return dict(result="ORDER_ADDED_SUCCESSFULLY", order_uid=order_obj.uid)


def change_status(data):
    order = data.get('order')
    status = data.get('status')

    order.status = status
    order.save()
    return "ORDER_STATUS_CHANGED_SUCCESSFULLY"
