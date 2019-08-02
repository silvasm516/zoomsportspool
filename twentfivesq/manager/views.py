from django.shortcuts import render
from django.http import HttpResponse


from django.template.context_processors import csrf
from django.template import Template, Context
from django.template import loader
import ctypes


def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)


#from Home Page Sign-In to Grid Set-Up
def Cat(request):
    if request.method == 'POST':
        from django.contrib.auth.models import User
        from django.contrib.auth import authenticate, login 
        from manager.models import Managers
        import datetime
        from grid2.views import maxLimitExpiration
        from grid2.views import deadline, expdaytest, update
        n = ""
        u = ""
        m = Managers.objects.all()
#       name = request.POST.get('username')
#       password = request.POST.get('password')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        n = m.filter(UsrName= str(username))
        if not n:
            reason = 'un'
            rat = logfail(reason)
        u = n.filter(Password= password)     
        if not u:
            reason = 'pw'
            #logfail(reason)
            rat = logfail(reason) 
        else:
            em = n[0].Email
            login(request, user)
            request.session['UsrName'] = username
            request.session['UsrType'] = 'm'
            n = Managers.objects.get(UsrName = str(username))
            exp = maxLimitExpiration(datetime.date(2019, 2, 3))
            if n.GridsOut == 999 and exp == 0:
                gr = 'U'
            elif n.GridsOut == 999 and exp == 1:
                n.GridsOut = 0
                n.save()
                gr = 0
            else:
                gr = n.GridsOut
            
            purch = n.GridsPurch
            if purch =='':
                gr = 0  
            
            #gr = n.GridsOut
            nameO = m.filter(Password= password)
            justLastName = nameO[0]
            ident = justLastName
            first = ident.FirstName            
            mgrId = ident.id
#           msg = loginM(name, password)
            update(mgrId)
            j = 'Buy Games'
            k = ferret(mgrId)
            j = len(k)
            b = []
            i = "Dashboard"
            for s in range(0, 10):
                if s >= j:
                    s = 99
                else:
                    s = s
                a = weasel(mgrId, s)
                b.append(a)
            data = {
            'gridsout': gr,
            'welcome':'welcome',   
            'tit': i,
            'firstname':first,
            'userName' :username,
            'mgrId'   :mgrId,
            'result0' : b[0],
            'result1' : b[1],
            'result2' : b[2],
            'result3' : b[3],
            'result4' : b[4],
            'result5' : b[5],
            'result6' : b[6],
            'result7' : b[7],
            'result8' : b[8],
            'result9' : b[9]
            
            }
           

            
            c = {'data':data}
            #moron = dumb
            
            temp = loader.get_template('DashBoard2.html')
            
            return HttpResponse(temp.render(c, request))
        
        
        temp = loader.get_template('Some.html')
        return HttpResponse(temp.render(rat, request))







def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)


    
   








               

    
def ferret(i):
    #filters Grid db to instances of that manager's active grids
    from django.template.context_processors import csrf
    from grid2.models import Grid
    from grid2.views import update
    g = Grid.objects.all()
    update(i)
    w = g.filter(managerNumber = i)
    y = w.filter(active = '10')
    if y != "":
        return y



def weasel(mgrId, o):
    #deals out the active grids to all "o" postions, or default values
    #of 'home' or 'visitor'.
    i = mgrId
    from django.template.context_processors import csrf
    from grid2.models import Grid
    p = o
    g = Grid.objects.all()
    z = g.filter(managerNumber = i)
    m = z.filter(active = '10')
    if is_empty(m):
        h = 'home'
        v = 'visitor'
        e = {
           'home' :h,
           'visit' :v,
           }
        return e 
    elif p == 99:
        h = 'home'
        v = 'visitor'
        e = {
           'home' :h,
           'visit' :v,
           }
        return e 
    else:
        h = m[p].homeTeam
        v = m[p].visitingTeam
        e = {
           'home' :h,
           'visit' :v,
           }
        return e 
        



             
            
def is_empty(any_structure):
    if any_structure:

        return False
    else:

        return True


