from django.urls import path
from books.views import ahome
from books.views import ahome,home,login,alogin,info,abase,viewp,ainfo,aregister,register,viewps,search,edit,update,aedit,aupdate,students,delete,add,bedit,bupdate,burrow,burrowed,returnn,aburrowed,alibrary,library,burrowedd
urlpatterns = [
    path('ahome/<ib>',ahome,name="ahome"),
    path('home/<ib>',home,name="home"),
    path('login',login,name="login"),
    path('alogin',alogin,name="alogin"),
    path("home/<ib>/<pro_info>",info,name="info"),
    path('layouts/abase/<ip>',abase,name="abase"),
    path('viewp/<ic>',viewp,name="viewp"),
    path("ahome/<ib>/<pro_info>",ainfo,name="ainfo"),
    path("aregister",aregister,name="aregister"),
    path("register",register,name="register"),
    path('viewps/<ic>',viewps,name="viewps"),
    path('search/<ib>',search,name="search"),
    path('edit/<ic>',edit,name="edit"),
    path('update/<pro_id>',update,name="update"),
    path('aedit/<ic>',aedit,name="aedit"),
    path('aupdate/<pro_id>',aupdate,name="aupdate"),
    path('students/<ib>',students,name="students"),
    path("delete/<pro_id>/<ib>",delete,name="delete"),
    path('add/<ib>',add,name="add"),
    path('bedit/<pro_id>/<ic>',bedit,name="bedit"),
    path('bupdate/<pro_id>/<ib>',bupdate,name="bupdate"),
    path('burrow/<ib>/<b>',burrow,name="burrow"),
    path('burrowed/<ib>',burrowed,name="burrowed"),
    path('returnn/<ib>/<b>',returnn,name="returnn"),
    path('aburrowed/<ib>',aburrowed,name="aburrowed"),
    path('alibrary/<ib>',alibrary,name="alibrary"),
    path('library/<ib>', library, name="library"),
    path('burrowedd/<ib>',burrowedd,name="burrowedd")

]