from datetime import datetime

#sec=time.time()
#t=time.localtime(sec)
def parking_costs(five,ten,fifty):#客戶投的錢總和
     usertotal=five*5+ten*10+fifty*50
     return usertotal
def parking_times(PC_I_h,PC_I_m,PC_O_h,PC_O_m):#計算停車時間
    if PC_I_m>PC_O_m:
        parking_time=((PC_O_h-1-PC_I_h)*60+(60-PC_I_m+PC_O_m))//30
    else:
        parking_time=((PC_O_h-PC_I_h)*60+(PC_O_m-PC_I_m))//30
    return parking_time    
def parking_payment_machine(carnum,five,ten,fifty,I_wday,p_start):
    if I_wday==O_wday:#當日
        wday=I_wday
        parking_time=parking_times(PC_I_h,PC_I_m,PC_O_h,PC_O_m)#計算停車時間
        usertotal=parking_costs(five,ten,fifty)#客戶投的錢總和 
        if wday>=0 and wday<=4:#平日
            total=parking_time*15
            if total>=300:#平日最高費用300
                total=300
            overage=usertotal-total
        else:#假日
            total=parking_time*20
            if total>=420:#假日最高費用420
                total=420
            overage=usertotal-total
    else:
          1
    print("車號",carnum)
    print("停車費共",total,"元","投入金額",usertotal,"找",overage,"元")
parking_start=datetime(2023,5,25,23,0)
parking_end=datetime(2023,5,26,23,0)       
#parking_payment_machine(512,0,3,1)
#parking_payment_machine(512,0,3,1,1,1)            
#print(t.tm_wday)    
