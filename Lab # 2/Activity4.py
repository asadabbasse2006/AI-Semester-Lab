def perimeter(listing):
    leng = len(listing)
    perimeter = 0

    # Sum distances between consecutive points
    for i in range(leng - 1):
        dist = ((listing[i][0] - listing[i+1][0]) ** 2 +
                (listing[i][1] - listing[i+1][1]) ** 2) ** 0.5
        perimeter += dist

    # Add distance between last and first point
    dist = ((listing[0][0] - listing[leng-1][0]) ** 2 +
            (listing[0][1] - listing[leng-1][1]) ** 2) ** 0.5
    perimeter += dist

    return perimeter

L = [(1,3),(2,7),(3,9),(-1,8)]
print(perimeter(L))
