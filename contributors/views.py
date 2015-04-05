from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from contributors.models import Article, Contributor, Email, Contact, HaveYouSeen, ThisMonthInEvolution
from contributors.forms import EmailForm, ContactForm


def main(request):
    recent_article_list=Article.objects.order_by('-pub_date')[1:5]
    newest_article_list=Article.objects.order_by('-pub_date')[0]
    newest_monthly=ThisMonthInEvolution.objects.order_by('-dateadded')[0]
    recent_seen_list=HaveYouSeen.objects.order_by('-dateadded')[:10]
    context={'recent_article_list': recent_article_list, "newest_article_list": newest_article_list,'recent_seen_list':recent_seen_list, 'newest_monthly':newest_monthly}
    return render(request, 'contributors/main.html', context)

def archive(request):
    article_list=Article.objects.order_by('-pub_date')
    context={'article_list': article_list,}
    return render(request, 'contributors/archive.html', context)

def mailinglist(request):
    return HttpResponse("This is my mailing list page")

def contributors(request):
    contributor_list=Contributor.objects.order_by('rank')
    context={'contributor_list': contributor_list,}
    print context
    return render(request, 'contributors/contributors.html', context)

def contributor(request, contributor_id):
    current_contributor=Contributor.objects.get(urlstring=contributor_id)
    contributor_articles=Article.objects.all().filter(contrib_id=current_contributor.id).order_by('-pub_date')
    context={ 'current_contributor': current_contributor, 'contributor_articles': contributor_articles,}
    print context
    return render(request, 'contributors/contributor.html', context)

def article(request, article_id):
    current_article=Article.objects.get(id=article_id)
    current_contributor=Contributor.objects.get(name=current_article.contrib)
    all_recent_article_list=Article.objects.order_by('-pub_date')[:4]
    for article in all_recent_article_list:
        if article.id == current_article.id: 
            all_recent_article_list=Article.objects.order_by('-pub_date')[4:8]
    context={'current_article': current_article, 'all_recent_article_list': all_recent_article_list, 'current_contributor': current_contributor, }
    return render(request, 'contributors/articles.html', context)

def about(request):
    recent_article_list=Article.objects.order_by('-pub_date')[:5]
    context={'recent_article_list': recent_article_list,}
    return render(request, 'contributors/about.html', context)

def submitted(request):
    return HttpResponse("Thank you for submitting your email.")

def mailinglist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newemail=form.cleaned_data['your_email']
            newentry=Email(email=newemail)
            newentry.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/submitted/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return render(request, 'contributors/contact.html', {'form': form})


def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newmessage=form.cleaned_data['your_feedback']
            newentry=Contact(feedback=newmessage)
            newentry.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/submitted/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contributors/contact.html', {'form': form})
