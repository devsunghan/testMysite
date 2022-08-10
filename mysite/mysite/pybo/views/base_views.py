from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from ..models import Question
from math import ceil

def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    val = request.GET.get('val', '') # 구분자
    # 조회`
    question_list = Question.objects.order_by('-create_date')

    if val == 1:
        question_list = question_list.filter(
            Q(author__username__icontains=val)
        ).distinct()


    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()


    # 페이징처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw}

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def tag_page(request):
    """
    태그별 표시
    """
    question_list = Question.objects.order_by('-create_date')
    nomi_question_list = question_list.filter(
        Q(tag__icontains="노미카이")  # 태그 검색
    ).distinct()[:10]

    worry_question_list = question_list.filter(
        Q(tag__icontains="고민 게시판")
    ).distinct()[:10]

    deal_question_list = question_list.filter(
        Q(tag__icontains="중고거래")
    ).distinct()[:10]

    advice_question_list = question_list.filter(
        Q(tag__icontains="일본생활 조언")
    ).distinct()[:10]



    context = {
        "nomi_question_list": nomi_question_list,
        "worry_question_list": worry_question_list,
        "deal_question_list": deal_question_list,
        "advice_question_list": advice_question_list

       }
    return render(request, 'pybo/test.html', context)

def nomi_page(request):
    """
    노미카이 채널
    """
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date')
    nomi_question_list = question_list.filter(
        Q(tag__icontains="노미카이")  # 태그 검색
    ).distinct()

    paginator = Paginator(nomi_question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page}

    return render(request, 'pybo/question_list.html', context)

def worry_page(request):
    """
    고민 게시판 채널
    """
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date')
    worry_question_list = question_list.filter(
        Q(tag__icontains="고민 게시판")  # 태그 검색
    ).distinct()

    paginator = Paginator(worry_question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page}

    return render(request, 'pybo/question_list.html', context)

def deal_page(request):
    """
    중고거래 채널
    """
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date')
    deal_question_list = question_list.filter(
        Q(tag__icontains="중고거래")  # 태그 검색
    ).distinct()

    paginator = Paginator(deal_question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page}

    return render(request, 'pybo/question_list.html', context)

def advice_page(request):
    """
    일본생활 조언 채널
    """
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date')
    advice_question_list = question_list.filter(
        Q(tag__icontains="일본생활 조언")  # 태그 검색
    ).distinct()

    paginator = Paginator(advice_question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page}

    return render(request, 'pybo/question_list.html', context)