#from Home Page Sign-Up Button to Sign-Up Form
def SignUp(request):
    a = 'Manger Sign-Up'
    c = { "title" : a }
    temp = loader.get_template('managerSignUp.html')
    return HttpResponse(temp.render(c, request))
    if request.method == 'GET':
        return HttpResponse(request.GET ['item_text'])

#from Sign-Up Form to home page
def Dog(request):
    if request.method == 'POST':
        from django.contrib.auth.models import User 
        from manager.models import Managers
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        street = request.POST.get('street') 
        city = request.POST.get('city')
        zipcode = request.POST.get('zip')
        state = request.POST.get('state')
        country = request.POST.get('country')
        username = request.POST.get('userName')
        email = request.POST.get('email')
        m = Managers.objects.all()
        for z in m:
            x = z.UsrName
            if username == x:
                    break
                    rat = logfail('un')
                    temp = loader.get_template('Some.html')
                    return HttpResponse(temp.render(rat, request))


        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')        
        user = User.objects.create_user(username, email, password2)
        user.save() 
        p = Managers.objects.create(FirstName = firstname, LastName = lastname, Street = street,\
        City = city, ZipCode = zipcode, State = state, Country = country, UsrName = username, Password = password2, \
        Email = email)
        p.save()
        rat = logfail('pw') 
    c = {
            'tit' : '25 SQUARES FOOTBALL',
            'pw2' : 'new',
            'name': username}    
    temp = loader.get_template('Some.html')
    return HttpResponse(temp.render(c, request))



#deprecated    
def Rat(request):
    if request.method == 'POST':
        from manager.models import Managers
        password = request.POST.get('password2')
        cardtype = request.POST.get('cardtype')
        cardno = request.POST.get('cardnumber')
        paypal = request.POST.get('paypal')
        m = Managers.objects.all()
        j = Managers.objects.get(Password = password)
        j.CardType = cardtype
        j.CardNo = cardno
        j.PayPal = paypal
        j.save()
        first = j.FirstName
        userName = j.UsrName
        mgrId = j.id
        c ={
            'firstname':first,
            'userName' :userName,
            'mgrId' :mgrId,
            }

        
        temp = loader.get_template('Menus.html')
        return HttpResponse(temp.render(c, request))

def grabNames(gameNo):
    from grid2.models import Grid
    g = Grid.objects.all()
    n = g.filter(id = gameNo)
    m = []
    for x in range(0, 1):
        m.append(n[x].name1)
        m.append(n[x].name2)
        m.append(n[x].name3)
        m.append(n[x].name4)
        m.append(n[x].name5)
        m.append(n[x].name6) 
        m.append(n[x].name7) 
        m.append(n[x].name8) 
        m.append(n[x].name9)
        m.append(n[x].name10) 
        m.append(n[x].name11)
        m.append(n[x].name12) 
        m.append(n[x].name13) 
        m.append(n[x].name14) 
        m.append(n[x].name15)    
        m.append(n[x].name16)
        m.append(n[x].name17) 
        m.append(n[x].name18) 
        m.append(n[x].name19)   
        m.append(n[x].name20) 
        m.append(n[x].name21)
        m.append(n[x].name22)        
        m.append(n[x].name23)
        m.append(n[x].name24)
        m.append(n[x].name25)
    return m
                 
def netNames(list):
    tally = []
    for a in range(0, len(list)):
            if list[a] not in tally and (list[a].isalpha() or len(list[a]) > 2):
                tally.append(list[a])
            else:
               continue
        
    return tally

def configDict(nameList):
    import collections
    from player.models import Players
    p = Players.objects.all()
    s = {}
    j = []
    checklist = []
    for x in p:
        a = x.UsrName 
        for y in nameList:
            if y == a and y not in checklist:
                z = p.filter(UsrName = y)
                s['User Name'] = z[0].UsrName
                s['First Name'] = z[0].FirstName
                s['Last Name'] = z[0].LastName
                s['Email'] = z[0].Email
                t = collections.OrderedDict(s) 
                j.append(t.copy())
                checklist.append(y) 
                
    return j
     




