from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from app.models import User, Contact, UserProfile, Articles, Like, ContactUs, Comment, News, NewsContent
from app.forms import ContactForm, UserForm, PostArticleForm, CommentForm
from django.views.generic.edit import CreateView
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.utils.timezone import utc
from django.contrib.auth.decorators import login_required
import datetime
import time
import operator

class UserProfileDetailView(DetailView):
    """User Profile in detail view"""
    slug_field = "username"
    template_name= "user_detail.html"
    model = get_user_model()

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        b = UserProfile.objects.get(user=user)
        return b

def landing(request):
    name = 'Foo Bar'
    context = RequestContext(request)
    t = get_template('landing.html')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=True)
            return render_to_response('landing.html', context)
    return render_to_response('landing.html', {'form': form}, context)

def details(request, contact_id=1):
    return render_to_response('disp.html', {'contact': Contact.objects.get \
            (id=contact_id)})

def login(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated():
       return HttpResponseRedirect('/accounts/articles')
    else:
        return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/articles')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request, personal_id=1):
    try:
        return render_to_response('articles.html',
                                    {'full_name': request.user.username,
                                    'reputation':UserProfile.objects.filter(user=request.user).reputation,})
    except:
        return render_to_response('articles.html',
                                    {'full_name': request.user.username,
                                    'location': 'NA'})

def invalid_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/articles')
    else:
        return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('articles.html')

def personal_info(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/index')
    else:
         form = PersonalForm()
    return render_to_response('personal_form.html', {'form': form}, context)

class UserProfileEditView(UpdateView):

    model = UserProfile
    form_class = UserForm
    template_name = 'user_edit.html'

    def get_object(self, queryset=None):
        a = UserProfile.objects.get(user=self.request.user)
        return a

    def form_valid(self, form):
        instance = form.instance
        instance.user = self.request.user
        instance.save()
        return HttpResponseRedirect('/accounts/articles')

def article_view(request):
    model = Articles
    posts = Articles.objects.all()
    score_dict = {}
    rend = []
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    for post in posts:
        diff = post.time_stamp - datetime.datetime.utcnow().replace(tzinfo=utc)
        t = abs((diff.days)) * 24 + diff.seconds/3600
        """ranking"""
        score = (post.votes-1)/((t+2)**1.8)
        post.score = score
        score_dict[post] = [score]

    for w in sorted(score_dict, key=score_dict.get, reverse=True):
        rend.append(w)

    data = {}
    data['posts'] = rend
    data['now'] = now
    if request.user.is_authenticated():
        data['full_name'] = request.user.username
        data['reputation'] = UserProfile.objects.get(user=request.user).reputation

    return render_to_response('articles.html', data, \
            context_instance=RequestContext(request))


@login_required
def post_article_view(request):
    model = Articles
    template_name = 'post_articles.html'
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    p = Articles.objects.filter(uploader=request.user, time_stamp__range=(today_min, today_max))
    if p.count() > 3:
        return HttpResponse("Max post limit for today reached! try posting \
                        tomorrow </br><a href='/accounts/articles/'>home</a>")
    if request.method == 'POST':
        form = PostArticleForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.uploader = request.user
            temp.time_stamp = datetime.datetime.now()
            temp.save()
            return HttpResponseRedirect('/accounts/articles/')
    else:
        form = PostArticleForm()
    return render_to_response(template_name, {'form':form}, \
                                RequestContext(request))

def like_article(request, article_id):
    new_like, created = Like.objects.get_or_create(user=request.user, \
                                                    article_id=article_id)
    if not created:
        pass
    else:
        pass
    a = Articles.objects.get(id=article_id)
    a.votes = a.like_set.all().count()
    rep_user = a.uploader
    if created:
        b = UserProfile.objects.get(user=rep_user)
        b.reputation += 10
        b.save()
    a.save()
    return HttpResponse(a.votes)


@login_required
def add_comment(request, article_id):
    """Add a new comment."""
    template = "comment.html"
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.date = datetime.datetime.now()
            temp.article_id = article_id
            temp.save()
            return HttpResponseRedirect('/accounts/articles/comments/'+str(article_id))
    else:
        form = CommentForm()
    try:
        comments = Comment.objects.filter(article_id=article_id)
        return render_to_response(template, {"form":form, "comments":comments, "article_id":article_id, "full_name":request.user.username},\
                                 RequestContext(request))
    except:
        return render_to_response(template, {"form":form, "article_id":article_id, "full_name": request.user.username}, RequestContext(request))

def recent_comarticles(request):
    template = "recent_comm.html"
    comments = Comment.objects.order_by('date').reverse()
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    return render_to_response(template, {"comments":comments, "now":now}, \
                                RequestContext(request))

def news(request):

    template = "news.html"
    articles = News.objects.all()
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    return render_to_response(template, {'news':articles, 'now':now}, \
                                        RequestContext(request))

def newscontent(request, news_id):

    template = "content.html"
    content = NewsContent.objects.get(id=news_id)
    return HttpResponse(content.content)

def get_submissions(request, slug):

    template = 'submission.html'
    user = User.objects.get(username=str(slug))
    content = Articles.objects.filter(uploader=user)
    return render_to_response(template, {'articles':content, \
                    'full_name':request.user.username}, RequestContext(request))

def get_comments(request, slug):

    template = 'user_comments.html'
    user = User.objects.get(username=str(slug))
    content = Comment.objects.filter(user=user)
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    return render_to_response(template, {'comments':content, \
            'full_name':request.user.username, 'now':now}, RequestContext(request))

def myself(request):

    template = 'myself.html'
    return render_to_response(template, RequestContext(request))
