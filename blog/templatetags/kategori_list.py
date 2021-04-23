from django import template
from blog.models import KategoriModel


register = template.Library()


@register.simple_tag #fonksiyonu kayıt etmek için decorator
def kategori_list():
    kategoriler = KategoriModel.objects.all()
    return kategoriler
