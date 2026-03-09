
def get_cost(clicks, cpc):
    return clicks * cpc

def get_roas(clicks, cpc, revenue):
    cost = clicks * cpc                             # Функция # Блок с логикой вычисления 
    roas = revenue / cost
    return roas 

def exchange(value, exchange_rate):
    return value * exchange_rate