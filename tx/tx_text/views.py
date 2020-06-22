from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from .models import *
from django.core.paginator import Paginator,Page
from haystack.generic_views import SearchView

from django.shortcuts import render
from .models import  FatfCx_xu
from django.http import HttpResponse,JsonResponse
import markdown

from markdown.extensions.toc import TocExtension

from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.utils.text import slugify

# Create your views
def chx(request):
    '''
    前端需要的数据的结构为[分类数据,....]for i in list
    分类数据包含：最新的4个商品[goods,goods,...]，人气最高的3个商品[]，分类对象type
    每个数据中都包含3部分，所以使用字典结构整合成一个数据{'new':,'hot':,'type':}
    '''
    #查询所有的分类对
    #构造结果列表
    glist=[]


    #将最新的4个商品加入结果中
    # dict={}
    # a=88
    # dd=chax.objects.values_list('gclick', flat=True)
    # pp=chax.objects.values('gclick','gunit').first()

    # dict['new'] = chax.objects.all().get(gclick=4)
    # dict['new']=chax.objects.filter(Gunit='500g')
    #将最火的3个商品加入结果中
    # dict['hot']=chax.objects.all().order_by('-gclick')[0:2]
    # dict['title']=chax.objects.all()
    #向列表中加入字典元素
    # glist.append(dict)
    # print(glist)
    #参数isCart的作用：在base.html当中进行判断，显示顶部是否含有购物车
    # context={'glist':dd}
    context={'bglx':['MER','MER+FUR'],'jy':['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10'],'cjzb':['Criterion'+' '+'1.6','Criterion 1.4',
                                                                                                        'Criterion'+'1.8',\
 'Criterion'+'1.11',\
 'Criterion'+'1.5',\
 'Criterion'+'1.2',\
 'Criterion'+'1.12',\
 'Criterion'+'1.3',\
 'Criterion'+'1.7',\
 'Criterion'+'1.1',\
 'Criterion'+'1.9',\
 'Criterion'+'1.10']
,'gj':['比利时','澳大利亚','美国','日本'],'pj':['LC','C','PC','NC']}
    print(context)
    return render(request,"chx.html",context)

def detail(request,gid):
    #根据商品编号，查询商品对象
    goods=GoodsInfo.objects.get(pk=gid)
    #增加人气
    # goods.gclick+=1
    # goods.save()
    #查询当前分类对应的最新的两个商品
    nlist=goods.gtype.goodsinfo_set.all().order_by('-id')[0:2]

    context={'title':'商品详细页','isCart':'yes','goods':goods,'nlist':nlist}
    response=render(request, 'tx_text/detail.html', context)

    # 记录当前浏览,
    #cookie中只能存储字符串，不能存储列表，而需要存储5个，所以需要转换
    #读取cookies中已经存储的商品编号
    zjll_str=request.COOKIES.get('zjll','')
    #将字符串转换成列表'1,2,3,4,5'=>[1,2,3,4,5]
    zjll_list=zjll_str.split(',')
    #如果当前编号已经存在则删除
    if gid in zjll_list:
        zjll_list.remove(gid)
    #最近，将编号加入第一个元素
    zjll_list.insert(0,gid)
    #如果超过5个则删除最后一个
    if len(zjll_list)>5:
        zjll_list.pop()
    #将列表转成字符串[1,2,3,4,5]=》'1,2,3,4,5'
    zjll_str=','.join(zjll_list)
    #存入cookie
    response.set_cookie('zjll',zjll_str,expires=60*60*24*14)

    return response
class MySearchView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['isCart']='yes'
        context['isSearch']='yes'
        return context


def chuanshu(request):
# ############### 添加数据 ###############
    #全量更新：
    update=True


    import numpy as np
    import pandas as pd

    if  update==True:


        FatfCx_xu.objects.all().delete()

        excel = pd.ExcelFile(r'/Users/saimatsu/Downloads/fatf619.xls')

        for i in excel.sheet_names:
            t='df'+i


            t=pd.read_excel(r'/Users/saimatsu/Downloads/fatf619.xls',sheetname=i)
            for x in np.array(t):
                FatfCx_xu.objects.create(bglx=x[0], jy=x[1], cjzb=x[2], gj=x[3], pj=x[4], pgyw=x[5], pjnr=x[6],bzh=x[7])

            print(FatfCx_xu)
    else:
         #增量更新
            excel = pd.ExcelFile(r'/Users/saimatsu/Downloads/fatf619.xls')

            for i in excel.sheet_names:
                t = 'df' + i

                t = pd.read_excel(r'/Users/saimatsu/Downloads/fatf619.xls', sheetname=i)
                for x in np.array(t):
                    FatfCx_xu.objects.create(bglx=x[0], jy=x[1], cjzb=x[2], gj=x[3], pj=x[4], pgyw=x[5], pjnr=x[6], bzh=x[7])

            print(FatfCx_xu)
# data=pd.read_csv(r'/Users/saimatsu/Desktop/fatf618.csv',encoding='utf8')

    # print(data)
    #
    #
    # for x in np.array(data):
    #
    #     FatfCx_xu.objects.create(bglx=x[0], jy=x[1], cjzb=x[2], gj=x[3], pj=x[4], pgyw=x[5], pjnr=x[6],bzh=x[7])


    # product_list_to_insert = list(data)
    # print(product_list_to_insert)
    # for x in data:
    #     product_list_to_insert.append(FatfCx_xu(bglx=x[0], jy=[1], cjzb=[2], gj=[3], pj=[4], pgyw=[5], pjnr=[6],bzh=[7]))
    # FatfCx_xu.objects.bulk_create(product_list_to_insert)
    return HttpResponse("导数完成")


