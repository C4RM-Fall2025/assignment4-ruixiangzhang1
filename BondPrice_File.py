

def getBondPrice(y, face, couponRate, m, ppy=1):
    coupon_payment = (couponRate * face) / ppy
    periods = m * ppy
    period_rate = y /ppy
    pv_coupons = sum([coupon_payment / (1 + period_rate)**t for t in range(1, periods + 1)])
    pv_face_value = face / (1 + period_rate)**periods
    bondPrice = pv_coupons + pv_face_value
    return(bondPrice)
 
