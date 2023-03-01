from datetime import date

from django.db.models import Sum
from django.shortcuts import render

from .models import Order
from .airtable_api import get_orders

# Create your views here.
def save_orders_in_db(orders_returned):
    orders_to_save = []
    for order in orders_returned:
        order_to_save = Order(order_id=order.get('order_id'), order_placed=order.get('order_placed'),
                product_name=order.get('product_name'),
                price=order.get('price'),
                first_name=order.get('first_name'),
                last_name=order.get('last_name'),
                address=order.get('address'),
                email=order.get('email'),
                order_status=order.get('order_status'))
        orders_to_save.append(order_to_save)

    print(len(orders_to_save))

    Order.objects.bulk_create(orders_to_save)
    print('order saved')


def dashboard(request):

    orders_returned = get_orders()

    print(f"returned orders {len(orders_returned)}")

    save_orders_in_db(orders_returned)

    orders = Order.objects.all()
    print(f"from db: {len(orders)}")

    total_orders = orders.count()
    orders_this_month = orders.filter(order_placed__month__exact=date.today().month).count()
    orders_in_progress = orders.filter(order_status='in_progress').count()
    revenue = orders.aggregate(Sum('price'))['price__sum']
    recent_orders = orders.order_by('-order_placed')[:5]
    context = {
        'total_orders': total_orders,
        'orders_this_month': orders_this_month,
        'orders_in_progress': orders_in_progress,
        'revenue': revenue,
        'recent_orders': recent_orders
    }

    print("Dashboard view function called, and sending this context along to it")
    print(context)
    return render(request, 'app/dashboard.html', context)