def output(dList):
    resultList = []
    dif = 100 - len(dList)
    for d in range(0, len(dList)):
        for (kk, jj) in sorted(dList[d].items()):
            resultList.append(jj)
    for z in range(len(dList), 100):
        resultList.append('')
    return resultList




def IndexR(request):
    from grid2.models import Grid
    from player.models import Players
    from twentfivesq.views import gmeList
    import collections
    ta = []
    name = request.session['UsrName']
    gameNos = []
    gameNos = gmeList(name)
    gameNo = request.POST.get('game No')
    if not int(gameNo) in gameNos:
        c = {'tit':'Index','rsn':'num', 'msg': 'The Game Number Is Invalid'}
        temp = loader.get_template('Index.html')
        return HttpResponse(temp.render(c, request))
    games = Grid.objects.all()
    g = games.filter(id = gameNo)
    n = g[0].managerName
    if n != name:
        c = {'rsn':'name', 'msg': 'The Name Is Invalid'}
        temp = loader.get_template('Index.html')
        return HttpResponse(temp.render(c, request))
    else:                 
        qq = grabNames(gameNo)
        a = 0
        b = 'false'
        for t in qq:
            a = a + 1
            t = t.replace(" ", "")
            if t.isalpha():
                b = 'true'
            if b == 'false' and a == 25: 
                c = {'tit':'Index','rsn':'num', 'msg': 'There Are No Players For That Grid'}
                temp = loader.get_template('Index.html')
                return HttpResponse(temp.render(c, request))     
        rr = netNames(qq)
        ss = configDict(rr)
        ta = output(ss)
        aa = "Index"

        c = {
             'tit' : aa,
             'a' : ta[0],
             'b' : ta[1],
             'c' : ta[2],
             'd' : ta[3],
             'e' : ta[4],
             'f' : ta[5],
             'g' : ta[6],
             'h' : ta[7],
             'i' : ta[8],
             'j' : ta[9],   
             'k' : ta[10],
             'l' : ta[11],
             'm' : ta[12],
             'n' : ta[13],
             'o' : ta[14],
             'p' : ta[15],
             'q' : ta[16],
             'r' : ta[17],
             's' : ta[18],
             't' : ta[19],
             'z3': ta[20],
             'z4': ta[21],
             'z5': ta[22],
             'z6': ta[23],
             'z7': ta[24],
             'z8': ta[25],
             'z9': ta[26],
             'z10': ta[27],
             'z11': ta[28],
             'z12': ta[29],
             'z13': ta[30],
             'z14': ta[31],
             'z15': ta[32],
             'z16': ta[33],
             'z17': ta[34],
             'z18': ta[35],
             'z19': ta[36],
             'z20': ta[37],
             'z21': ta[38],
             'z22': ta[39],
             'z23': ta[40],
             'z24': ta[41],
             'z25': ta[42],
             'z26': ta[43],
             'z27': ta[44],
             'z28': ta[45],
             'z29': ta[46],
             'z30': ta[47],
             'z31': ta[48],
             'z32': ta[49],
             'z33': ta[50],
             'z34': ta[51],
             'z35': ta[52],
             'z36': ta[53],
             'z37': ta[54],
             'z38': ta[55],
             'z39': ta[56],
             'z40': ta[57],
             'z41': ta[58],
             'z42': ta[59],
             'z43': ta[60],
             'z44': ta[61],
             'z45': ta[62],
             'z46': ta[63],
             'z47': ta[64],
             'z48': ta[65],
             'z49': ta[66],
             'z50': ta[67],
             'z51': ta[68],
             'z52': ta[69],
             'z53': ta[70],
             'z54': ta[71],
             'z55': ta[72],
             'z56': ta[73],
             'z57': ta[74],
             'z58': ta[75],
             'z59': ta[76],
             'z60': ta[77],
             'z61': ta[78],
             'z62': ta[79],
             'z63': ta[80],
             'z64': ta[81],
             'z65': ta[82],
             'z66': ta[83],
             'z67': ta[84],
             'z68': ta[85],
             'z69': ta[86],
             'z70': ta[87],
             'z71': ta[88],
             'z72': ta[89],
             'z73': ta[90],
             'z74': ta[91],
             'z75': ta[92],
             'z76': ta[93],
             'z77': ta[94],
             'z78': ta[95],
             'z79': ta[96],
             'z80': ta[97],
             'z81': ta[98],     
             'z82': ta[99]

     # must be 100 pairs in length       
             }
         
    temp = loader.get_template('Index.html')
    return HttpResponse(temp.render(c, request)) 
    

