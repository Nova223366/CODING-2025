def total_cal(bill_amont, tip_pert):
    total=bill_amont *(1+0.01*tip_pert)
    total=round(total,2)
    print("The total payable amount is:", total)
    
total_cal(150,20)