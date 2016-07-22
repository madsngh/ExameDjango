from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question,Answer,Option,StoreUserAns,Total



def home(request):

    print(request.POST.get('selected'))

    Questions=Question.objects.all()

    paginator = Paginator(Questions, 1)

    page = request.GET.get('page')

    try:

        contacts = paginator.page(page)
    except PageNotAnInteger:

        contacts = paginator.page(1)

    except EmptyPage:

        contacts = paginator.page(paginator.num_pages)

    context={
        'que':contacts
    }
    if(request.method=='POST'):

        for que in contacts:
            k=Answer.objects.get(id=que.correct_answer_id)
            print(k.correct_answer)
            print(request.user)
            d=0
            try:
                stored_ans=StoreUserAns.objects.filter(user=request.user)
                if len(stored_ans)==0:
                    st = StoreUserAns(user=request.user, ques_id=que.correct_answer_id,
                                     subans=request.POST.get('selected'))
                    st.save()


                else:

                    for astored_ans in stored_ans:
                        print(que.correct_answer_id)
                        print(astored_ans.ques_id)

                        if(astored_ans.ques_id == que.correct_answer_id):
                            print("condition true")
                            sua=StoreUserAns.objects.get(ques_id=que.correct_answer_id)
                            print("dint get sua")
                            print("got suA")
                            sua.subans=request.POST.get('selected')
                            sua.save()
                            d=d+1
                            break

                    print(d)
                    if(d==0):
                        print(d)

                        k = StoreUserAns(user=request.user, ques_id=que.correct_answer_id,
                                             subans=request.POST.get('selected'))
                        k.save()

            except:
                    pass

    return render(request,"helloworld.html",context)


def results(request):

    try:
        ans = Answer.objects.all()
        stored_ans = StoreUserAns.objects.filter(user=request.user)
        print("try kia")
        k=Total.objects.get(user_id=request.user.id)
        print("k milla")
        for anwers in ans:
            print(anwers.id)
            print("\n \n")
            for stor in stored_ans:
                print(stor.ques_id)
                print("exiting for")
                if (anwers.id == stor.ques_id):
                    print("into if")
                    if (anwers.correct_answer in stor.subans):
                        print("ans_correct")
                        k.marks = k.marks + 1
                        break
                    else:
                        print("%s %s",(anwers.correct_answer,stor.subans))
                        k.marks = k.marks - 1
                        break
        k.save()
        print(k.marks)


    except:
        print("into except")
        k=Total(user=request.user,marks=0)
        k.save()
        for anwers in ans:
            for stor in stored_ans:
                print("exiting for")
                if (anwers.id == stor.ques_id):
                    if(anwers.correct_answer is stor.subans):
                        k.marks = k.marks + 1
                        break
                    else:
                        k.marks = k.marks - 1
                        break
        k.save()

        print(k.marks)

    return render(request,"results.html",{})