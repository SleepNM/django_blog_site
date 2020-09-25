from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,\
                                 CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, UpdateForm, AddCategoryForm, AddCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class AricleDetaliView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            AricleDetaliView,
            self
            ).get_context_data(*args, **kwargs)

        obj = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = obj.total_likes()

        liked = False
        if obj.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    # def form_valid(self, form):
    #     form.instance.author = self.request.user.id
    #     return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'add_category.html'


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


def category_list_view(request):
    cat_menu_list = Category.objects.all()
    return render(
        request,
        'category_list.html',
        {'cat_menu_list': cat_menu_list}
        )


def category_view(request, slug):
    category_posts = Post.objects.filter(
        category=slug.replace('-', ' ')
        ).order_by('-post_date')
    cat_menu = Category.objects.all()
    return render(
        request,
        'categories.html',
        {
            'slug': slug.title().replace("-", " "),
            'category_posts': category_posts,
            'cat_menu': cat_menu
        })


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
