from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template.context_processors import csrf
from django.template import Template
from django.template import loader

    
def Shome(request):
    if request.method == 'POST':
        pw = request.POST.get('pass')
        if pw != "Fl53002#$":
            b = 'fail'
            a = "ZOOMSPORTSPOOL" 
            c = {
            'tit': a, 
            'verdict': b
            }
            temp = loader.get_template('Hmpage.html')
            return HttpResponse(temp.render(c,request))

            
        else:
            a = "25 SQUARES FOOTBALL" 
            data = {
                'tit' : a,    
                }
            temp = loader.get_template('Some.html')
            return HttpResponse(temp.render(data,request))
        

    
def Hmpage(request):
    b = "" 
    a = "ZOOMSPORTSPOOL" 
    c = {
         'tit': a, 
         'verdict': b
         }
    temp = loader.get_template('Hmpage.html')
    return HttpResponse(temp.render(c,request))




def Ghome(request):
    a = "25 SQUARES FOOTBALL" 
    data = {
        'tit' : a,    
                }
    temp = loader.get_template('Some.html')
    return HttpResponse(temp.render(data,request))





def Grid_FB(request):
    return render(request, 'testGrid.html')
    if request.method == 'GET':
        return HttpResponse(request.GET ['item_text'])

def Contact(request):
  #  if request.method == 'POST':
  #  return HttpResponse(request.POST['item_text'])
   
    
    a = "Contact Us" 
    c = {
         'tit': a,
         
         }
    temp = loader.get_template('twentyFiveSqContact.html')
    return HttpResponse(temp.render(c,request))

def More(request):
  #  if request.method == 'POST':
  #  return HttpResponse(request.POST['item_text'])
    a = "More Information" 
    c = {
         'tit': a, 
         
         }
    temp = loader.get_template('MoreInfoHistory.html')
    return HttpResponse(temp.render(c,request))



def Some(request):
  #  if request.method == 'POST':
  #  return HttpResponse(request.POST['item_text'])
    a = "25 SQUARES FOOTBALL"
    
    data = {
         'title': a,
        
         }
    temp = loader.get_template('Some.html')
    return HttpResponse(temp.render(data,request))





def Archive(request):
   # if request.method == 'POST':
  #  return HttpResponse(request.POST['item_text'])
    if request.method == 'GET':
        #return HttpResponse(request.GET ['item_text'])    
        #return HttpResponse(request.GET ['item_text'])
        from manager.models import Managers
   # if request.method == 'POST':
   #if request.method == 'GET':
        play = request.GET.get('player')
        a = 'Games Archive' 
        c = {
        'tit': a,
        'play' : play,
        }
        temp = loader.get_template('Archive.html')
        return HttpResponse(temp.render(c,request))



def ArchiveM(request):
  #  if request.method == 'POST':
  #  return HttpResponse(request.POST['item_text'])
    games = archiveGameList(request)
    #agnumbers = archiveGameNumber(request)
    if request.method == 'GET':
        #return HttpResponse(request.GET ['item_text'])    
        #return HttpResponse(request.GET ['item_text'])
        from manager.models import Managers
   # if request.method == 'POST':
   #if request.method == 'GET':
        play = request.GET.get('player')
        a = "Archive"

        c = {
        'tit': a,
        'play' : play,
        'games': games
        
        }
        temp = loader.get_template('ArchiveM.html')
        return HttpResponse(temp.render(c,request))       

def archiveGameList(request):
    import time 
    from grid2.models import Grid
    from manager.models import Managers
    m = Managers.objects.all()
    g = Grid.objects.all()
    ##name = request.session['UsrName']
    name = request.session['UsrName']
    u = g.filter(managerName = name)
    s = []
    j = []
    r = {}
    for t in u:
        i = t.id
        j.append(i)
        d = t.gameDate
        e = d.strftime('%d %b %Y')
        r = {'Name': t.managerName, 'Auth': t.accessNumber, 'Number': t.id, 'Date': e}
        h = t.active
        if h != '10':
            s.append(str(r).strip("{}"))
    return s

def gmeList(username):
    ##Validates input to Index form
    import time 
    from grid2.models import Grid
    from manager.models import Managers
    m = Managers.objects.all()
    g = Grid.objects.all()
    name = username
    u = g.filter(managerName = name)
    s = []
    j = []
    z = []
    r = {}
    for t in u:
        i = t.id
        j.append(i)
        d = t.gameDate
        e = d.strftime('%d %b %Y')
        r = {'Name': t.managerName, 'Auth': t.accessNumber, 'Number': t.id, 'Date': e}
        v = r.values()
        z.append(str(v))
        h = t.active
        if h != '10':
            s.append(str(r).strip("{}"))
    return j   

