from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils import timezone

from products.models import Product
from questions.form import QuestionForm
from questions.models import Question


@login_required(login_url='accounts:login')
def create(request, product_id):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.content_type = ContentType.objects.get(app_label='products', model='product')
            question.user = request.user
            question.reg_date = timezone.now()
            question.object_id = product_id
            question.save()
            return redirect('products:detail', product_id)
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'questions/question_form.html', context)


@login_required(login_url='accounts:login')
def modify(request, product_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.user:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('products:detail', product_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modifyDate = timezone.now()
            question.save()
            return redirect('products:detail', product_id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'questions/question_form.html', context)


@login_required(login_url='accounts:login')
def delete(request, product_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.user:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('products:detail', product_id)
    question.delete()
    return redirect('products:detail', product_id)