def loginM(manager, auth):
    from manager.models import Managers
    from grid2.models import Grid
    u = manager
    request.session['UsrName'] = u
    request.session['UsrType'] = 'm'
    
        
          
    

def preKit(UsrName):
    mgrName = UsrName
    from manager.models import Managers
    man = Managers.objects.all()
    name = man.filter(UsrName = mgrName)
    pw = name[0].Password

    return pw
	

def Kit(request):
    from manager.models import Managers
    m = Managers.objects.all()
    pw = preKit(request.session['UsrName'])
    nameO = m.filter(Password= pw)
    justLastName = nameO[0]
    ident = justLastName
    first = ident.FirstName            
    mgrId = ident.id
    name = request.session['UsrName']
    n = Managers.objects.get(UsrName = str(name))
    if n.GridsOut == 999:
        gr = 'U'
    else:
        gr = n.GridsOut
    if gr == '':
        gr = 0
    k = ferret(mgrId)
    j = len(k)
    i = "Dashboard"
    b = []
    for s in range(0, 10):
        if s >= j:
            s = 99
        else:
            s = s
        a = weasel(mgrId, s)
        b.append(a)
    data = {
    'tit' : i,
    'firstname':first,
    'userName' :name,
    'mgrId' :mgrId,
    'gridsout': gr,
    'result0' : b[0],
    'result1' : b[1],
    'result2' : b[2],
    'result3' : b[3],
    'result4' : b[4],
    'result5' : b[5],
    'result6' : b[6],
    'result7' : b[7],
    'result8' : b[8],
    'result9' : b[9]
    
    }
   

    
    c = {'data':data}
   
    #Sign-On extends Grid Set-Up(Dashboard)
    temp = loader.get_template('SignOn.html')
    return HttpResponse(temp.render(c, request))

def Enroll(request):
    a = 'Manager Sign-Up'
    c = { "tit" : a }
    temp = loader.get_template('managerSignUp.html')
    return HttpResponse(temp.render(c, request))
    
def BuyGames(request):
    k = 'Buy Games'
    c = { "tit" : k}      
    temp = loader.get_template('BuyGames.html')
    return HttpResponse(temp.render(c, request)) 

def OverLimit(request, m):
    m = m
    k = 'Buy Games'
    c = { "tit" : k,
          "m" : m}
    return c 
    


def RunOutTest(request):
    from manager.models import Managers
    m = Managers.objects.all()
    name = request.session['UsrName']
    u = Managers.objects.get(UsrName = str(name))
    grout = u.GridsOut
    if grout == '':
        grout = 0
    if grout == 'NO':
        grout = 0
    if grout <= 0:
        j = 'runout'
        a = OverLimit(request, j)
        return a
    else:
        return 'v'
    
        
    

