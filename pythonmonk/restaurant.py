class Restaurant:

    def __init__(self, menu):
        self.menu = menu

    def cost(self, *orders):
        def cal_total_cost(total_cost, order):
            def cal_order_cost(order_cost, key):
                return order_cost + order[key] * self.menu[key]
            return total_cost + reduce(cal_order_cost, order.keys(), 0)
        return reduce(cal_total_cost, orders, 0)
