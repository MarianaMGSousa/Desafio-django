from django.contrib import admin
from .models import Usuario, Livro
from django.contrib.admin.filters import SimpleListFilter

# Register your models here.

class CustomFilter(SimpleListFilter):  #filtro do django
    title = "Filtro customizado" #titulo do filtro
    parameter_name = "custom" #qual o parâmetro que vai apareer na url
    def lookups(self, request, model_admin):
        return(
            ("value_01", "Titulo"), #valor passado e valor que aparece
            ("value_02", "Autor"),
        )
    def queryset(self, request, queryset): #classe obrigatoria para filtros customizados, classe que realmente vai fazer os filtros
        if self.value() == "value_01":
            queryset = queryset.order_by("titulo") #definiu uma ordenação
        elif self.value() == "value_02":
            queryset = queryset.order_by("autor")
        return queryset


class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'leitor', 'data_inicio_leitura']
    list_filter = ["titulo", CustomFilter]
    search_fields = ['titulo', 'autor']


admin.site.register(Usuario)
admin.site.register(Livro, LivroAdmin)