def Index(request):
  #  if request.method == 'POST':
  #  return HttpResponse(request.POST['item_text'])
    if request.method == 'GET':
        #return HttpResponse(request.GET ['item_text'])    
        #return HttpResponse(request.GET ['item_text'])
        from manager.models import Managers
   # if request.method == 'POST':
   #if request.method == 'GET':
        play = request.GET.get ('player')
        a = "Index" 
        c = {
        'tit': a,
        'play' : play,
        }
        temp = loader.get_template('Index.html')
        return HttpResponse(temp.render(c,request))  

        
    
    
  
        



    
def TABLE_LIST_TEST_DRAFT_3(request):
    return render(request, 'twentyFiveSquaresDashboard.html')
    if request.method == 'GET':
        return HttpResponse(request.GET ['item_text']) 

##def Login(request):
##    a = "Player Login" 
##    c = Context({
##         'title': a
##         })
    
##    temp = loader.get_template('login.html')
##    return HttpResponse(temp.render(c,request)) 
##    if request.method == 'GET':
##        return HttpResponse(request.GET ['item_text']) 

def SignUp(request):
    return render(request, 'SignUp.html')
    if request.method == 'GET':
        return HttpResponse(request.GET ['item_text'])
     


def Fish(request):
    from django.views.decorators.csrf import csrf_protect 
    from django.shortcuts import render
    from django.template import Template
    from django.template import loader
    from django.http import HttpResponse
    from manager.models import Managers
    from django.template.context_processors import csrf
    from django.template import RequestContext 
    from player.models import Players
    from grid2.views import openStatusTest
    from player.models import Players
    from grid2.models import Grid
    c ={}
    c.update(csrf(request))
    authcode = request.GET.get('authorization9') 
    email = request.GET.get('email')
    p = Players.objects.all()
    u = []
    bb = 0
    #evaluate player email and authcode. u = all player's email
    for j in range(0, len(p)):
        o = p[j].Email
        u.append(o)
    i =[]
    ii = []
    iii = []
    for t in u:
        e = t.lower() 
        i.append(e)
    ii = getMgrMail()
    iii = i + ii
    v = email.lower()
    #if email is valid but now checking only the player List("i")
   
    
    if v in i:         
        temp = loader.get_template('Menus.html')
        from grid2.models import Grid
        from manager.models import Managers
        from grid2.views import Catclone, ferret, weasel
##        r = Catclone(request)
       

##       OBTAIN MANAGER ID
        g = Grid.objects.all()
        m = Managers.objects.all()
        aa = g.filter(accessNumber = authcode)
        if any(aa) == False:
            msg = "We don't have the code '"+ authcode +"' you entered on record. "
            msg = msg + "Please, contact your Manager Sponser. Or, try another Code."
            temp = loader.get_template('Login.html')
            message = {'msg':msg, 'tit':'Player Login', 'flag':'pw'}
            return HttpResponse(temp.render(message, request))
            
            
        name = aa[0].managerName
        mgr = m.filter(UsrName = name)
        mgrid = mgr[0].id
        from grid2.views import expdaytest
        update(mgrid)
##       OBTAIN PLAYER NAME 
##        u = []
##        for j in range(0, len(p)):
##            o = p[j].Email
##            u.append(o)
##        i =[]
        v = email.lower()
        
        for t in i:
##            e = t.lower() 
##            i.append(e)            
            if v == t:
                for y in range(0, len(p)):
                    a1 = p[y].Email
                    b1 = a1
                    c1 = b1.lower()
                    if v == c1: 
            
                        plaer = p.filter(Email = b1 )
                        first = plaer[0].UsrName
                        d = login(request, first, authcode)
                        u = first
                        request.session['UserName'] = u
                        request.session['UsrType'] = 'p'

                        
                break
        for t in ii:
            if v == t:
                firstname = name
             
        w = len(p) + len(m)
        
        
##      FILTER GRID GET PRO AND COL GAMES AND LEN ACTIVE GAMES
##      OBTAIN GRIDNUMS LISTS.(IN JK TUPLE JK[1] & JK[2] FROM SKUNK)
        jk = ferret2(mgrid, authcode)
        k = jk[0]
        gridNumsP = jk[1]
        gridNumsC = jk[2]
        Pstatus = {}
        Cstatus = {}

        if gridNumsP is not "":
            step = 0
            for gamep in gridNumsP:
                statusP = openStatusTest(gamep)
                Pstatus[step] = statusP
                step = step + 1
        if gridNumsC is not "":
            step2 = 0
            for gamec in gridNumsC:
                statusC = openStatusTest(gamec)
                Cstatus[step2] = statusC
                step2 = step2 + 1
        
        xxx = []
        zzz = []
        
