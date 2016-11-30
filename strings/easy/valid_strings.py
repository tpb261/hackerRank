S="ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"#"jtqgugmcsxvdwidtcyqpogkdifapuloqykjfxruvfrshcehekoiwbpbrprahwvhliglyxynjotbaswnnnmxbkmcftvsdqajemeul"
s=set(S)
h={}
let_count_1 = let_count_2 = imp = 0
let_count_1_count=0
let_count_2_count=0
for c in s:
    h[c] = S.count(c)    
    if(h[c]==let_count_1):
        let_count_1_count+=1
    elif(h[c]==let_count_2):
        let_count_2_count+=1
    elif(0==let_count_1):
        let_count_1=h[c]
        let_count_1_count=1
    elif(0==let_count_2):
        let_count_2 = h[c]
        let_count_2_count=1        
    else:
        imp=1
        break
if(let_count_1>let_count_2):
    [let_count_1, let_count_2]=[let_count_2, let_count_1]
    [let_count_1_count, let_count_2_count]=[let_count_2_count, let_count_1_count]
    
if(0==imp):
    if(let_count_2-let_count_1<=1 and 1==let_count_2_count):
        print("YES")
    elif(0==let_count_1):
        print("YES")
    elif(1==let_count_1 and 1==let_count_1_count):
        print("YES")
    else:
        print("NO")
else:
    print ("NO")
    
