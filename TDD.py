import time 
sec=time.time()
t=time.localtime(sec) 
def parking_payment_machine(carnum,five,ten,fifty,wday,PC_I_h,PC_I_m,PC_O_h,PC_O_m):
    if PC_I_m>PC_O_m:
        parking_time=((PC_O_h-1-PC_I_h)*60+(60-PC_I_m+PC_O_m))//30
    else:
        parking_time=((PC_O_h-PC_I_h)*60+(PC_O_m-PC_I_m))//30
    usertotal=five*5+ten*10+fifty*50#客戶投的錢總和 
    if wday>=0 and wday<=4:#平日
        total=parking_time*15
        if total>=300:
            total=300
        overage=usertotal-total
    else:#假日
        total=parking_time*20
        if total>=420:
            total=420
        overage=usertotal-total
    print("車號",carnum)
    print("停車費共",total,"元","投入金額",usertotal,"找",overage,"元")    
parking_payment_machine(512,0,3,1,1,1,30,4,20)
parking_payment_machine(512,0,3,1,1,5,30,8,30)            
#print(t.tm_wday)    
