def solution(input_list):
    #version sorting algortithm (pushing the biggest version from left to max right)
    def sorting(soring_list):
        minus = 1
        for _ in range(len(input_list)-1):
            for versions in range(len(soring_list)-minus):
                for num_in_version in range(biggest_version):
                    #compares current version with the version to the right in list.  
                    try:
                        back_version_num, front_version_num = soring_list[versions][num_in_version], soring_list[versions+1][num_in_version]
                    except:
                        if len(soring_list[versions]) > len(soring_list[versions+1]):
                            soring_list[versions], soring_list[versions+1] = soring_list[versions+1], soring_list[versions]
                            break
                        elif len(soring_list[versions]) < len(soring_list[versions+1]):
                            break
                    back_version_num, front_version_num = int(back_version_num), int(front_version_num)
                    #switch versions
                    if back_version_num > front_version_num:
                        soring_list[versions], soring_list[versions+1] = soring_list[versions+1], soring_list[versions] 
                        break
                    elif back_version_num < front_version_num:
                        break
                        
            #makes the last version item invisible so it can sort faster
            minus += 1
        return soring_list
        
    #convert version to numbers
    numbers_list = [] 
    for versions in input_list:
        versions = versions.split(".")
        numbers_list.append(versions)
    
    #get the list with most numbers
    biggest_version = 0
    for numbers in numbers_list: 
        if biggest_version < len(numbers):
            biggest_version = len(numbers)
    
    sorting(numbers_list)
    
    #converts all the numbers back to version
    input_list = []
    for versions in numbers_list:
        input_list.append(".".join(versions))

    return input_list
