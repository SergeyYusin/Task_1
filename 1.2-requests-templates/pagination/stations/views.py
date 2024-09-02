from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def read_csv():
    csv_list = []

    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] != 'Name' or row[4] != 'Street' or row[6] != 'District':
                csv_list.append({
                    'Name': row[1],
                    'Street': row[4],
                    'District': row[6]
                })

    return csv_list


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    csv_list = read_csv()

    p_name = Paginator(csv_list, 10)
    current_page = request.GET.get('page', 1)
    page = p_name.get_page(current_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }

    return render(request, 'stations/index.html', context)