def query(request):

    return render(request,'search/query.html')


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = "请输入关键词"
        return render(request, 'index.html', {'error_msg': error_msg})

    post_list = FatfCx_xu.objects.filter(Q(pgyw__icontains=q) | Q(pjnr__icontains=q))
    print("Q:%s q:%s" %Q %q)
    return render(request, 'index.html', {'error_msg': error_msg,
                                               'post_list': post_list})



from django.shortcuts import render
from django.http import JsonResponse
def ajax(request):
    if request.method == 'POST':
        print(request.POST)
        data = {'status': 0, 'msg': '请求成功', 'data': [11, 22, 33, 44]}  # 假如传人的数据为一字典
        # return HttpResponse(json.dumps(data))      #原来写法，需要dumps
        return JsonResponse(data)  # 后来写法
    else:
        return render(request, 'ajax.html')


from django.http import JsonResponse

def json1(request):
    a='2'
    return render(request,'json1.html',{'a':a})
def json2(request):
    return JsonResponse({'h1':'hello','h2':'world'})

def fatf_base(request):
    t=FatfCx_xu.objects.all()

    return render(request, 'FATF.html')
def post2(request):
    # if request.POST:
    import re

    dict=request.POST
    # table_dict=FatfCx_xu.objects.all()
    print(dict)
    bglx=dict.get('sex1')
    jy = dict.get('sex2')
    cjzb = dict.get('sex3')
    gj = dict.get('sex4')
    pj = dict.get('sex5')
    # mhjs = dict.get('sex6')
    # pattern = 'Criterion\s\d{1,9}'
    # m = re.match(pattern, cjzb)
    # m = re.match(pattern, 'Criterion 123')



    print('sss1:%s' %bglx)
    print('sss1:%s' %jy)
    print('sss1:%s' %cjzb)
    print('sss1:%s' %gj)
    print('sss1:%s' %pj)
    # else:
    #     return HttpResponse("失败")
    pp=[]
    for i in FatfCx_xu.objects.all():
        pp.append(i.cjzb)
        print(set(pp))

    # context={'bglx'}
    # if FatfCx_xu.cjzb:
    post_list = FatfCx_xu.objects.filter(Q(bglx=bglx)&Q(jy=jy))
    # post_list=post_list.filter(cjzb=cjzb)
    print('#############')
    # for i in  post_list:
    #     print(i.cjzb)
    # print('#############')

    if gj!='请选择' and cjzb!='请选择' and pj!='请选择' :

        post_list=post_list.filter(Q(gj=gj)&Q(cjzb=cjzb)&Q(pj=pj))
    elif gj!='请选择' and cjzb!='请选择':
        post_list=post_list.filter(Q(gj=gj)&Q(cjzb=cjzb))

    elif gj != '请选择' and pj != '请选择' :
        post_list=post_list.filter(Q(gj=gj) & Q(pj=pj))
    elif cjzb != '请选择' and pj != '请选择':
        post_list=post_list.filter(Q(cjzb=cjzb) & Q(pj=pj))

    elif  gj!='请选择':
        post_list=post_list.filter(Q(gj=gj))
    elif cjzb != '请选择':
        post_list=post_list.filter(Q(cjzb=cjzb))
    elif pj != '请选择':
        post_list=post_list.filter(Q(pj=pj))
    else:
        pass

    # if mhjs!='请填写':
        # post_list.filter(Q(pjnr__contains=mhjs))
    # else:
    #     pass

    #
    # print('########################')
    # print(post_list)
    #
    # for i in post_list:
    #    print( i.cjzb)
    # print('########################')
    # (Q(cjzb__icontains=cjzb) & Q(pj__icontains=pj)))
    # for i in post_list.get(cjzb).cjzb:
    #     print("cjzbbbbbb:%s" %i)
    # bglx=[]
    # cjzb=[]
    # jy=[]
    # gj=[]
    # pj=[]
    # pgyw=[]
    # pjnr=[]
    # bzh=[]
    # for i in post_list:
    #     cjzb.append(i.cjzb)
    #     bglx.append(i.bglx)
    #     jy.append(i.jy)
    #     gj.append(i.gj)
    #     pj.append(i.pj)
    #     pgyw.append(i.pgyw)
    #     pjnr.append(i.pjnr)
    #     # , 'pgyw': pgyw, 'pjnr': pjnr
    # content={'bglx':bglx,'jy':jy,'cjzb':cjzb,'gj':gj,'pj':pj, 'pgyw': pgyw, 'pjnr': pjnr}
    # data={}
    # data['status']='success'
    # data['xuge']='xuge'
    tt={'tt':post_list}
    # return  JsonResponse(data)
    return render(request,'post2.html', tt)
import json

def scene_update_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        status = 0
        result = "Error!"
        return HttpResponse(json.dumps({
            "status": status,
            "result": result
        }))





            # t = []
    # # for i in upwd:
    # #     t.append(i.gj)
    # #     t.append(i.wj)
    # #     t.append(i.bglx)
    # context={'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':a}
    # for j in pp:
    #     a.append(j.bglx)
    #     print("a:%s"%a)
    #
    # # t=[]
    # # for i in upwd:
    # #     t.append(i.gj)
    # #     t.append(i.wj)
    # #     t.append(i.bglx)
    # context={'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':a}
    # # print(FATF.gj.)
    # print(FATF.objects.all())
    # return redirect('/chx/',context)