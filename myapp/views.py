import operator

from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import User, Message

from .forms import (
    LoginForm,
    SignUpForm,
    MessageForm,
    ChangeUsernameForm,
    ChangeMailForm,
    ChangeIconForm,
    ChangePasswordForm,
)

User = get_user_model()


def index(request):
    return render(request, "myapp/index.html")

def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        error_message = ''
    elif request.method == "POST":
        # 画像ファイルをformに入れた状態で使いたい時はformに"request.FILES"を加える。
        # request.POST だけではNoneが入る。
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            # モデルフォームはformの値をmodelsにそのまま格納できるsave()メソッドがあるので便利。
            form.save()
            # フォームから"username"を読み取る
            username = form.cleaned_data.get("username")
            # フォームから"password1"を読み取る
            password = form.cleaned_data.get("password1")
            # 認証情報のセットを検証するには authenticate() を利用してください。
            # このメソッドは認証情報をキーワード引数として受け取ります。
            # 検証する対象はデフォルトでは username と password であり
            # その組み合わせを個々の 認証バックエンド に対して問い合わせ、認証バックエンドで認証情報が有効とされれば
            # User オブジェクトを返します。もしいずれの認証バックエンドでも認証情報が有効と判定されなければ PermissionDenied が送出され、None が返されます。
            # (公式ドキュメントより)
            # つまり、authenticateメソッドは"username"と"password"を受け取り、その組み合わせが存在すれば
            # そのUserを返し、不正であれば"None"を返します。
            user = authenticate(username=username, password=password)
            if user is not None:
                # あるユーザーをログインさせる場合は、login() を利用してください。この関数は HttpRequest オブジェクトと User オブジェクトを受け取ります。
                # ここでのUserは認証バックエンド属性を持ってる必要がある。
                # authenticate()が返すUserはuser.backendを持つので連携可能。
                login(request, user)
            return redirect("/")
        # バリデーションが通らなかった時の処理を記述
        else:
            # エラー時 form.errors には エラー内容が格納されている
            print(form.errors)

    context = {
        "form": form,
    }
    return render(request, "myapp/signup.html", context)

class Login(LoginView):
    """ログインページ
    GETの時は指定されたformを指定したテンプレートに表示
    POSTの時はloginを試みる。→成功すればsettingのLOGIN_REDIRECT_URLで指定されたURLに飛ぶ
    """

    authentication_form = LoginForm
    template_name = "myapp/login.html"

@login_required
def friends(request):
    user = request.user
    friends = User.objects.exclude(id=user.id)
    
    info = []
    
    for friend in friends:
        latest_message = Message.objects.filter(
            Q(sender=user, receiver=friend) | Q(receiver=user, sender=friend)
        ).order_by('pub_time').last()

        if latest_message:
            data_list = [friend, latest_message.message, latest_message.pub_time]
        else:
            data_list = [friend, None, None]
            
        info.append(data_list)
            
    print(info)
    params = {
        'info': info
    }
    return render(request, 'myapp/friends.html', params)

@login_required
def talk_room(request, user_id):
    user = request.user
    friend = get_object_or_404(User, id=user_id)
    talk_data = Message.objects.filter(
        Q(sender=user, receiver=friend) | Q(receiver=user, sender=friend)
    ).order_by('pub_time')
    
    if request.method == "GET":
        form = MessageForm()
        error_message = ''
    elif request.method == "POST":
        new_talk = Message(sender=user, receiver=friend)
        form = MessageForm(request.POST, instance=new_talk)
        if form.is_valid():
            form.save()
            return redirect("talk_room", user_id)
        else:
            print(form.errors)
            
    params = {
        'friend': friend,
        'form': form,
        'talk_data': talk_data
    }
        
    return render(request, "myapp/talk_room.html", params)

@login_required
def setting(request):
    return render(request, "myapp/setting.html")

@login_required
def change_username(request):
    user = request.user
    if request.method == "GET":
        form = ChangeUsernameForm(instance=user)
        
    elif request.method == "POST":
        form = ChangeUsernameForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("change_username_done")
        else:
            print(form.errors)
    params = {
        'form': form,
    }
    return render(request, "myapp/change_username.html", params)
    

@login_required
def change_username_done(request):
    return render(request, "myapp/change_username_done.html")

@login_required
def change_mail(request):
    user = request.user
    if request.method == "GET":
        form = ChangeMailForm(instance=user)
        
    elif request.method == "POST":
        form = ChangeMailForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("change_mail_done")
        else:
            print(form.errors)
    params = {
        'form': form,
    }
    return render(request, "myapp/change_mail.html", params)

@login_required
def change_mail_done(request):
    return render(request, "myapp/change_mail_done.html")

@login_required
def change_icon(request):
    user = request.user
    if request.method == "GET":
        form = ChangeIconForm(instance=user)
        
    elif request.method == "POST":
        form = ChangeIconForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("change_icon_done")
        else:
            print(form.errors)
    params = {
        'form': form,
    }
    return render(request, "myapp/change_icon.html", params)

@login_required
def change_icon_done(request):
    return render(request, "myapp/change_icon_done.html")

class ChangePassword(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy("change_password_done")
    template_name = "myapp/change_password.html"
    
class ChangePasswordDone(PasswordChangeDoneView):
    """Django標準パスワード変更後ビュー"""