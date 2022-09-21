from django.urls import path
from . import views

urlpatterns = [
    # restaurant urls
    path('', views.show_restaurants),
    path('new/', views.new_restaurant),
    path('edit/<int:restaurant_id>', views.edit_restaurant),
    path('delete/<int:restaurant_id>', views.delete_restaurant),

    # menu itens urls
    path('menus/<int:restaurant_id>', views.show_menu_itens, name="menu"),
    path('menus/<int:restaurant_id>/new/', views.new_menu_item, name="new"),
    path('menus/<int:restaurant_id>/edit/<int:item_id>/', views.edit_menu_item, name="edit"),
    path('menus/<int:restaurant_id>/delete/<int:item_id>/', views.delete_menu_item, name="delete"),
]