##      CREATING LISTS OF GRID NUMBERS TO TRANSFER TO TEMPLATE TEXTS
##      FOR LATER POSTING TO FIND GRIDS FOR PLAYERS VIA 'VIEW' BUTTONS
        for items in range(0, 10):
             xxx.append("")
             zzz.append("")
        for items in range(0, len(gridNumsP)):
             xxx[items]=(gridNumsP[items])
        for items in range(0, len(gridNumsC)):
             zzz[items]=(gridNumsC[items])
          
             
        # k is active games, b is pro list, cc is college list
        
        j = len(k)
        ik = mgrid
        z = g.filter(managerNumber = ik)
        kk = z.filter(accessNumber = authcode)
##        mbefore = kk.filter(active = '10')
        for mt in kk:
##        for mt in mbefore:
            gnum = mt.id
            exx = expdaytest(gnum, 2)
            if exx == "expired":
                kk = kk.exclude(id = gnum)
##                mbefore = mbefore.exclude(id = gnum)
#       m = mbefore
        m = kk 
       
        mm = m.filter(gameType = 'p')
        c = m.filter(gameType = 'c')
        t = []
        vv = []
        n = []
        vw = []
        b = []
        cc = []
        ccc = 0
        bbb = 0
        gg = "display:none"
        
        for s in range(0, 20):
            a = {}    
            a = weasel(mgrid, s, bbb, authcode)
            
            if ccc < len(c): 
              
                cc.append(a)
                ccc = ccc + 1
                
            elif ccc >= len(c) and ccc < j:
                b.append(a)        
                ccc = ccc + 1
                
            
                  
            else:
                for ff in range(0, 10):
                     t.append("")
                     n.append("")
                     vv.append("background-color:green")
                     vw.append("background-color:green")
                     
                for zz in range(0, 10 - len(c)):
                    r = len(c) + zz
                    cc.append({'homec': " ", 'visitc':" "})
##                    t[r] = gg
##                    vv[r] = gg
                    n[r] = gg
                    vw[r] = gg
                    
                for xx in range(len(mm), 10):
                    b.append({'homes': " ", 'visit':" "})
                    t[xx] = gg
                    vv[xx] = gg
                    
        z = 'Your Available Games'
        klattu = 'WELCOME'        
        ne = request.session['UsrName']    
        data = {
        'result0' : b[0],
        'result1' : b[1],
        'result2' : b[2],
        'result3' : b[3],
        'result4' : b[4],
        'result5' : b[5],
        'result6' : b[6],
        'result7' : b[7],
        'result8' : b[8],
        'result9' : b[9],
        'result10' : cc[0],
        'result11' : cc[1],
        'result12' : cc[2],
        'result13' : cc[3],
        'result14' : cc[4],
        'result15' : cc[5],
        'result16' : cc[6],
        'result17' : cc[7],
        'result18' : cc[8],
        'result19' : cc[9],
        't0' : t[0],
        't1' : t[1],
        't2' : t[2],
        't3' : t[3],
        't4' : t[4],
        't5' : t[5],
        't6' : t[6],
        't7' : t[7],
        't8' : t[8],
        't9' : t[9],
        'n0' : n[0],
        'n1' : n[1],
        'n2' : n[2],
        'n3' : n[3],
        'n4' : n[4],
        'n5' : n[5],
        'n6' : n[6],
        'n7' : n[7],
        'n8' : n[8],
        'n9' : n[9],
        'vv0' : vv[0],
        'vv1' : vv[1],
        'vv2' : vv[2],
        'vv3' : vv[3],
        'vv4' : vv[4],
        'vv5' : vv[5],
        'vv6' : vv[6],
        'vv7' : vv[7],
        'vv8' : vv[8],
        'vv9' : vv[9],
        'vw0' : vw[0],
        'vw1' : vw[1],
        'vw2' : vw[2],
        'vw3' : vw[3],
        'vw4' : vw[4],
        'vw5' : vw[5],
        'vw6' : vw[6],
        'vw7' : vw[7],
        'vw8' : vw[8],
        'vw9' : vw[9],
        'gnP0': xxx[0],
        'gnP1': xxx[1],
        'gnP2': xxx[2],
        'gnP3': xxx[3],
        'gnP4': xxx[4],
        'gnP5': xxx[5],
        'gnP6': xxx[6],
        'gnP7': xxx[7],
        'gnP8': xxx[8],
        'gnP9': xxx[9],
        'gnC0': zzz[0],
        'gnC1': zzz[1],
        'gnC2': zzz[2],
        'gnC3': zzz[3],
        'gnC4': zzz[4],
        'gnC5': zzz[5],
        'gnC6': zzz[6],
        'gnC7': zzz[7],
        'gnC8': zzz[8],
        'gnC9': zzz[9]
        }
        

        
        c = {
            'Pstatus': Pstatus,
            'Cstatus': Cstatus,
            'firstname':name,
            'playername' : first,
            'mgrId' :mgrid,
            'data' : data,
            'name': ne,
            'welcome': klattu,
            'tit': z
            }
        
        return HttpResponse(temp.render(c, request)) 
        
    elif v not in i:
        from grid2.models import Grid
        g = Grid.objects.all()
        m = Managers.objects.all()
        aa = g.filter(accessNumber = authcode)
        if any(aa)==False:
            msg = "We don't have the code '"+ authcode +"' you entered on record. "
            msg = msg + "Please, contact your Manager Sponser. Or, try another Code."
            temp = loader.get_template('Login.html')
            message = {'msg':msg, 'tit':'Player Login', 'flag':'pw'}
            return HttpResponse(temp.render(message, request)) 
        else:

        
            #if request.method == 'POST':
            temp = loader.get_template('clientSignUp.html')
            a = 'Player Sign-Up'
            c = {
               
                'tit': a
                 
                 }
            return HttpResponse(temp.render(c, request))        
    
        
