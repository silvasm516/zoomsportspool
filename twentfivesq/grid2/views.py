from django.shortcuts import render
from django.template import Template
from django.template import loader
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime, timedelta
import pytz
from pytz import timezone
import time
import datetime
import pytz
from datetime import timedelta
from datetime import date
from datetime import datetime, date, time
# Create your views here.
def Gull(request):
    if request.method == 'POST':
        from grid2.models import Grid
        one = request.POST.get('a1')
        two = request.POST.get('a2')
        three = request.POST.get('a3')
        four = request.POST.get('a4')
        five = request.POST.get('a5')
        six = request.POST.get('a6')
        seven = request.POST.get('a7')
        eight = request.POST.get('a8')
        nine = request.POST.get('a9')
        ten = request.POST.get('a10')
        eleven = request.POST.get('a11')
        twelve = request.POST.get('a12')
        thirteen = request.POST.get('a13')
        fourteen = request.POST.get('a14')
        fifteen = request.POST.get('a15')
        sixteen = request.POST.get('a16')
        seventeen = request.POST.get('a17')
        eighteen = request.POST.get('a18')
        nineteen = request.POST.get('a19')
        twenty = request.POST.get('a20')
        twentyOne = request.POST.get('a21')
        twentyTwo = request.POST.get('a22')
        twentyThree = request.POST.get('a23')
        twentyFour = request.POST.get('a24')
        twentyFive = request.POST.get('a25')
        #p = Grid.objects.create(name1 = one, name2 = two, name3 = three, name4 = four, name5 = five, name6 = six, name7 = seven, name8 = eight, name9 = nine, name10 = ten , name11 = eleven, name12 = twelve, name13 = thirteen, name14 = fourteen, name15 = fifteen, name16 = sixteen, name17 = seventeen, name18 = eighteen, name19 = nineteen ,name20 = twenty, name21 = twentyOne, name22 = twentyTwo, name23 = twentyThree, name24 = twentyFour, name25 = twentyFive)
        p.save()
        

