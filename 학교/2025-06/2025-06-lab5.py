log1 = {"id" : 1 , "status" : "error" , "value" : -100 }
log2 = {"id" : 2 , "status" : "success" , "value" : 20 }
log3 = {"id" : 3 , "status" : "error" , "value" : -30 }
log4 = {"id" : 4 , "status" : "success" , "value" : 80 }



def analyze_logs(analyze_name , *log , **option):
    
    if "filter_status" in option and option["filter_status"] == "error":
        filter_list = []
        for i in log:
            for k , v in i.items():
                if k == "status" and v == "error" :
                    filter_list.append(i)
        
        log = filter_list
    
    
    if "abs" in option and option["abs"] == "True":
        abs_list = []
        for i in log:
            for k , v in i.items():
                if k == "value" and v < 0:
                    v *= -1
        
    if "uniqe_id" in option and option["uniqe_id"] == "True":
        check_list = []
        for i in log:
            for k , v in i.items():
                if k == "id" :
                    if v not in check_list:
                        check_list.append(i)
        log = check_list        
    
    
    if "mode" in option and option["mode"] == "sum":
        sum = 0
        for i in log:
            for k , v in i.items():
                if k == "value" :
                    sum += v
        
        print(sum)
    
    elif "mode" in option and option["mode"] == "average":
        sum = 0
        count = 0
        for i in log:
            for k , v in i.items():
                if k == "value" :
                    sum += v
                    count+= 1
        
        average = sum / count
        print(round(average,2))
    
    elif "mode" in option and option["mode"] == "max":
        max_num = 0
        for i in log:
            for k , v in i.items():
                if k == "value" :
                    if v > max_num:
                        max_num = v
        
        print(max_num)
    
        


analyze_logs("기본분석" , log1 , log2 , log3 , log4 , mode ="max")