def Ram(request):
     
    if request.method == 'POST':
        from player.models import Players
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        street = request.POST.get('street') 
        city = request.POST.get('city')
        zipcode = request.POST.get('zip')
        state = request.POST.get('state')
        country = request.POST.get('country')
        username = request.POST.get('userName')
        email = request.POST.get('email')
        p = Players.objects.create(FirstName = firstname, LastName = lastname, Street = street,\
        City = city, ZipCode = zipcode, State = state, Country = country, UsrName = username, \
        Email = email)
        p.save()
        a = ''
        c = {
             'title' : a
             }
    temp = loader.get_template('login.html')
    return HttpResponse(temp.render(c, request))        
                           
def Gull(request):
    if request.method == 'POST':
        from grid2.models import Grid
        one = request.POST.get('a1').value
        two = request.POST.get('a2').value
        three = request.POST.get('a3').value
        four = request.POST.get('a4').value
        five = request.POST.get('a5').value
        six = request.POST.get('a6').value
        seven = request.POST.get('a7'.value)
        eight = request.POST.get('a8').value
        nine = request.POST.get('a9'.value)
        ten = request.POST.get('a10'.value)
        eleven = request.POST.get('a11'.value)
        twelve = request.POST.get('a12'.value)
        thirteen = request.POST.get('a13'.value)
        fourteen = request.POST.get('a14').value
        fifteen = request.POST.get('a15').value
        sixteen = request.POST.get('a16'.value)
        seventeen = request.POST.get('a17'.value)
        eighteen = request.POST.get('a18'.value)
        nineteen = request.POST.get('a19').value
        twenty = request.POST.get('a20'.value)
        twentyOne = request.POST.get('a21'.value)
        twentyTwo = request.POST.get('a22'.value)
        twentyThree = request.POST.get('a23'.value)
        twentyFour = request.POST.get('a24'.value)
        twentyFive = request.POST.get('a25'.value)
        p = Grid.objects.create(name1 = one, name2 = two, name3 = three, name4 = four, name5 = five, name6 = six, name7 = seven, name8 = eight, name9 = nine, name10 = ten, \
        name11 = eleven, name12 = twelve, name13 = thirteen, name14 = fourteen, name15 = fifteen, name16 = sixteen, name17 = seventeen, name18 = eighteen, name19 = nineteen, \
        name20 = twenty, name21 = twentyOne, name22 = twentyTwo, name23 = twentyThree, name24 = twentyFour, name25 = twentyFive)
        p.save() 

def ferret2(i, ac):
    #ACCEPTS MGR # AND AUTH CODE filters Grid db to instances of that manager's active grids.CALLS SKUNK.RETURNS ACTIVE GRIDS('10' GRIDS)AND GRIDNOS TUPLES(ACTIVE COLLEGE AND PRO GRIDS)
    from django.template.context_processors import csrf
    from grid2.models import Grid
    g = Grid.objects.all()
    kk = g.filter(accessNumber = ac)
    w = kk.filter(managerNumber = i)
    y = w.filter(active = '10')
    gp, gc = skunk(y)
    h = (y, gp, gc) 
    return h

# ACCEPTS MGR'S ACTIVE GRIDS('10'GRIDS) AND RETURNS COL AND PRO LISTS OF GRIDNUMS.
def skunk(ag):
    gridNumsP = []
    gridNumsC = []
    grids = ag
    j = len(grids)
    for k in range(0, j):
        num = grids[k].id
        typ = grids[k].gameType
        if typ == 'p':
            gridNumsP.append(num)
        else:
            gridNumsC.append(num)
     
    return gridNumsP, gridNumsC


#UPDATES A MANAGERS ACTIVE GRID'S STATUS TO DB
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
                pass 
            if gdx == 10:
                gdx = gdx + 20
                gd.active = str(gdx) 
                gd.save()
        else:
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