def Purchase(request):
    if request.method == 'POST':
        from manager.models import Purchases
        from manager.models import Managers
        import datetime
        date = datetime.datetime.today()
        nam = request.session['UsrName']
        g = request.POST.get('num')
        if g == '999':
           gr = 'U' 
           gridspurchased = 0
        else:
            gridspurchased = request.POST.get('num')
        amount = request.POST.get('amt')
        p = Purchases.objects.create(Date = date, UsrName = nam, GridsPch = gridspurchased, Amount = amount)
        p.save()
    from manager.models import Managers    
    m = Managers.objects.all()
    name = request.session['UsrName']
    u = Managers.objects.get(UsrName = str(name))
    pw = u.Password
    g = request.POST.get('num')
    if g == '':
        g = 0
    elif g == '999':
        u.GridsOut = 999
        u.save
        g = 0
    elif g == 0:
        g = 0
    else:
        g = int(g)
    d = request.POST.get('amt')
    if d == '':
        d = 0
    else:
        d = float(d)
    total = u.GridsPurch
    dollar = u.DollarPurch
    if g != '999':
        go = u.GridsOut
    else:
        go = 0
    if go == '':
        go = 0
    if go == 'NO':
        go = 0
    if go + g > 0: 
        if total == 0:
            u.GridsPurch = u.GridsPurch + int(g)
            u.GridsOut = int(g) + int(2)     
        else:
            u.GridsOut = u.GridsOut + int(g)
        if dollar == '':
            u.DollarPurch = 0
        u.DollarPurch = u.DollarPurch + float(d)
        u.GridsPurch = u.GridsPurch + int(g)
        u.save()
        nameO = m.filter(Password= pw)
        justLastName = nameO[0]
        ident = justLastName
        first = ident.FirstName            
        mgrId = ident.id
       # msg = loginM(request, name, pw)
        j = 'Buy Games'
        k = ferret(mgrId)
        j = len(k)     
        b = []
        for s in range(0, 10):
            if s >= j:
               s = 99
            else:
                s = s
            a = weasel(mgrId, s)
            b.append(a)
        if g != 0:
            gr = u.GridsOut
        data = {
                'gridsout': gr,
                'welcome':'welcome',   
                'userName' :name,
                'mgrId' :mgrId,
                #'msg' : msg,
                'result0' : b[0],
                'result1' : b[1],
                'result2' : b[2],
                'result3' : b[3],
                'result4' : b[4],
                'result5' : b[5],
                'result6' : b[6],
                'result7' : b[7],
                'result8' : b[8],
                'result9' : b[9]
                
                }
               

              
        c = {'data':data}
        temp = loader.get_template('DashBoard2.html')
        return HttpResponse(temp.render(c, request))  
##    else:
##        m = 'modal'
##        t = OverLimit(request, m)
##        return t
        
def logfail(reason):
    # Redirect to a success page.
    z = reason   
    temp = loader.get_template('Some.html') 
    a = '25 SQUARES FOOTBALL'
    c = {
         'rsn': z,
         'tit': a

         }
    return c



def purch(request):
    if request.method == 'POST':
        from manager.models import Purchases
        import datetime
        date = datetime.datetime.today() 
        gridspurchased = request.POST.get('num')
        amount = request.POST.get('amt')
        p = Managers.objects.create(Date = date, GridsPch = gridspurchased, Amount = amount)
        p.save()
                                    
def ErrorProc(request, number):
    from manager.models import Managers
    m = Managers.objects.all()
    pw = preKit(request.session['UsrName'])
    nameO = m.filter(Password= pw)
    justLastName = nameO[0]
    ident = justLastName
    first = ident.FirstName            
    mgrId = ident.id
    name = request.session['UsrName']
    n = Managers.objects.get(UsrName = str(name))
    gr = n.GridsOut
    if gr == '':
        gr = 0
    k = ferret(mgrId)
    j = len(k)
    i = "Dashboard"
    hh = "nope"
    b = []
    for s in range(0, 10):
        if s >= j:
            s = 99
        else:
            s = s
        a = weasel(mgrId, s)
        b.append(a)
    data = {
    'tripper': hh,   
    'tit' : i,
    'firstname':first,
    'userName' :name,
    'mgrId' :mgrId,
    'gridsout': gr,
    'result0' : b[0],
    'result1' : b[1],
    'result2' : b[2],
    'result3' : b[3],
    'result4' : b[4],
    'result5' : b[5],
    'result6' : b[6],
    'result7' : b[7],
    'result8' : b[8],
    'result9' : b[9]
    
    }
   

    
    z = {'data':data}
    return z
##    #Sign-On extends Grid Set-Up(Dashboard)


