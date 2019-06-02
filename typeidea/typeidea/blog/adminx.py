import xadmin
from xadmin.layout import Row,Fieldset,Container
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from .models import Post,Category,Tag
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin





class PostInline:#StackedInlin样式不同
    form_layout = (
        Container(
            Row("title","desc")
        )
    )
    extra = 1 #控制额外多几个
    model = Post


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name','status','is_nav','created_time','owner','post_count')
    fields = ('name','status','is_nav')
    inlines = [PostInline,]

    #通过类继承可以实现项目代码的功能，减少代码数量，清晰代码结构
    """
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request,obj,form,change)
    """

    def post_count(self,obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name','status','is_nav','created_time','owner')
    fields = ('name','status')
    """
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin,self).save_model(request,obj,form,change)
    """

class CategoryOwnerFilter(RelatedFieldListFilter):
    """
    #自定义过滤器只展示当前用户分类

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset
    """
    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self,field,request,params,model,model_admin,field_path):
        super().__init__(field,request,params,model,model_admin,field_path)
        #重新获取lookup_choices，根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id','name')

manager.register(CategoryOwnerFilter,take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):

    form = PostAdminForm

    list_display = [
        'title','category','status',
        'created_time', 'owner',
        'operator',
    ]

    list_display_links = []

    #过滤器
    #list_filter = ['category','tag']
    #list_filter = [CategoryOwnerFilter]
    list_filter = ['category']
    search_fields = ['title','category__name']
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = False

    #编辑页面
    save_on_top = True
    save_on_bottom = True

    exclude = ('owner',)
    """
    fields = (
        ('category','title'),
        'desc',
        'status',
        'content',
        'tag',
    )
    """
    """
    fieldsets = (
        ('基础配置',{
            'description': '基础配置描述',
            'fields':(
                ('title','category'),
                'status',
            ),
        }),
        ('内容',{
            'fields':(
                'desc',
                'content',
            ),
        }),
        ('额外信息',{
            'classes':('collapse',),
            'fields':('tag',),
        })
    )
    """
    form_layout = (
        Fieldset(
            '基础信息',
            Row("title","category"),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'content',
        )
    )
    #字段竖向展示
    #filter_vertical = ('tags',)

    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            #self.model_admin_url('change',obj.id)
            reverse('xadmin:blog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'


    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request,obj,form,change)

    def get_queryset(self, request):
        qs = super(PostAdmin,self).get_queryset(request)
        return qs.filter(owner=request.user)

    """
    class Media:
        css = {
            'all':("https//cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)
    """
    """
    @property
    def media(self):
        # xadmin 基于Bootstrap，引入会导致页面样式冲突，这里只做演示
        media = super().media
        media.add_js(['https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js'])
        media.add_css({
            'all': ('https//cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css'),
        }),
        return media
    """


@xadmin.sites.register(LogEntry)
class LogEntryAdmin:
    list_display = ['object_repr','object_id','action_flag','user',
                    'change_message']