#EVALUATES MGR EMAIL LIST FOR PLAYER SIGN IN WHEN MGR SIGNS IN AS PLAYER TO ACCESS ARCHIVE
def getMgrMail():
    from manager.models import Managers 
    m = Managers.objects.all()
    uu = []
    #evaluate manager email. uu = all manager's email
    for jj in range(0, len(m)):
        oo = m[jj].Email
        uu.append(oo)
    ii =[]
    for tt in uu:
        ee = tt.lower() 
        ii.append(ee)
    return ii

def Dash(request):
    from grid2.models import Grid
    from grid2.models import Terms
    from manager.models import Managers
    from grid2.views import expdaytest

    ne = request.session['UsrName']
    a = ""

    c ={'title': a,
        'name' : ne
        }
    


    temp = loader.get_template('Dashboard2.html')
    return HttpResponse(temp.render(c,request))  


def Lemur(request):
   ## From Grid page to Games Available page  
    from django.shortcuts import render
    from django.template import Template
    from django.template import loader
    from django.http import HttpResponse
    from manager.models import Managers
    from django.template.context_processors import csrf
    from django.template import RequestContext 
    from player.models import Players
    from grid2.models import Grid
    g = Grid.objects.all()
    from manager.models import Managers
    m = Managers.objects.all()
    from player.models import Players
    p = Players.objects.all()
    from grid2.views import expdaytest
    from grid2.views import openStatusTest
    if 'UserName' not in request.session:
        return
    player = request.session['UserName']
    gamnum = request.POST.get('gameNum1')
    person = p.filter(UsrName = player)
    game = g.filter(id = gamnum)
    auth = game[0].accessNumber
    mgrname = game[0].managerName
   
    email = person[0].Email
    authcode = auth
    email = email
    u = []
    bb = 0
   
    #evaluate player email and authcode. u = all player's email
    for j in range(0, len(p)):
        o = p[j].Email
        u.append(o)
    i =[]
    ii = []
    iii = []
    for t in u:
        e = t.lower() 
        i.append(e)
    ii = getMgrMail()
    iii = i + ii
    v = email.lower()
    #if email is valid but now checking only the player List("i")
    if v in i:         
        temp = loader.get_template('Menus.html')
        from grid2.models import Grid
        from manager.models import Managers
        from grid2.views import Catclone, ferret, weasel

       

##       OBTAIN MANAGER ID
        g = Grid.objects.all()
        m = Managers.objects.all()
        aa = g.filter(accessNumber = authcode)
        name = aa[0].managerName
        mgr = m.filter(UsrName = name)
        mgrid = mgr[0].id
        from grid2.views import expdaytest
        update(mgrid)
##       OBTAIN PLAYER NAME 
##        u = []
##        for j in range(0, len(p)):
##            o = p[j].Email
##            u.append(o)
##        i =[]
        v = email.lower()
        
        for t in i:
##            e = t.lower() 
##            i.append(e)            
            if v == t:
                for y in range(0, len(p)):
                    a1 = p[y].Email
                    b1 = a1
                    c1 = b1.lower()
                    if v == c1: 
            
                        plaer = p.filter(Email = b1 )
                        first = plaer[0].UsrName
                       
                       
                break
        for t in ii:
            if v == t:
                firstname = name
             
        w = len(p) + len(m)
        
        
##      FILTER GRID GET PRO AND COL GAMES AND LEN ACTIVE GAMES
##      OBTAIN GRIDNUMS LISTS.(IN JK TUPLE JK[1] & JK[2] FROM SKUNK)
        jk = ferret2(mgrid, authcode)
        k = jk[0]
        gridNumsP = jk[1]
        gridNumsC = jk[2]


        Pstatus = {}
        Cstatus = {}

        if gridNumsP is not "":
            step = 0
            for gamep in gridNumsP:
                statusP = openStatusTest(gamep)
                Pstatus[step] = statusP
                step = step + 1
        if gridNumsC is not "":
            step2 = 0
            for gamec in gridNumsC:
                statusC = openStatusTest(gamec)
                Cstatus[step2] = statusC
                step2 = step2 + 1

                
        xxx = []
        zzz = []
        
##      CREATING LISTS OF GRID NUMBERS TO TRANSFER TO TEMPLATE TEXTS
##      FOR LATER POSTING TO FIND GRIDS FOR PLAYERS VIA 'VIEW' BUTTONS
        for items in range(0, 10):
             xxx.append("")
             zzz.append("")
        for items in range(0, len(gridNumsP)):
             xxx[items]=(gridNumsP[items])
        for items in range(0, len(gridNumsC)):
             zzz[items]=(gridNumsC[items])
          
             
        # k is active games, b is pro list, cc is college list
        
        j = len(k)
        ik = mgrid
        z = g.filter(managerNumber = ik)
        kk = z.filter(accessNumber = authcode)
