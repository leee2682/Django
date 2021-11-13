from django.contrib.messages.constants import ERROR
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Question, QuestionCount


def index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')     # 페이지
    tp = request.GET.get('tp', '')          # 필터
    kw = request.GET.get('kw', '')          # 검색어
    so = request.GET.get('so', 'recent')    # 정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    elif so == 'view':
        question_list = Question.objects.annotate(num_answer=Count('hits')).order_by('-hits', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # 검색
    if kw:
        if tp == 'content':
            question_list = question_list.filter(
                Q(content__icontains=kw)
            ).distinct()  # 내용
        elif tp == 'subcon':
            question_list = question_list.filter(
                Q(subject__icontains=kw) |
                Q(content__icontains=kw)
            ).distinct()  # 제목 + 내용
        elif tp == 'username':
            question_list = question_list.filter(
                Q(author__username__icontains=kw)
            ).distinct()  # 글쓴이
        else:
            question_list = question_list.filter(
                Q(subject__icontains=kw)
            ).distinct()  # 제목

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'tp': tp, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    ip = get_client_ip(request)
    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()
    if cnt == 0:
        qc = QuestionCount(ip=ip, question=question)
        qc.save()
        if question.hits:
            question.hits += 1
        else:
            question.hits = 1
        question.save()

    # question.hits += 1
    # question.save()
    
    return render(request, 'pybo/question_detail.html', context)