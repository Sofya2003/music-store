from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache
from .models import Blog, Img_for_instrument, Instruments, Subcategory
from .serializers import (
    BlogSerializer,
    Img_for_instrumentSerializer,
    InstrumentsSerializer, SubcategorySerializer,
)
from django.http import HttpResponse
from .tasks import send_email


def home(request):
    send_email.delay()
    return HttpResponse('<h1> отправка сообщения на почту </h1>')


class InstrumentsPagination(PageNumberPagination):
    page_size = 9


class InstrumentsViewSet(viewsets.ModelViewSet):
    serializer_class = InstrumentsSerializer
    pagination_class = InstrumentsPagination

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if 'instruments_key' in cache:
            data = cache.get('instruments_key')
            if not pk:
                print("ИСПОЛЬЗУЕТСЯ КЭШ")
                return data
            return data.filter(pk=pk)
        else:
            instruments = Instruments.objects.all()
            cache.set('instruments_key', instruments, 3600)
            if not pk:
                print("сОЗДАЕТСЯ КЭШ")
                return instruments
            return instruments.filter(pk=pk)
            

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category", "subcategory"]

#     else:
#         products = Product.objects.all()
#         results = [product.to_json() for product in products]
#         cache.set(product, results, timeout=CACHE_TTL)
#         return Response(results, status=status.HTTP_201_CREATED)

class SubCatViewSet(viewsets.ModelViewSet):
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()

    def get_queryset(self):
        sub_id = self.request.query_params.get('id')
        return Subcategory.objects.filter(category_id=sub_id)


class ImagesViewSet(viewsets.ModelViewSet):
    serializer_class = Img_for_instrumentSerializer
    queryset = Img_for_instrument.objects.all()

    def get_queryset(self):
        ins_id = self.request.query_params.get('id')
        return Img_for_instrument.objects.filter(instrument_id=ins_id)


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Blog.objects.all()
        return Blog.objects.filter(pk=pk)