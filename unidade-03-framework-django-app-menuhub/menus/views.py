from django.shortcuts import render, redirect

from .models import MenuItem, Restaurant


# Restaurant views.
def show_restaurants(request):
    """show restaurants by name."""
    restaurants = Restaurant.objects.order_by('name')
    context = {'restaurants': restaurants}
    return render(request, "restaurants/show_restaurants.html", context)


def new_restaurant(request):
    """create a new restaurant."""
    if request.method == 'POST':
        form_data = request.POST
        restaurant = Restaurant()
        restaurant.name = form_data.get('name')
        restaurant.save()
        return redirect("/")
    else:
        return render(request, 'restaurants/new_restaurant.html')


def edit_restaurant(request, restaurant_id):
    """edit a restaurant by a id."""
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    if request.method == 'POST':
        form_data = request.POST
        restaurant.name = form_data.get('name')
        restaurant.save()
        return redirect("/")
    else:
        return render(request, 'restaurants/edit_restaurant.html', {'restaurant': restaurant})


def delete_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    if request.method == 'POST':
        restaurant.delete()
        return redirect("/")
    else:
        return render(request, 'restaurants/delete_restaurant.html', {'restaurant': restaurant})


# MenuItem views
def show_menu_itens(request, restaurant_id):
    """show a menus by category for a restaurant"""
    menu_itens = MenuItem.objects.order_by('category')
    context = {'restaurant_id':restaurant_id, 'menu_itens': menu_itens}
    return render(request, "menus/show_menu_itens.html", context)


def new_menu_item(request, restaurant_id):
    """create a new menu item for restaurant"""
    if request.method == 'POST':
        form_data = request.POST
        menu_item = MenuItem()
        menu_item.category = form_data.get('category')
        menu_item.name = form_data.get('name')
        menu_item.description = form_data.get('description')
        menu_item.price = form_data.get('price')
        menu_item.restaurant_id = restaurant_id
        menu_item.save()
        return redirect(f"/menus/{restaurant_id}")
    else:
        return render(request, 'menus/new_menu_item.html', {'restaurant_id': restaurant_id})


def edit_menu_item(request, restaurant_id, item_id):
    """edit a menu item by a id."""
    menu_item = MenuItem.objects.get(pk=item_id)
    if request.method == 'POST':
        form_data = request.POST
        menu_item.category = form_data.get('category')
        menu_item.name = form_data.get('name')
        menu_item.description = form_data.get('description')
        menu_item.price = form_data.get('price')
        menu_item.save()
        return redirect(f"/menus/{restaurant_id}")
    else:
        return render(request, 'menus/edit_menu_item.html', {'menu_item': menu_item})


def delete_menu_item(request, restaurant_id, item_id):
    menu_item = MenuItem.objects.get(pk=item_id)
    if request.method == 'POST':
        menu_item.delete()
        return redirect(f"/menus/{restaurant_id}")
    else:
        return render(request, 'menus/delete_menu_item.html', {'menu_item': menu_item})