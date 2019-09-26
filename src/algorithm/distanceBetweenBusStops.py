
def distanceBetweenBusStops(distance,start,destination) -> int:
    s = 0
    t = sum(distance)
    for i in range(start, destination):
        s += distance[i]
    return s if s < t - s else t - s


print(distanceBetweenBusStops([7,10,1,12,11,14,5,0], 7, 2))
