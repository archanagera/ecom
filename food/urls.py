from . import views
from django.urls import include,path
app_name='food'
urlpatterns =[
    #as class_view
    #path('',views.index,name='index'),
    path('',views.IndexClassView.as_view(),name='index'),
    #as class_view
    # path('<int:item_id>/',views.detail,name='detail'),
      path('<int:pk>/',views.DetailClassView.as_view(),name='detail'),
    #userform
    path('form',views.userform,name='userform'),
    #userform
    path('form27',views.userform27,name='userform27'),
    #addname
    path('addname',views.get_name,name='get_name'),
    path('addItem',views.add_item,name='add_item'),
    path('addItem1',views.add_item_model,name='add_item_model'),
    path('updateItem/<int:item_id>',views.update_item,name='update_item'),

] 