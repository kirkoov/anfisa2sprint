# from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # ice_cream_list = IceCream.objects.all()  # BAD if dot notaion is in the
    # templates that help render the view.

    # Mind you, a list of dicts is returned via the values():
    # in the template, use the {{ ice_cream.category__title }} notation vs the
    # dot one.
    # ice_cream_list = IceCream.objects.values(
    # 'id', 'title', 'category__title')  # I.e. selected fields
    # VS all fields of the related model
    # ice_cream_list = IceCream.objects.select_related('category')

    ice_cream_list = IceCream.objects.values(
        'id',
        'title',
        'price',
        'description'
    ).filter(
        is_published=True,
        is_on_main=True,
        category__is_published=True
    )

    # ice_cream_list = IceCream.objects.values(
    #         'id', 'title', 'description'
    #     ).filter(
    #         is_published=True, is_on_main=True
    #     ).order_by('title')[0:3]

    # Q(is_published=True)
    # & (Q(is_on_main=True) | Q(title__contains='пломбир'))
    # 'title', 'id', 'description').filter(
    # is_published=True, is_on_main=True)
    # 'title', 'id', 'description').exclude(is_published=False)

    # categories = Category.objects.values(
    #     'id', 'output_order', 'title').order_by(
    #     'output_order', 'title')

    # Условия для конкретной даты:
    # Post.objects.filter(pub_date__date=datetime.date(1890, 1, 1))
    # # Ранее первого января 1895 года:
    # Post.objects.filter(pub_date__date__lt=datetime.date(1895, 1, 1))
    # # В конкретный год:
    # Post.objects.filter(pub_date__year=1890)
    # # В любой год с января по июнь включительно:
    # Post.objects.filter(pub_date__month__gte=6)
    # # В первый квартал любого года:
    # Post.objects.filter(pub_date__quarter=1)
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