##        mbefore = kk.filter(active = '10')
        for mt in kk:
##        for mt in mbefore:
            gnum = mt.id
            exx = expdaytest(gnum, 2)
            if exx == "expired":
                kk = kk.exclude(id = gnum)
##                mbefore = mbefore.exclude(id = gnum)
#       m = mbefore
        m = kk 
        
        mm = m.filter(gameType = 'p')
        c = m.filter(gameType = 'c')
        t = []
        vv = []
        n = []
        vw = []
        b = []
        cc = []
        ccc = 0
        bbb = 0
        gg = "display:none"
        
        for s in range(0, 20):
            a = {}    
            a = weasel(mgrid, s, bbb, authcode)
            
            if ccc < len(c): 
              
                cc.append(a)
                ccc = ccc + 1
                
            elif ccc >= len(c) and ccc < j:
                b.append(a)        
                ccc = ccc + 1
                
            
                  
            else:
                for ff in range(0, 10):
                     t.append("")
                     n.append("")
                     vv.append("background-color:green")
                     vw.append("background-color:green")
                     
                for zz in range(0, 10 - len(c)):
                    r = len(c) + zz
                    cc.append({'homec': " ", 'visitc':" "})
##                    t[r] = gg
##                    vv[r] = gg
                    n[r] = gg
                    vw[r] = gg
                    
                for xx in range(len(mm), 10):
                    b.append({'homes': " ", 'visit':" "})
                    t[xx] = gg
                    vv[xx] = gg
        klattu = 'WELCOME'        
        ne = request.session['UserName']
            
        data = {   
        'result0' : b[0],
        'result1' : b[1],
        'result2' : b[2],
        'result3' : b[3],
        'result4' : b[4],
        'result5' : b[5],
        'result6' : b[6],
        'result7' : b[7],
        'result8' : b[8],
        'result9' : b[9],
        'result10' : cc[0],
        'result11' : cc[1],
        'result12' : cc[2],
        'result13' : cc[3],
        'result14' : cc[4],
        'result15' : cc[5],
        'result16' : cc[6],
        'result17' : cc[7],
        'result18' : cc[8],
        'result19' : cc[9],
        't0' : t[0],
        't1' : t[1],
        't2' : t[2],
        't3' : t[3],
        't4' : t[4],
        't5' : t[5],
        't6' : t[6],
        't7' : t[7],
        't8' : t[8],
        't9' : t[9],
        'n0' : n[0],
        'n1' : n[1],
        'n2' : n[2],
        'n3' : n[3],
        'n4' : n[4],
        'n5' : n[5],
        'n6' : n[6],
        'n7' : n[7],
        'n8' : n[8],
        'n9' : n[9],
        'vv0' : vv[0],
        'vv1' : vv[1],
        'vv2' : vv[2],
        'vv3' : vv[3],
        'vv4' : vv[4],
        'vv5' : vv[5],
        'vv6' : vv[6],
        'vv7' : vv[7],
        'vv8' : vv[8],
        'vv9' : vv[9],
        'vw0' : vw[0],
        'vw1' : vw[1],
        'vw2' : vw[2],
        'vw3' : vw[3],
        'vw4' : vw[4],
        'vw5' : vw[5],
        'vw6' : vw[6],
        'vw7' : vw[7],
        'vw8' : vw[8],
        'vw9' : vw[9],
        'gnP0': xxx[0],
        'gnP1': xxx[1],
        'gnP2': xxx[2],
        'gnP3': xxx[3],
        'gnP4': xxx[4],
        'gnP5': xxx[5],
        'gnP6': xxx[6],
        'gnP7': xxx[7],
        'gnP8': xxx[8],
        'gnP9': xxx[9],
        'gnC0': zzz[0],
        'gnC1': zzz[1],
        'gnC2': zzz[2],
        'gnC3': zzz[3],
        'gnC4': zzz[4],
        'gnC5': zzz[5],
        'gnC6': zzz[6],
        'gnC7': zzz[7],
        'gnC8': zzz[8],
        'gnC9': zzz[9]
        
        }
        z = 'Your Available Games'
        c = {
            'name' : ne,
            'welcome' : klattu,
            'firstname':name,
            'playername' : first,
            'mgrId' :mgrid,
            'title': z,
            'data' : data,
            'Pstatus': Pstatus,
            'Cstatus': Cstatus
            }
        #dipshit = asshole
        return HttpResponse(temp.render(c, request)) 
        
            
    #if request.method == 'POST':
    temp = loader.get_template('clientSignUp.html')
    a = 'Player Sign-Up'
    c = {
       
        'title': a,
         
         }
    return HttpResponse(temp.render(c, request))         



    
