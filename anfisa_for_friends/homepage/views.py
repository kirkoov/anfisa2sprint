from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        # 'title', 'id', 'description').filter(is_on_main=True)
        'title', 'id', 'description').exclude(is_published=False)
    ## Условия для конкретной даты:
    # Post.objects.filter(pub_date__date=datetime.date(1890, 1, 1))
    # # Ранее первого января 1895 года:
    # Post.objects.filter(pub_date__date__lt=datetime.date(1895, 1, 1))
    # # В конкретный год:
    # Post.objects.filter(pub_date__year=1890)
    # # В любой год с января по июнь включительно:
    # Post.objects.filter(pub_date__month__gte=6)
    # # В первый квартал любого года:
    # Post.objects.filter(pub_date__quarter=1)
    context = {'ice_cream_list': ice_cream_list}
    return render(request, template, context)
