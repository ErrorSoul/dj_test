#coding:utf-8


from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from blog.models import Post, Comment 
from blog.forms import CommentForm


def posted(request, post_id):
    context_dict = {}
    context = RequestContext(request,{"all_tags":make_tags()})
    pst = get_object_or_404(Post, pk=post_id)
    tgs = pst.get_tags()
    comments = Comment.objects.filter(post=pst)
    context_dict["post"] = pst
    context_dict["comments"] = comments
    context_dict["form"] =  CommentForm()
    return render_to_response('blog/post.html', context_dict, context)


def index(request): 
    context = RequestContext(request, {"all_tags":make_tags()})
    post_list = Post.objects.all()[:10]
    len_comments(post_list)
    return render_to_response('blog/index.html',{"post_list":post_list}, context)

def tag(request, t):
    context_dict = {}
    context = RequestContext(request,{"all_tags":make_tags()})
    posts_with_tag = Post.objects.filter(tags__icontains=t)
    len_comments(posts_with_tag)
    context_dict["tag"] = t
    context_dict["post_list"] = posts_with_tag 
    return render_to_response('blog/tags.html', context_dict, context)


def make_tags():
    posts = Post.objects.all()
    posts = (p.get_tags() for p in posts)
    posts = sum(posts, [])
    tag_list = []
    [tag_list.append(c) for c in posts if c not in tag_list]
    return tag_list

def len_comments(post_list):
    for p in post_list:
        p.len_comments = len(Comment.objects.filter(post=p))
    

def add_comment(request, pk):
    
    post=Post.objects.get(pk=pk)
    if request.method == "POST":
        context = RequestContext(request,{"all_tags":make_tags()})
        comment = Comment(post=post)
        comment = CommentForm(request.POST, instance=comment)
        if comment.is_valid():
            comment.save()
        else:
            form = CommentForm()
            comments = Comment.objects.filter(post=post)
            return render_to_response('blog/post.html',{"post":post,"comments":comments,
                                                        "error":comment.errors, "form":form },
                                      context)
       
            
    return HttpResponseRedirect("/blog/post/%s" % pk)
            
        
