
def buying_ticket_each_station(stations,cost):
    return stations * cost

def optimal_cost(stations,m_stations,each_cost,m_cost):
    cost1 = 0
    cost2 = 0
    while stations >= m_stations:
        stations -=m_stations
        cost1+=m_cost

    cost2 = cost1
    remaining_stations = stations

    if stations > 0:
        while stations > 0:
            stations-=1
            cost1+=each_cost
        while remaining_stations > 0:
            remaining_stations-=m
            cost2+=m_cost    

    return(min(cost1,cost2))




if __name__ == '__main__':
    n,m,a,b = input().strip().split()

    n = int(n)
    m = int(m)
    a = int(a)
    b = int(b)

    print(min(optimal_cost(n,m,a,b),buying_ticket_each_station(n,a)))

