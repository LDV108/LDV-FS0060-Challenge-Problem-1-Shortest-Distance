import math

# 52.6369° N, 1.1398° W - LE
# 37.7749° N, 122.4194° W - SF
# Earth radius = 6.371 km

EARTH_RADIUS = 6371.09
DEG_TO_KM = 111.32
LE_LONG = 52.6369
LE_LAT = 1.1398
SF_LONG = 37.7749
SF_LAT = 122.4194
EXPECTED_RESULT = 8472


def gdc_calc(lo1, la1, lo2, la2):
    latDiff = abs(la2 - la1)
    longDiff = abs(lo1 - lo2)
    cntrl_ang = math.acos((math.sin(la1) * math.sin(la2)) + (math.cos(la1) * math.cos(la2) * math.cos(longDiff)))
    print("Central angle:", cntrl_ang, "rads")
    arcLen = EARTH_RADIUS * cntrl_ang

    return arcLen


def degtokm_calc(dis):
    km = dis * DEG_TO_KM
    return km


def degtorad_calc(deg):
    rad = deg * (180 / math.pi)
    return rad


# distanceDeg = gdc_calc(LE_LONG, LE_LAT, SF_LONG, SF_LAT)
# print(distanceDeg)
# distanceKM = degtokm_calc(distanceDeg)
# print(distanceKM)

print("//")
distanceDeg2 = (gdc_calc(degtorad_calc(LE_LONG), degtorad_calc(LE_LAT), degtorad_calc(SF_LONG), degtorad_calc(SF_LAT)))
print("Calculated result:" ,distanceDeg2,"km")

# distanceKM2 = degtokm_calc(distanceDeg2)
# print(distanceKM2,"km")

print("Expected result:" ,EXPECTED_RESULT, "km")