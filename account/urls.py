from django.urls import path
from account import views
urlpatterns=[
    path("register/",views.register_view),
    path("login/",views.login_view),
    path("logout/",views.logout_view),
    path("protect1/",views.protect_view1),
    path("protect2/",views.protect_view2),

]