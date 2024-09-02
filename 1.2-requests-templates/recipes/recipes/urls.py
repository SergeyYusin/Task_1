"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from calculator.views import calculate_view
urlpatterns = [
    path('<dish_get>/', calculate_view, name='calculate'),

    # Добавьте path('your_view_name/', your_view_function),  # пример: path('add_recipe/', add_recipe),  # замените 'your_view_name' на имя вашей view-функции и 'add_recipe' на название вашего URL-пути.  # вместо add_recipe() укажите в
    # здесь зарегистрируйте вашу view-функцию

]
