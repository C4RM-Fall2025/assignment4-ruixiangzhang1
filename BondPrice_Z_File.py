
def getBondPrice_Z(face, couponRate, times, yc):
    couponPayment = face * couponRate
    BondPrice = 0.0

    for t, yc_rate in zip(times, yc):
        if t == max(times):
            cash_flow = couponPayment + face
        else:
            cash_flow = couponPayment

        pv_factor = 1 / (1 + yc_rate) ** t
        pvcf = cash_flow * pv_factor

        BondPrice += pvcf

    return BondPrice
