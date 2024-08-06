from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from web.models import BlogPost
from django.core.files.storage import default_storage
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User 

# Create your views here.


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    #Recupération et modification du queryset pour differencier les articles publiés des non publiés
    def get_queryset(self):
        queryset = super().get_queryset() #recupération du queryset
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


#Creer un article 
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "web/blogpost_create.html"
    fields = ['title', 'content', 'thumbnail']

#Modifier un article
class BlogPostUpdated(UpdateView):
    model = BlogPost
    template_name = "web/blogpost_edit.html"
    fields = ['title', 'slug', 'content', 'thumbnail']


#Détailler un article 
class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"

#Supprimer un article 
class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy('web:home')


#connection au tableau de bord 
# from django.views.generic import View


# class LoginPageView(View):
#     template_name = 'web/blogpost_login.html'
#     form_class = LoginForm

#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request, self.template_name, context={'form': form, 'message': message})
        
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         message = 'Identifiants invalides.'
#         return render(request, self.template_name, context={'form': form, 'message': message})
            




    


