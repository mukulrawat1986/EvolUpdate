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
    contributor_list=Contributor.objects.order_by('name')
    context={'contributor_list': contributor_list,}
    print context
    return render(request, 'contributors/contributors.html', context)

def article(request, article_id):
    current_article=Article.objects.get(id=article_id)
    context={'current_article': current_article }
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
