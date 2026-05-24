from django.db import transaction
from django.db.models import QuerySet

from db.models import Order


def create_order(
    tickets: list[dict],
    username: str,
    date: str | None = None,
) -> Order:
    with transaction.atomic():
        order = Order.objects.create(
            tickets=tickets,
            username=username,
        )
        if date:
            order.date = date
        return order