def login(request, player, auth):
    from player.models import Players
    from grid2.models import Grid
    u = player
    a = auth
    request.session['UsrName'] = u
    request.session['Ackcode'] = a
    request.session['UsrType'] = 'p'
    msg = "You are logged in as " + u
    
        
          
    return msg



def logout_view(request):
    from django.contrib.auth import logout 
    logout(request)
    # Redirect to a success page.
    temp = loader.get_template('Some.html') 
    a = '25 SQUARES FOOTBALL'
    c = {

         'tit': a

         }
    return HttpResponse(temp.render(c, request))



          
def Tomenus(request):
    import time 
    from grid2.models import Grid
    from manager.models import Managers
    from player.models import Players
    from django.views.decorators.csrf import csrf_protect 
    from django.shortcuts import render
    from django.template import Template
    from django.template import loader
    from django.http import HttpResponse
    from manager.models import Managers
    from django.template.context_processors import csrf
    from django.template import RequestContext 
    from player.models import Players
    from grid2.views import expdaytest
    from grid2.views import openStatusTest
    m = Managers.objects.all()
    p = Players.objects.all()
    g = Grid.objects.all()
    name = request.session['UserName']
    n = p.filter(UsrName = name)
    eml = n[0].Email
    pw = request.session['Ackcode']
    c ={}
    c.update(csrf(request))
    authcode = pw 
    email = eml
    p = Players.objects.all()
    u = []
    bb = 0
    #evaluate player email and authcode. u = all player's email
    for j in range(0, len(p)):
        o = p[j].Email
        u.append(o)
    i =[]
    ii = []
    iii = []
    for t in u:
        e = t.lower() 
        i.append(e)
    ii = getMgrMail()
    iii = i + ii
    v = email.lower()
    #if email is valid but now checking only the player List("i")
   
    
    if v in i:         
        temp = loader.get_template('Menus.html')
        from grid2.models import Grid
        from manager.models import Managers
        from grid2.views import Catclone, ferret, weasel
##        r = Catclone(request)
       

##       OBTAIN MANAGER ID
        g = Grid.objects.all()
        m = Managers.objects.all()
        aa = g.filter(accessNumber = authcode)
        if any(aa) == False:
            msg = "We don't have the code[" + authcode + "]you entered on record. "
            msg = msg + "Please, contact your Manager Sponser. Or, try another Code."
            temp = loader.get_template('Login.html')
            message = {'msg':msg, 'title' : 'Player Login'}
            return HttpResponse(temp.render(message, request))
        name = aa[0].managerName
        mgr = m.filter(UsrName = name)
        mgrid = mgr[0].id
        from grid2.views import expdaytest
        update(mgrid)
##       OBTAIN PLAYER NAME 
##        u = []
##        for j in range(0, len(p)):
##            o = p[j].Email
##            u.append(o)
##        i =[]
        v = email.lower()
        
        for t in i:
##            e = t.lower() 
##            i.append(e)            
            if v == t:
                for y in range(0, len(p)):
                    a1 = p[y].Email
                    b1 = a1
                    c1 = b1.lower()
                    if v == c1: 
            
                        plaer = p.filter(Email = b1 )
                        first = plaer[0].UsrName
                        d = login(request, first, authcode)
                        
                break
        for t in ii:
            if v == t:
                firstname = name
             
        w = len(p) + len(m)
        
        
##      FILTER GRID GET PRO AND COL GAMES AND LEN ACTIVE GAMES
##      OBTAIN GRIDNUMS LISTS.(IN JK TUPLE JK[1] & JK[2] FROM SKUNK)
        jk = ferret2(mgrid, authcode)
        k = jk[0]
        gridNumsP = jk[1]
        gridNumsC = jk[2]

        Pstatus = {}
        Cstatus = {}

        if gridNumsP is not "":
            step = 0
            for gamep in gridNumsP:
                statusP = openStatusTest(gamep)
                Pstatus[step] = statusP
                step = step + 1
        if gridNumsC is not "":
            step2 = 0
            for gamec in gridNumsC:
                statusC = openStatusTest(gamec)
                Cstatus[step2] = statusC
                step2 = step2 + 1
        
        xxx = []
        zzz = []
        
##      CREATING LISTS OF GRID NUMBERS TO TRANSFER TO TEMPLATE TEXTS
##      FOR LATER POSTING TO FIND GRIDS FOR PLAYERS VIA 'VIEW' BUTTONS
        for items in range(0, 10):
             xxx.append("")
             zzz.append("")
        for items in range(0, len(gridNumsP)):
             xxx[items]=(gridNumsP[items])
        for items in range(0, len(gridNumsC)):
             zzz[items]=(gridNumsC[items])
          
             
        # k is active games, b is pro list, cc is college list
        
        j = len(k)
        ik = mgrid
        z = g.filter(managerNumber = ik)
        kk = z.filter(accessNumber = authcode)
