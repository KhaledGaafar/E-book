from django.urls import path,include
from .views import( home,bookShowGenericView,bookDeleteGenericView,CreatebookView,borrowbooks,showbook,bookUpdateGenericView,users,
                  search_user,showbookUser)

urlpatterns = [
    path('home/',home,name='books-home'),
    path('<int:id>/borrow',borrowbooks,name='borrow'),
    path('<int:pk>',bookShowGenericView.as_view(),name='show-books'),
    path('<int:pk>/delet',bookDeleteGenericView.as_view(), name='delete'),
    path('create/',CreatebookView.as_view(),name='create'),
    path('show/',showbook,name='show-borrow'),
    path('<int:pk>/update',bookUpdateGenericView.as_view(),name="update"),
    path('uses/',users,name='users'),
    path('search/',search_user,name='search'),
    path('showuser/',showbookUser,name='show-borrowuser'),
    
]