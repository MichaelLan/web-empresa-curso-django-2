class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
