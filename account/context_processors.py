from account.models import Account

def current_account(request):
    current_user = request.user
    if current_user and not current_user.is_anonymous:
        current_account = Account.objects.get(user=current_user)
    return {'current_account': current_account,}