def Trout(request):
    #Creates game to Grid db, and terms to Terms db. Calls Catclone.
    if request.method == 'POST':
        from grid2.models import Grid
        from grid2.models import Terms
        import datetime
        from manager.models import Managers
        from manager.views import Cat
        from manager.views import RunOutTest
        test = RunOutTest(request)
        if test != 'v':
            temp = loader.get_template('BuyGames.html')    
            return HttpResponse(temp.render(test, request))
        else:
            mgrname = request.POST.get('managerName')
            mgrnumber = request.POST.get('mgrNumber')
            authcode = request.POST.get('gridPasswordCode')
            atest = authCodeCheck(authcode)
        if atest == 'false':
            m = Managers.objects.all()
            name = request.session['UsrName']
            mgrId = request.POST.get('mgrNumber')
            n = Managers.objects.get(UsrName = str(name))
            gr = n.GridsOut
            if gr == '':
                gr = 0
            k = ferret(mgrId)
            j = len(k)
            i = "Dashboard"
            hh = "awthcode"
            b = []
            for s in range(0, 10):
                if s >= j:
                    s = 99
                else:
                    s = s
                a = foxer(mgrId, s)
                b.append(a)
            data = {
            'tripper': hh,   
            'tit' : i,
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
            
            

            
            temp = loader.get_template('Dashboard2.html')    
            return HttpResponse(temp.render(z, request))
            return
        atest = uniqueAuthCodeCheck(request, authcode)
        if atest == 'false':
            m = Managers.objects.all()
            name = request.session['UsrName']
            mgrId = request.POST.get('mgrNumber')
            n = Managers.objects.get(UsrName = str(name))
            gr = n.GridsOut
            if gr == '':
                gr = 0
            k = ferret(mgrId)
            j = len(k)
            i = "Dashboard"
            hh = "unique"
            b = []
            for s in range(0, 10):
                if s >= j:
                    s = 99
                else:
                    s = s
                a = foxer(mgrId, s)
                b.append(a)
            data = {
            'tripper': hh,   
            'tit' : i,
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
            
            

            
            temp = loader.get_template('DashBoard2.html')    
            return HttpResponse(temp.render(z, request))
            return 
        hometeam = request.POST.get('homeTeam')
        visitingteam = request.POST.get('visitingTeam')
        dateorig = datetime.datetime.now()
        dogboy = request.POST.get ('gamedate')
        gtime = request.POST.get ('gtime')
        gamedate = dateConvert(dogboy, gtime)
        gametype = request.POST.get('gType')
        s = []
        u = []
        s = randomAssign()
        u = randomAssign()
        p = Grid.objects.create(managerName = mgrname, managerNumber = mgrnumber, homeTeam = hometeam, visitingTeam = visitingteam, dateOriginated = str(dateorig), gameDate = gamedate, gameType = gametype, accessNumber = authcode,
            column1 = s[0], column2 = s[1], column3 = s[2], column4 = s[3],  column5 = s[4],  column6 = s[5], column7 = s[6], column8 = s[7],  column9 = s[8],  column10 = s[9], row1 = u[0], row2 = u[1], row3 = u[2], row4 = u[3],
            row5 = u[4], row6 = u[5], row7 = u[6], row8 = u[7], row9 = u[8], row10 = u[9])
        p.save()
        grid = gridNum()
        price = request.POST.get('squarePrice')
        first = request.POST.get('fQtr')
        secnd = request.POST.get('sQtr')
        third = request.POST.get('tQtr')
        final = request.POST.get('fthQtr')
        minimum = request.POST.get('minPurchase')
        maximum = request.POST.get('maxPurchase')
        frth = request.POST.get('when')
        notes = request.POST.get('notes')
        r = Terms.objects.create(GRID = grid, MIN = minimum, MAX = maximum, PRICE = price, FIRST = first, SECND = secnd, THIRD = third, FINAL = final, FRTH = frth, NOTES = notes)
        r.save()
        t = Catclone(request)
        temp = loader.get_template('DashBoard2.html')    
        return HttpResponse(temp.render(t, request))    
    
        
            


from django.contrib.auth.decorators import login_required

@login_required
def Elephant(request):
    #from grid display panel view buttons to game grid
    if request.method == 'POST':
        import collections  
        from grid2.models import Grid
        from grid2.models import Terms
        import datetime
        from manager.models import Managers
        from manager.views import Cat
        from manager.views import ErrorProc
        from manager.views import preKit
        from django.template.context_processors import csrf
        from django.template import RequestContext
        position = request.POST.get('butsrc')
        n = request.POST.get('mgrNumber')
        g = Grid.objects.all()
        w = ferret(n)
        location = int(position[1])
        actgrds = len(w)
        if len(w) < location + 1:
            ee = ErrorProc(request, n)
            temp = loader.get_template('SignOn.html')
            return HttpResponse(temp.render(ee, request))
        ter = Terms.objects.all() 
        gridnum = w[location] 
        gameNumP = gridnum.id
        num = gameNumP
        de = Giraffe(num)
        popovr = collections.OrderedDict(sorted(de.items()))
        temp = loader.get_template('popover.html') 
        temp.render(popovr)
        request.session['mgrterms'] = {}
        s = g.filter(id = gameNumP) 
        hs = gridnum.homeTeam
        vs = gridnum.visitingTeam
        t = gridnum.gameType
        status = expdaytest(gameNumP, 1)
        rt = request.session['UsrType']
        if status == 'closed':
            return showRandom(gameNumP, hs, vs, t, 'name', request)
        else:
            nam1 =  s[0].name1
            nam2 =  s[0].name2
            nam3 =  s[0].name3
            nam4 =  s[0].name4
            nam5 =  s[0].name5
            nam6 =  s[0].name6
            nam7 =  s[0].name7
            nam8 =  s[0].name8
            nam9 =  s[0].name9
            nam10 = s[0].name10
            nam11 = s[0].name11
            nam12 = s[0].name12
            nam13 = s[0].name13
            nam14 = s[0].name14
            nam15 = s[0].name15
            nam16 = s[0].name16
            nam17 = s[0].name17
            nam18 = s[0].name18
            nam19 = s[0].name19
            nam20 = s[0].name20
            nam21 = s[0].name21
            nam22 = s[0].name22
            nam23 = s[0].name23
            nam24 = s[0].name24
            nam25 = s[0].name25
            ct = {    
            'homT': hs,
            'visT': vs,
            'gType': t,
            'gameNumP' : gameNumP,
            'e1': nam1,
            'e2': nam2,
            'e3': nam3,
            'e4': nam4,
            'e5': nam5,
            'e6': nam6,
            'e7': nam7,
            'e8': nam8,
            'e9': nam9,
            'e10': nam10,
            'e11': nam11,
            'e12': nam12,
            'e13': nam13,
            'e14': nam14,
            'e15': nam15,
            'e16': nam16,
            'e17': nam17,
            'e18': nam18,
            'e19': nam19,
            'e20': nam20,
            'e21': nam21,
            'e22': nam22,
            'e23': nam23,
            'e24': nam24,
            'e25': nam25,
            'rt': rt,
            'popovr': popovr
            }
            
   
    temp = loader.get_template('testGrid.html')
    return HttpResponse(temp.render(ct, request))        


    
from django.contrib.auth.decorators import login_required

@login_required         
def Mammoth(request):
    #FROM PLAYER'S GAMES AVAILABLE(MENUS page)PAGE TO GAME GRID 
    from grid2.models import Grid
    from grid2.models import Terms
    import datetime
    from manager.models import Managers
    from manager.views import Cat
    from django.template.context_processors import csrf
    from django.template import RequestContext
    g = Grid.objects.all()
    gridnum = request.POST.get('gameNumP')
    s = g.filter(id = gridnum)
    play = request.POST.get('player1')
    name = request.session['UsrName']
    hs = s[0].homeTeam
    vs = s[0].visitingTeam
    t = s[0].gameType
    status = expdaytest(gridnum, 1)
    rt = request.session['UsrType']
    if status == 'closed':
        return showRandom(gridnum, hs, vs, t, play, request)
    else:
        nam1 =  s[0].name1
        nam2 =  s[0].name2
        nam3 =  s[0].name3
        nam4 =  s[0].name4
        nam5 =  s[0].name5
        nam6 =  s[0].name6
        nam7 =  s[0].name7
        nam8 =  s[0].name8
        nam9 =  s[0].name9
        nam10 = s[0].name10
        nam11 = s[0].name11
        nam12 = s[0].name12
        nam13 = s[0].name13
        nam14 = s[0].name14
        nam15 = s[0].name15
        nam16 = s[0].name16
        nam17 = s[0].name17
        nam18 = s[0].name18
        nam19 = s[0].name19
        nam20 = s[0].name20
        nam21 = s[0].name21
        nam22 = s[0].name22
        nam23 = s[0].name23
        nam24 = s[0].name24
        nam25 = s[0].name25    
        ct = {
        'e1': nam1,
        'e2': nam2,
        'e3': nam3,
        'e4': nam4,
        'e5': nam5,
        'e6': nam6,
        'e7': nam7,
        'e8': nam8,
        'e9': nam9,
        'e10': nam10,
        'e11': nam11,
        'e12': nam12,
        'e13': nam13,
        'e14': nam14,
        'e15': nam15,
        'e16': nam16,
        'e17': nam17,
        'e18': nam18,
        'e19': nam19,
        'e20': nam20,
        'e21': nam21,
        'e22': nam22,
        'e23': nam23,
        'e24': nam24,
        'e25': nam25,
        'playet': name,
        'homT': hs,
        'visT': vs,
        'gType': t,
        'gameNumP': gridnum,
        't': t,
        'rt': rt
        }
        
        temp = loader.get_template('testGrid.html')    
        return HttpResponse(temp.render(ct, request))


from django.contrib.auth.decorators import login_required

@login_required    
def Mastedon(request):
    #CREATES 'TERMS' MODAL FROM MENUS PAGE
    import datetime
    from manager.models import Managers
    from manager.views import Cat
    #from django.template.context_processors import csrf
    from django.template import RequestContext
    from grid2.models import Grid
    from grid2.models import Terms
    
    g = Grid.objects.all()
    t = Terms.objects.all()
    gridnum = request.POST.get('gameNumP')
    g = g.filter(id = gridnum)
    t = t.filter(GRID = gridnum)
##    gridnum = request.GET.get('gameNumP') 
    name = g[0].managerName
    homet = g[0].homeTeam
    visitt = g[0].visitingTeam
    gamedate = g[0].gameDate
    price = t[0].PRICE
    minn = t[0].MIN
    maxx = t[0].MAX
    firstpo = t[0].FIRST
    secondpo = t[0].SECND
    thirdpo = t[0].THIRD
    finalpo = t[0].FINAL
    last = t[0].FRTH
    notes = t[0].NOTES
    gamnum = gridnum
    gg = "display:none" 
    if last == '1':
            FINAL_PAYOUT_AT_ = 'End of fourth Qtr score'
    else: 
            FINAL_PAYOUT_AT_ = 'End of game score'
            
    modal = {}        
    closes = deadline(gridnum, gamedate) + timedelta(hours = -4.00) 
    data = {
            't0' : gg,
            't1' : gg,
            't2' : gg,
            't3' : gg,
            't4' : gg,
            't5' : gg,
            't6' : gg,
            't7' : gg,
            't8' : gg,
            't9' : gg,
            'vv0' : gg,
            'vv1' : gg,
            'vv2' : gg,
            'vv3' : gg,
            'vv4' : gg,
            'vv5' : gg,
            'vv6' : gg,
            'vv7' : gg,
            'vv8' :gg,
            'vv9' : gg,
            'n0' : gg,
            'n1' : gg,
            'n2' : gg,
            'n3' : gg,
            'n4' : gg,
            'n5' : gg,
            'n6' : gg,
            'n7' : gg,
            'n8' : gg,
            'n9' : gg,
            'vw0' : gg,
            'vw1' : gg,
            'vw2' : gg,
            'vw3' : gg,
            'vw4' : gg,
            'vw5' : gg,
            'vw6' : gg,
            'vw7' : gg,
            'vw8' : gg,
            'vw9' : gg
            }
    modal = {
            'price': price,
            'min': minn,
            'firstQtr': firstpo,
            'secQtr' : secondpo,
            'thirdQtr' : thirdpo,
            'final' : finalpo,	    
            'eog' : FINAL_PAYOUT_AT_,
            'name' : name,
            'gamnum' : gamnum,
            'homeT' : homet,
            'visitT' : visitt,
            'gameDat' : gamedate,
            'closes'  : closes,
            'max' :  maxx,
            'notes' : notes,
            'dog' : 'loaded',
            'data': data
            } 
       
    temp = loader.get_template('Menus.html')
    return HttpResponse(temp.render(modal,request))
    


            
        
def Catclone(request):
    #assigns games to grid display panel
    from django.shortcuts import render
    from django.template import Template
    from django.template import loader
    from django.http import HttpResponse
    from manager.models import Managers
    from django.template.context_processors import csrf
    from django.template import RequestContext

    m = Managers.objects.all()
    
    mgrId = request.POST.get('mgrNumber')
    name = request.POST.get('managerName')
    aa = m.filter(id = mgrId)
    first = aa[0].FirstName
    #first = ident.FirstName 
    k = ferret(mgrId)
    j = len(k)
    b = []
    ma = Managers.objects.get(UsrName = str(name))
    if ma.GridsOut == 999:
        gridsout = 'U'
    else:
        ma.GridsOut = ma.GridsOut - 1
        ma.save()
        gridsout = ma.GridsOut 
    for s in range(0, 10):
        if s >= j:
            s = 99
        else:
            s = s
        a = foxer(mgrId, s)
        b.append(a)
    data = {
    'firstname':first,
    'userName' :name,
    'mgrId' :mgrId,
    'gridsout': gridsout, 
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
    return c
    #Sign-On extends Grid Set-Up(Dashboard)

    
def ferret(i):
    #filters Grid db to instances of that manager's active grids
    from django.template.context_processors import csrf
    from grid2.models import Grid
    g = Grid.objects.all()
    w = g.filter(managerNumber = i)
    y = w.filter(active = '10')
    return y



def weasel(mgrId, o, bbb, ac):
#FOR MENUS TEMPLATE   

    ik = mgrId
    from django.template.context_processors import csrf
    from grid2.models import Grid
    from django.template import RequestContext
    pp = o
    g = Grid.objects.all()
    z = g.filter(managerNumber = ik)
    kk = z.filter(accessNumber = ac)
    mbefore = kk.filter(active = '10')
    
    for mt in mbefore:
        gnum = mt.id
        exx = expdaytest(gnum, 2)
        if exx == "expired":
            mbefore = mbefore.exclude(id = gnum)        
    m = mbefore
    mm = m.filter(gameType = 'p')
    c = m.filter(gameType = 'c')
        
    #EVALUATES BLANK POSITIONS

    if pp >= (len(c)+ len(mm)):
        h = str(" ")
        v = str(" ")
        games = {'homes': h, 'visit':v}
                 
              
        return games

    if bbb >len(mm) and bbb < 10 :
        h = str(" ")
        v = str(" ")
        games = {'homec':h, 'visitc':v}
              
        return games
    

    

    
    #EVALUATES POSITIONS FOR COLLEGE GAMES
    if len(c) > 0 and pp < len(c):
        hc = c[pp].homeTeam + " " + "vs"
        vc = c[pp].visitingTeam 
        
        games = {'homec':hc, 'visitc':vc}
            
           
        return games
    
    #EVALUATES POSITIONS FOR PRO GAMES
        
    elif pp >= len(c) and pp < (len(m) + len(c)):
        pq = (pp - len(c))
        h = mm[pq].homeTeam + " " + "vs"
        v = mm[pq].visitingTeam
        
        games = {'homes':h, 'visit':v}
                 
        return games

    


def foxer(mgrId, o):
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


#DETERMINES A GRID'S DEADLINE BASED ON GAMEDATE
def deadline(gridno, gameDate):
    from datetime import datetime, timedelta
    import pytz
    from pytz import timezone
    import time
    import datetime
    import pytz
    from datetime import timedelta
    from datetime import date
    from datetime import datetime, date, time
    from grid2.models import Grid
    g = Grid.objects.all()
    d = g.filter(id = gridno)
    e = d[0].gameDate
    deadlineDay =  e + timedelta(days = -1.25)
    t = time(23, 59, 59)
    ##UTC midnight time:
    utcTime = datetime.combine(deadlineDay, t)
    deadline = utcTime + timedelta(hours = 4.0)
    
    return deadline	




#USES DATETIME FUNCTIONS TO TEST A GRID NO. IF EXPIRED, OR CLOSED
def expdaytest(gridno, test):
    import time
    import datetime
    from datetime import timedelta, datetime, tzinfo
    from datetime import date
    from grid2.models import Grid
    i = 0
    k = 0
    g = Grid.objects.all()
    num = gridno
    typ = test
    dn = datetime
    tday = dn.now()
    ge = g.filter(id = num)    
    if typ == 1:
        ge = g.filter(id = num)
        for x in range(0, len(ge)):
            d = ge[x].gameDate
            d = d.replace(tzinfo = None)
            dl = deadline(ge, d)
            if dl < tday:
                    test = "closed"    
            else:
                pass
            i = i + 1
    elif typ == 2:
        ge = g.filter(id = num)
        for z in range(0, len(ge)):
            d = ge[z].gameDate
            d = d.replace(tzinfo = None)
            e = timedelta(days = 1) 
            f = d + e
        if tday > f:                       
                test = "expired"
        else:
                test = " "
        k = k + 1
    
    return test


#UPDATES A MANAGERS ACTIVE GRID'S STATUS TO DB (I.E. ADJUSTS 'ACTIVE' FIELD VALUE)
def update(mgrid):
    from grid2.models import Grid
    from grid2.models import Terms
    from manager.models import Managers
    from grid2.views import expdaytest
    g = Grid.objects.all()
    mgrgs = g.filter(managerNumber = mgrid)
    for x in range(0, len(mgrgs)):
        n = mgrgs[x].id
        gr = expdaytest(n, 2) 
        if gr == 'expired':
            gd = Grid.objects.get(id = n)
            gdx = gd.active
            gdx = int(gdx)  
            if gdx >= 30:
                return 
            elif gdx == 10:
                gdx = gdx + 20
                gd.active = str(gdx) 
                gd.save()
        else:
            if gr == '': 
                pass
    for x in range(0, len(mgrgs)):
        n = mgrgs[x].id
        gr = expdaytest(n, 1)
        if gr == 'closed':
            go = Grid.objects.get(id = n)
            gox = go.active
            gox = int(gox)
            if gox == 10: 
               gox = gox + 0
               go.active = str(gox)
               go.save() 
            if gox >= 20:


               return 

#FROM GRID PAGE TO GRID PAGE AFTER SAVE BUTTON CLICKED.
from django.contrib.auth.decorators import login_required

@login_required            
def Badger(request):
    import collections
    from grid2.models import Grid
    from grid2.models import Terms
    import datetime
    from manager.models import Managers
    from manager.views import Cat
    from django.template.context_processors import csrf
    from django.template import RequestContext
    from grid2.models import Grid
    

   
    if request.method == 'POST' or 'GET':
        gridnum = request.POST.get('gameNum')
        ear = request.POST.get('player')
        if ear == "":
            un = "un"
            t = {
                'rsn':un}
            temp = loader.get_template('GridSaveError.html') 
            return HttpResponse(temp.render(t, request))
        g = Grid.objects.all()
        t = g.filter(id = gridnum)
        t2 = t[0].gameType
        s = g.filter(id = gridnum)
        hs = s[0].homeTeam
        vs = s[0].visitingTeam
        o = g.filter(id = gridnum)
        num = gridnum
        (de) = Giraffe(gridnum)
        popovr = collections.OrderedDict(sorted(de.items()))
        vname = "";
        name = 'name';
        flagg = 'flagg'
        rt = request.session['UsrType']
  # GET "d" VALUES AND CREATE LIST OF CURRENT PLAYER(ear)SELECTIONS STORED IN "current"      
        a = []
        names = []
        current = []
        for n in range(0, 25):
            e = 'd' + str(n)
            a.append(request.POST.get(e))
        x = 0    
        for m in a:
            x = x + 1
            if m == ear:
                current.append(x)
                
                
 #CONCATENATE PLAYER'S SELECTED NUMBERS WITH STRING "name" TO USE AS VARIABLE FOR DB FIELD TO BE UPDATED
        if len(current)==25:
            return
        for z in range(0, len(current)):
            names.append(name + str(current[z]))

 #UPDATE DB FOR CURRENT SELECTION           
        x = 0    
        for n in names:

            o.update(**{n : ear})
            x = x + 1

        
        nam1 =  s[0].name1
        nam2 =  s[0].name2
        nam3 =  s[0].name3
        nam4 =  s[0].name4
        nam5 =	s[0].name5
        nam6 =	s[0].name6
        nam7 =  s[0].name7
        nam8 =	s[0].name8
        nam9 =	s[0].name9
        nam10 =	s[0].name10
        nam11 =	s[0].name11
        nam12 =	s[0].name12
        nam13 =	s[0].name13
        nam14 =	s[0].name14
        nam15 =	s[0].name15
        nam16 =	s[0].name16
        nam17 =	s[0].name17
        nam18 =	s[0].name18
        nam19 =	s[0].name19
        nam20 =	s[0].name20
        nam21 =	s[0].name21
        nam22 =	s[0].name22
        nam23 =	s[0].name23
        nam24 =	s[0].name24
        nam25 =	s[0].name25
        w = {
        'e1': nam1,
        'e2': nam2,
        'e3': nam3,
        'e4': nam4,
        'e5': nam5,
        'e6': nam6,
        'e7': nam7,
        'e8': nam8,
        'e9': nam9,
        'e10': nam10,
        'e11': nam11,
        'e12': nam12,
        'e13': nam13,
        'e14': nam14,
        'e15': nam15,
        'e16': nam16,
        'e17': nam17,
        'e18': nam18,
        'e19': nam19,
        'e20': nam20,
        'e21': nam21,
        'e22': nam22,
        'e23': nam23,
        'e24': nam24,
        'e25': nam25,
        'player': ear,
        'homT': hs,
        'visT': vs,
        'gType': t2,
        'gameNumP': gridnum,
        'flagg' : flagg,
        'rt': rt,
        'popovr': popovr
      }  
    temp = loader.get_template('testGrid.html')    
    return HttpResponse(temp.render(w, request))    
        
        
 # randomizes a list of ten integers 0 tru 9.
def randomAssign():
    import random
    import numbers
    import RNumbers
    r =[1,2,3,4,5,6,7,8,9,0]
    random.shuffle(r)
    random.shuffle(r)
    return r       

 #renders random numbers on grid
def showRandom(gridnum, hs, vs, t, play, request):
    import collections
    from grid2.models import Grid
    from django.template.context_processors import csrf
    from django.template import RequestContext 
    g = Grid.objects.all()
    n = g.filter(id = gridnum)
    rt = request.session['UsrType']
    num = gridnum 
    de = Giraffe(num)
    col1 =n[0].column1
    col2 =n[0].column2
    col3 =n[0].column3
    col4 =n[0].column4
    col5 =n[0].column5
    col6 =n[0].column6
    col7 =n[0].column7
    col8 =n[0].column8
    col9 =n[0].column9
    col10 =n[0].column10
    ro1 = n[0].row1
    ro2 = n[0].row2
    ro3 = n[0].row3
    ro4 = n[0].row4
    ro5 = n[0].row5
    ro6 = n[0].row6
    ro7 = n[0].row7
    ro8 = n[0].row8
    ro9 = n[0].row9
    ro10 = n[0].row10
    nam1 =  n[0].name1
    nam2 =  n[0].name2
    nam3 =  n[0].name3
    nam4 =  n[0].name4
    nam5 =  n[0].name5
    nam6 =  n[0].name6
    nam7 =  n[0].name7
    nam8 =  n[0].name8
    nam9 =  n[0].name9
    nam10 = n[0].name10
    nam11 = n[0].name11
    nam12 = n[0].name12
    nam13 = n[0].name13
    nam14 = n[0].name14
    nam15 = n[0].name15
    nam16 = n[0].name16
    nam17 = n[0].name17
    nam18 = n[0].name18
    nam19 = n[0].name19
    nam20 = n[0].name20
    nam21 = n[0].name21
    nam22 = n[0].name22
    nam23 = n[0].name23
    nam24 = n[0].name24
    nam25 = n[0].name25
    ct = {
    'dig': 'dig',
    'co1': col1,
    'co2': col2,
    'co3': col3,
    'co4': col4,
    'co5': col5,
    'co6': col6,
    'co7': col7,
    'co8': col8,
    'co9': col9,
    'co10': col10,
    'r1': ro1,
    'r2': ro2,
    'r3': ro3,
    'r4': ro4,
    'r5': ro5,
    'r6': ro6,
    'r7': ro7,
    'r8': ro8,
    'r9': ro9,
    'r10': ro10,
    'e1': nam1,
    'e2': nam2,
    'e3': nam3,
    'e4': nam4,
    'e5': nam5,
    'e6': nam6,
    'e7': nam7,
    'e8': nam8,
    'e9': nam9,
    'e10': nam10,
    'e11': nam11,
    'e12': nam12,
    'e13': nam13,
    'e14': nam14,
    'e15': nam15,
    'e16': nam16,
    'e17': nam17,
    'e18': nam18,
    'e19': nam19,
    'e20': nam20,
    'e21': nam21,
    'e22': nam22,
    'e23': nam23,
    'e24': nam24,
    'e25': nam25,
    'player': play,
    'homT': hs,
    'visT': vs,
    'gType': t,
    'gameNumP': gridnum,
    'rt': rt,
    'popovr': de
    }
    temp = loader.get_template('testGrid.html')    
    return HttpResponse(temp.render(ct, request))


#renders random numbers on grid
from django.contrib.auth.decorators import login_required

@login_required
def showRandomArchiveP(request, gridnum, hs, vs, t, play):
    import collections
    from grid2.models import Grid
    from django.template.context_processors import csrf
    from django.template import RequestContext 
    g = Grid.objects.all()
    n = g.filter(id = gridnum)
    rt = 'a'
    num = gridnum 
    de = Giraffe(num)
    col1 =n[0].column1
    col2 =n[0].column2
    col3 =n[0].column3
    col4 =n[0].column4
    col5 =n[0].column5
    col6 =n[0].column6
    col7 =n[0].column7
    col8 =n[0].column8
    col9 =n[0].column9
    col10 =n[0].column10
    ro1 = n[0].row1
    ro2 = n[0].row2
    ro3 = n[0].row3
    ro4 = n[0].row4
    ro5 = n[0].row5
    ro6 = n[0].row6
    ro7 = n[0].row7
    ro8 = n[0].row8
    ro9 = n[0].row9
    ro10 = n[0].row10
    nam1 =  n[0].name1
    nam2 =  n[0].name2
    nam3 =  n[0].name3
    nam4 =  n[0].name4
    nam5 =  n[0].name5
    nam6 =  n[0].name6
    nam7 =  n[0].name7
    nam8 =  n[0].name8
    nam9 =  n[0].name9
    nam10 = n[0].name10
    nam11 = n[0].name11
    nam12 = n[0].name12
    nam13 = n[0].name13
    nam14 = n[0].name14
    nam15 = n[0].name15
    nam16 = n[0].name16
    nam17 = n[0].name17
    nam18 = n[0].name18
    nam19 = n[0].name19
    nam20 = n[0].name20
    nam21 = n[0].name21
    nam22 = n[0].name22
    nam23 = n[0].name23
    nam24 = n[0].name24
    nam25 = n[0].name25
    ct = {
    'dig': 'dig',
    'co1': col1,
    'co2': col2,
    'co3': col3,
    'co4': col4,
    'co5': col5,
    'co6': col6,
    'co7': col7,
    'co8': col8,
    'co9': col9,
    'co10': col10,
    'r1': ro1,
    'r2': ro2,
    'r3': ro3,
    'r4': ro4,
    'r5': ro5,
    'r6': ro6,
    'r7': ro7,
    'r8': ro8,
    'r9': ro9,
    'r10': ro10,
    'e1': nam1,
    'e2': nam2,
    'e3': nam3,
    'e4': nam4,
    'e5': nam5,
    'e6': nam6,
    'e7': nam7,
    'e8': nam8,
    'e9': nam9,
    'e10': nam10,
    'e11': nam11,
    'e12': nam12,
    'e13': nam13,
    'e14': nam14,
    'e15': nam15,
    'e16': nam16,
    'e17': nam17,
    'e18': nam18,
    'e19': nam19,
    'e20': nam20,
    'e21': nam21,
    'e22': nam22,
    'e23': nam23,
    'e24': nam24,
    'e25': nam25,
    'player': play,
    'homT': hs,
    'visT': vs,
    'gType': t,
    'gameNumP': gridnum,
    'rt': rt,
    'popovr': de
    }
    temp = loader.get_template('testGrid.html')    
    return HttpResponse(temp.render(ct, request))


from django.contrib.auth.decorators import login_required

@login_required    
def TRex(request):
    # from archive to grid
    from grid2.models import Grid
    g = Grid.objects.all()
    d = []
    
    if request.method == 'POST':
        gridnum = request.POST.get('game No')
        code = request.POST.get('auth code')
        digtest = gridnum.isdigit()
        if digtest == False:
            from twentfivesq.views import archiveGameList
            games = archiveGameList(request)
            c ={'rsn':'num', 'msg': 'The Game Number Is Invalid', 'games': games,
               'tit': 'Archive' }
            temp = loader.get_template('ArchiveM.html')
            return HttpResponse(temp.render(c,request))
        ge = int(gridnum)
        fe = g.filter(id = ge)
        if fe.exists() == False:
            from twentfivesq.views import archiveGameList
            games = archiveGameList(request)
            c ={'rsn':'num', 'msg': 'The Game Number Is Invalid', 'games': games,
                   'tit': 'Archive' }
            temp = loader.get_template('ArchiveM.html')
            return HttpResponse(temp.render(c,request))
        
        from manager.models import Managers
        m = Managers.objects.all()
        name = request.session['UsrName']
        nm = m.filter(UsrName = name)
        ln = nm[0].LastName
        maname = fe[0].managerName
        if maname != name:
            cat = dog
            from twentfivesq.views import archiveGameList
            games = archiveGameList(request)
            c ={'rsn':'num', 'msg': 'The Game Number Is Invalid', 'games': games,
                   'tit': 'Archive' }
            temp = loader.get_template('ArchiveM.html')
            return HttpResponse(temp.render(c,request))
        
        d = g.filter(accessNumber = code)
        e = d.filter(id = gridnum)
        z = e        
        le = len(d)
        lf = len(e)
        ztest = expdaytest(gridnum, 2)
        
        if ztest != "expired":
            from twentfivesq.views import archiveGameList
            games = archiveGameList(request)
            
            c ={'rsn':'num', 'msg': 'The Game Number Is Invalid', 'games': games,
               'tit': 'Archive' }
            temp = loader.get_template('ArchiveM.html')
            return HttpResponse(temp.render(c,request))
        
        if le == 0:
            from twentfivesq.views import archiveGameList
            games = archiveGameList(request)
            
            reason = 'code'
            msg = 'Sorry, But That Code Does Not Exist'
            c = {
                'rsn': reason,
                'msg': msg,
                'tit': 'Archive',
                'games': games
                }
            temp = loader.get_template('ArchiveM.html')
            return HttpResponse(temp.render(c, request))
        
        if lf == 0:
            from twentfivesq.views import archiveGameList
            games = archiveGameList(request)
            
                
            reason = 'gridNo'
            msg = 'Sorry, But That Grid Number Is Invalid'
            c = {
                'rsn': reason,
                'msg': msg,
                'tit': 'Archive',
                'games': games
                }
            temp = loader.get_template('ArchiveM.html')
            return HttpResponse(temp.render(c, request))
        
        else:
        

        
            import datetime
            from manager.models import Managers
            from manager.views import Cat
            from django.template.context_processors import csrf
            from django.template import RequestContext
            ##g = Grid.objects.all()
            ## gridnum = request.POST.get('gameNumP')
            ## s = g.filter(id = gridnum)
            play = request.POST.get('player')
            ##hs = g.filter(id = z)[0].homeTeam
            hs = z[0].homeTeam 
            ##vs = g.filter(id = z)[0].visitingTeam
            vs = z[0].visitingTeam 
            ##t = g.filter(id = z)[0].gameType
            t = z[0].gameType
            x = z[0].id
            status = expdaytest(x, 2)
            rt = request.session['UsrType']
            if status == 'expired':
                 return showRandom(gridnum, hs, vs, t, play, request)
            else:
                nam1 =  s[0].name1
                nam2 =  s[0].name2
                nam3 =  s[0].name3
                nam4 =  s[0].name4
                nam5 =  s[0].name5
                nam6 =  s[0].name6
                nam7 =  s[0].name7
                nam8 =  s[0].name8
                nam9 =  s[0].name9
                nam10 = s[0].name10
                nam11 = s[0].name11
                nam12 = s[0].name12
                nam13 = s[0].name13
                nam14 = s[0].name14
                nam15 = s[0].name15
                nam16 = s[0].name16
                nam17 = s[0].name17
                nam18 = s[0].name18
                nam19 = s[0].name19
                nam20 = s[0].name20
                nam21 = s[0].name21
                nam22 = s[0].name22
                nam23 = s[0].name23
                nam24 = s[0].name24
                nam25 = s[0].name25    
                ct = {
                'e1': nam1,
                'e2': nam2,
                'e3': nam3,
                'e4': nam4,
                'e5': nam5,
                'e6': nam6,
                'e7': nam7,
                'e8': nam8,
                'e9': nam9,
                'e10': nam10,
                'e11': nam11,
                'e12': nam12,
                'e13': nam13,
                'e14': nam14,
                'e15': nam15,
                'e16': nam16,
                'e17': nam17,
                'e18': nam18,
                'e19': nam19,
                'e20': nam20,
                'e21': nam21,
                'e22': nam22,
                'e23': nam23,
                'e24': nam24,
                'e25': nam25,
                'person': play,
                'homT': hs,
                'visT': vs,
                'gType': t,
                'gameNumP': gridnum,
                'rt': rt
                }

                temp = loader.get_template('testGrid.html')    
                return HttpResponse(temp.render(ct, request))       


    
from django.contrib.auth.decorators import login_required

@login_required
def Triceritops(request):
    # from archive to grid
    from grid2.models import Grid
    g = Grid.objects.all()
    d = []    
    if request.method == 'POST':
        gridnum = request.POST.get('game No')
        code = request.POST.get('auth code')
        if gridnum.isdigit(): 
            d = g.filter(accessNumber = code)
            e = d.filter(id = gridnum)
            z = e
        else:
            from twentfivesq.views import archiveGameList
            from twentfivesq.views import archiveGameListP
            games = archiveGameListP(code)
            c ={'rsn':'num', 'msg': 'The Game Number Is Invalid', 'games': games,
               'tit': 'Games Archive' }
            temp = loader.get_template('Archive.html')
            return HttpResponse(temp.render(c,request))
                
        le = len(d)
        lf = len(e) 
        
        
        if le == 0:
            from twentfivesq.views import archiveGameList
            from twentfivesq.views import archiveGameListP
            games = archiveGameListP(code)
            reason = 'code'
            msg = 'Sorry, But That Code Does Not Exist'
            c = {
                'rsn': reason,
                'msg': msg,
                'tit': 'Games Archive',
                'games': games
                }
            temp = loader.get_template('Archive.html')
            return HttpResponse(temp.render(c, request))
        
        if lf == 0:
            from twentfivesq.views import archiveGameList
            from twentfivesq.views import archiveGameListP
            games = archiveGameListP(code) 
            reason = 'gridNo'
            msg = 'Sorry, But That Grid Number Is Invalid'
            c = {
                'rsn': reason,
                'msg': msg,
                'tit': 'Games Archive'
                
                }
            temp = loader.get_template('Archive.html')
            return HttpResponse(temp.render(c, request))

        from grid2.views import expdaytest
        lg = expdaytest(e, 2)
        if lg != "expired":
            from twentfivesq.views import archiveGameList
            from twentfivesq.views import archiveGameListP 
            games = archiveGameListP(code) 
            reason = 'gridNo'
            msg = 'Sorry, But That Grid Number Is Invalid'
            c = {
                'rsn': reason,
                'msg': msg,
                'tit': 'Games Archive'
                
                }
            temp = loader.get_template('Archive.html')
            return HttpResponse(temp.render(c, request))

            
        else:
        

        
            import datetime
            #import expdaytest
            from manager.models import Managers
            from manager.views import Cat
            from django.template.context_processors import csrf
            from django.template import RequestContext
##            play = request.POST.get('player')
            play = request.session['UsrName']
            hs = z[0].homeTeam 
            vs = z[0].visitingTeam 
            t = z[0].gameType
            x = z[0].id
            status = expdaytest(x, 2)
            nt = 'a'
            num = gridnum 
            de = Giraffe(num)
            if status == 'expired':
                return showRandomArchiveP(request, gridnum, hs, vs, t, play)
            else:
                nam1 =  s[0].name1
                nam2 =  s[0].name2
                nam3 =  s[0].name3
                nam4 =  s[0].name4
                nam5 =  s[0].name5
                nam6 =  s[0].name6
                nam7 =  s[0].name7
                nam8 =  s[0].name8
                nam9 =  s[0].name9
                nam10 = s[0].name10
                nam11 = s[0].name11
                nam12 = s[0].name12
                nam13 = s[0].name13
                nam14 = s[0].name14
                nam15 = s[0].name15
                nam16 = s[0].name16
                nam17 = s[0].name17
                nam18 = s[0].name18
                nam19 = s[0].name19
                nam20 = s[0].name20
                nam21 = s[0].name21
                nam22 = s[0].name22
                nam23 = s[0].name23
                nam24 = s[0].name24
                nam25 = s[0].name25    
                ct = {
                'e1': nam1,
                'e2': nam2,
                'e3': nam3,
                'e4': nam4,
                'e5': nam5,
                'e6': nam6,
                'e7': nam7,
                'e8': nam8,
                'e9': nam9,
                'e10': nam10,
                'e11': nam11,
                'e12': nam12,
                'e13': nam13,
                'e14': nam14,
                'e15': nam15,
                'e16': nam16,
                'e17': nam17,
                'e18': nam18,
                'e19': nam19,
                'e20': nam20,
                'e21': nam21,
                'e22': nam22,
                'e23': nam23,
                'e24': nam24,
                'e25': nam25,
                'person': play,
                'homT': hs,
                'visT': vs,
                'gType': t,
                'gameNumP': gridnum,
                'nt': nt,
                'tit': 'Games Archive'
                }
                temp = loader.get_template('testGrid.html')    
                return HttpResponse(temp.render(ct, request))     



    
            
def Giraffe(gameNo):
    #CREATES 'TERMS' FILE FROM GRID PAGE. 
    import collections 
    import datetime
    from manager.models import Managers
    from manager.views import Cat
    #from django.template.context_processors import csrf
    from django.template import RequestContext
    from grid2.models import Grid
    from grid2.models import Terms
    import requests
    g = Grid.objects.all()
    g = g.filter(id = gameNo)
    t = Terms.objects.all()
    t = t.filter(GRID = gameNo) 
    #gridnum = request.POST.get('gameNumber')
    gridnum = gameNo
    authcode = g[0].accessNumber
    homet = g[0].homeTeam
    visitt = g[0].visitingTeam
    gamedate = g[0].gameDate
    grid = t[0].GRID
    price = t[0].PRICE
    minn = t[0].MIN
    maxx = t[0].MAX
    firstpo = t[0].FIRST
    secondpo = t[0].SECND
    thirdpo = t[0].THIRD
    finalpo = t[0].FINAL
    last = t[0].FRTH
    notes = t[0].NOTES
    gamnum = gridnum
    gg = "display:none" 
    if last == '1':
            FINAL_PAYOUT_AT_ = 'End of fourth Qtr score'
    else: 
            FINAL_PAYOUT_AT_ = 'End of game score'
            
    closes = deadline(gridnum, gamedate) + timedelta(hours = -4.00)
    popvr ={
    '0.grid:': grid,
    '01.price:': price,
    '02.min sq pur:' : minn,
    '03.firstQtr:' : firstpo,
    '04.secQtr:'  : secondpo,
    '05.thdQtr:' : thirdpo,
    '06.final:' : finalpo,	    
    '07.eog:' : FINAL_PAYOUT_AT_,
    '08.auth:' : authcode,
    '09.gamnum:' : gamnum,
    '10.homeT:' : homet,
    '11.visitT:' : visitt,
    '12.gameDat:' : gamedate,
    '13.max sq pur:'  : maxx,
    '14.notes:' : notes}
    
    ordpop = collections.OrderedDict(sorted(popvr.items(), key = lambda t: t[0]))
    
         
             
   
    return ordpop


from django.contrib.auth.decorators import login_required

@login_required
def Petrodyl(request, gridnum):   
    import datetime
    from manager.models import Managers
    from manager.views import Cat
    #from django.template.context_processors import csrf
    from django.template import RequestContext
    from grid2.models import Grid
    from grid2.models import Terms
    
    g = Grid.objects.all()
    t = Terms.objects.all()
    #gridnum = request.POST.get('gameNumP')
   ## gridnum = request.GET.get('gameNumP')
    grid = t[0].GRID
    name = g[0].managerName
    homet = g[0].homeTeam
    visitt = g[0].visitingTeam
    gamedate = g[0].gameDate
    price = t[0].PRICE
    minn = t[0].MIN
    maxx = t[0].MAX
    firstpo = t[0].FIRST
    secondpo = t[0].SECND
    thirdpo = t[0].THIRD
    finalpo = t[0].FINAL
    last = t[0].FRTH
    notes = t[0].NOTES
    gamnum = gridnum
    gg = "display:none" 
    if last == '1':
            FINAL_PAYOUT_AT_ = 'End of fourth Qtr score'
    else: 
            FINAL_PAYOUT_AT_ = 'End of game score'
            
    modal = {}        
    closes = deadline(gridnum, gamedate) + timedelta(hours = -4.00) + 'Eastern'
    data = {
            'price': price,
            'min': minn,
            'firstQtr': firstpo,
            'secQtr' : secondpo,
            'thirdQtr' : thirdpo,
            'final' : finalpo,	    
            'eog' : FINAL_PAYOUT_AT_,
            'name' : name,
            'gamnum' : gamnum,
            'homeT' : homet,
            'visitT' : visitt,
            'gameDat' : gamedate,
            'closes'  : closes,
            'max' :  maxx,
            'notes' : notes,
            'dog' : 'loaded',
            'data': data
            } 
    temp = loader.get_template('Menus.html')
    return HttpResponse(temp.render(data,request))



def openStatusTest(grdNo):
    #Tests grids for open, full, or closed status for labeling on Menus Template(Games Avail.Page)
    #Called by "Fish" function.
    from grid2.models import Grid
    g = Grid.objects.all()
    n = grdNo
    c = expdaytest(n, 1)
    if c == "closed":
        t = "closed"
        return t
    g2 = g.get(id =  str(n))
    ant1 = g2.name1
    ant2 = g2.name2
    ant3 = g2.name3
    ant4 = g2.name4
    ant5 = g2.name5
    ant6 = g2.name6
    ant7 = g2.name7
    ant8 = g2.name8
    ant9 = g2.name9
    ant10 = g2.name10
    ant11 = g2.name11
    ant12 = g2.name12
    ant13 = g2.name13
    ant14 = g2.name14
    ant15 = g2.name15
    ant16 = g2.name16
    ant17 = g2.name17
    ant18 = g2.name18
    ant19 = g2.name19
    ant20 = g2.name20
    ant21 = g2.name21
    ant22 = g2.name22
    ant23 = g2.name23
    ant24 = g2.name24 
    ant25 = g2.name25
    ant = [ant1, ant2, ant3, ant4, ant5, ant6, ant7, ant8, ant9, ant10, ant11, ant12, ant13, ant14, ant15, ant16, ant17, ant18, ant19, ant20, ant21, ant22, ant23, ant24, ant25]
    
    
    for zz in range(0, 25):
        if (ant[zz]).isdigit(): 
            t = "open"
            return t
    t = "full"
    return t


##converts date and time submitted to server
##from 'Dashbord' into datetime format for db.
def dateConvert(dte, tme):
    import datetime
    import time
    dt = str(dte)
    stringdate = dt.replace('-', " ", 3) 
    tm = str(tme)
    stringtime = tm.replace(':'," ", 2)
    joinedate = stringdate + "  " + stringtime
    f = '%Y %m %d %H %M'
    gamedate = datetime.datetime.strptime(joinedate, f)
    return gamedate

def numberName(number):
    ##accepts a mgr number and returns the mgr name
    from manager.models import Managers
    mgrNum = number 
    man = Managers.objects.all()
    ide = man.filter(id = mgrNum)
    name = ide[0].UsrName
    return name

def maxLimitExpiration(dat):
    #accepts arbitrary date. Returns boolean 1 = true, 0 = false
    #called by Cat to test expiration of season pass or maxLimit pass
    from manager.models import Managers
    import datetime
    import time
    from datetime import timedelta
    dt = dat
    d = datetime.date.today()
    e = datetime.date.fromordinal(d.toordinal())
    f = e.toordinal()
    #if d.strftime('%d-%m-%Y') > dt:
    if dt.toordinal() < d.toordinal():
        expired = 1
    else:
        expired = 0
    #dumb = moron
    return expired


def authCodeCheck(authcode):
    #checks that access code is correct(six to twelve) number of
    #characters. Called by Trout. 
    from manager.models import Managers 
    a = authcode
    if len(a) < 6: 
        return 'false'
    if len(a) > 12:
        return 'false'
    else:
        return 'true'
    
def uniqueAuthCodeCheck(request,authcode):
    #checks that the grid's access code is not being used by another
    #manager's grid.
    from grid2.models import Grid
    import requests
    activeg = []
    g = Grid.objects.all()
    a = authcode
    activeg = g.filter(active = '10', accessNumber = authcode)
    if activeg == []:
        return 'true'
    else:
        for item in activeg:
            if item.accessNumber == a:
                if item.managerName == request.session['UsrName']:
                    return 'true'
                else:
                    return 'false'
                    
            else:
                return 'true'
            
def gridNum():
    from grid2.models import Grid
    g = Grid.objects.all()
    gridList = []
    for f in g:
        gridList.append(int(f.id))
    maxx = max(gridList)
    gridNum = maxx

    return gridNum
    
        
      
          
    

    