##        mbefore = kk.filter(active = '10')
        for mt in kk:
##        for mt in mbefore:
            gnum = mt.id
            exx = expdaytest(gnum, 2)
            if exx == "expired":
                kk = kk.exclude(id = gnum)
##                mbefore = mbefore.exclude(id = gnum)
#       m = mbefore
        m = kk 
       
        mm = m.filter(gameType = 'p')
        c = m.filter(gameType = 'c')
        t = []
        vv = []
        n = []
        vw = []
        b = []
        cc = []
        ccc = 0
        bbb = 0
        gg = "display:none"
        
        for s in range(0, 20):
            a = {}    
            a = weasel(mgrid, s, bbb, authcode)
            
            if ccc < len(c): 
              
                cc.append(a)
                ccc = ccc + 1
                
            elif ccc >= len(c) and ccc < j:
                b.append(a)        
                ccc = ccc + 1
                
            
                  
            else:
                for ff in range(0, 10):
                     t.append("")
                     n.append("")
                     vv.append("background-color:green")
                     vw.append("background-color:green")
                     
                for zz in range(0, 10 - len(c)):
                    r = len(c) + zz
                    cc.append({'homec': " ", 'visitc':" "})
##                    t[r] = gg
##                    vv[r] = gg
                    n[r] = gg
                    vw[r] = gg
                    
                for xx in range(len(mm), 10):
                    b.append({'homes': " ", 'visit':" "})
                    t[xx] = gg
                    vv[xx] = gg
        z = 'Your Available Games'
        klattu = 'WELCOME'        
        ne = request.session['UsrName']    
        data = {  
        'result0' : b[0],
        'result1' : b[1],
        'result2' : b[2],
        'result3' : b[3],
        'result4' : b[4],
        'result5' : b[5],
        'result6' : b[6],
        'result7' : b[7],
        'result8' : b[8],
        'result9' : b[9],
        'result10' : cc[0],
        'result11' : cc[1],
        'result12' : cc[2],
        'result13' : cc[3],
        'result14' : cc[4],
        'result15' : cc[5],
        'result16' : cc[6],
        'result17' : cc[7],
        'result18' : cc[8],
        'result19' : cc[9],
        't0' : t[0],
        't1' : t[1],
        't2' : t[2],
        't3' : t[3],
        't4' : t[4],
        't5' : t[5],
        't6' : t[6],
        't7' : t[7],
        't8' : t[8],
        't9' : t[9],
        'n0' : n[0],
        'n1' : n[1],
        'n2' : n[2],
        'n3' : n[3],
        'n4' : n[4],
        'n5' : n[5],
        'n6' : n[6],
        'n7' : n[7],
        'n8' : n[8],
        'n9' : n[9],
        'vv0' : vv[0],
        'vv1' : vv[1],
        'vv2' : vv[2],
        'vv3' : vv[3],
        'vv4' : vv[4],
        'vv5' : vv[5],
        'vv6' : vv[6],
        'vv7' : vv[7],
        'vv8' : vv[8],
        'vv9' : vv[9],
        'vw0' : vw[0],
        'vw1' : vw[1],
        'vw2' : vw[2],
        'vw3' : vw[3],
        'vw4' : vw[4],
        'vw5' : vw[5],
        'vw6' : vw[6],
        'vw7' : vw[7],
        'vw8' : vw[8],
        'vw9' : vw[9],
        'gnP0': xxx[0],
        'gnP1': xxx[1],
        'gnP2': xxx[2],
        'gnP3': xxx[3],
        'gnP4': xxx[4],
        'gnP5': xxx[5],
        'gnP6': xxx[6],
        'gnP7': xxx[7],
        'gnP8': xxx[8],
        'gnP9': xxx[9],
        'gnC0': zzz[0],
        'gnC1': zzz[1],
        'gnC2': zzz[2],
        'gnC3': zzz[3],
        'gnC4': zzz[4],
        'gnC5': zzz[5],
        'gnC6': zzz[6],
        'gnC7': zzz[7],
        'gnC8': zzz[8],
        'gnC9': zzz[9],
        }
        
        c = {
            'welcome' : klattu,
            'name' : ne,
            'firstname':name,
            'playername' : first,
            'mgrId' :mgrid,
            'data' : data,
            'tit': z,
            'Pstatus': Pstatus,
            'Cstatus': Cstatus
            }
        
        return HttpResponse(temp.render(c, request)) 
   #if request.method == 'POST':
    temp = loader.get_template('clientSignUp.html')
    a = 'Player Sign-Up'
    c = {
       
        'title': a,
         
         }
    return HttpResponse(temp.render(c, request))         	

    	
