from datetime import date

from django.core.cache import cache

from django.db.models import Q,F
from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404
from config.models import SideBar
from .models import Post,Category,Tag

from comment.forms import CommentForm
from comment.models import Comment

class CommonViewMixin:
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })
        context.update(Category.get_navs())
        return context

class IndexView(CommonViewMixin,ListView):
    model = Post
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category,pk=category_id)
        context.update({
            'category': category,
        })
        return context

    def get_queryset(self):
        """重写queryset,根据分类过滤"""
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag,pk=tag_id)
        context.update({
            'tag': tag,
        })

        return context

    def get_queryset(self):
        """重写queryset,根据标签过滤"""
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag_id=tag_id)

class PostDetailView(CommonViewMixin,DetailView):
    model = Post
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
    """
    评论模块
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'comment_form': CommentForm,
            'comment_list': Comment.get_by_target(self.request.path)
        })
        return context
    """
    """
    统计用户访问量
    def get(self,request, *args, **kwargs):
        response = super().get(request,*args,**kwargs)
        Post.objects.filter(pk=self.object.id).update(pv=F('pv')+ 1, pu=F('pu')+1)

        #调试用
        from django.db import connection
        print(connection.queries)
        return response
    """
    def get(self,request,*args,**kwargs):
        response = super().get(request,*args,**kwargs)
        self.handle_visited()
        return response

    def handle_visited(self):
        increase_pv = False
        increase_pu = False
        uid = self.request.uid
        pv_key = 'pv:%s:%s' % (uid,self.request.path)
        pu_key = 'pu:%s:%s:%s' % (uid,str(date.today()),self.request.path)
        if not cache.get(pv_key):
            increase_pv = True
            cache.set(pv_key,1,1*60) #1分钟有效

        if not cache.get(pu_key):
            increase_pu = True
            cache.set(pv_key,1,24*60*60) #24小时有效

        if increase_pv and increase_pu:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1,pu=F('pu')+1)
        elif increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1)
        else:
            Post.objects.filter(pk=self.object.id).update(pu=F('pu')+1)


class SearchView(IndexView):
    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'keyword':self.request.GET.get('keyword','')
        })
        return context

    def get_queryset(self):
        querset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return querset
        return querset.filter(Q(title__icontains=keyword) | Q(desc__icontains=
                                                              keyword))


class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)