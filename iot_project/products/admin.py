from django.contrib import admin

from products.models import Cheese, Cheese_condition, Cheese_batch


class CheeseAdmin(admin.ModelAdmin):
    list_display = ('name', 'ripening_period',)


class CheeseConditionAdmin(admin.ModelAdmin):
    list_display = ('cheese', 'current_condition', 'previous_condition', 'term_days',)


class CheeseBatchAdmin(admin.ModelAdmin):
    list_display = ('cheese', 'amount', 'chamber_zone', 'datetime',)

    list_filter = ('cheese', 'chamber_zone',)


admin.site.register(Cheese, CheeseAdmin)
admin.site.register(Cheese_condition, CheeseConditionAdmin)
admin.site.register(Cheese_batch, CheeseBatchAdmin)
