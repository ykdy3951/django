from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from kuser.decorators import login_required
from .models import Board
from .forms import WriteForm
from kuser.models import Kuser

# Create your views here.


class BoardList(ListView):
    model = Board
    template_name = 'board.html'
    context_object_name = 'board_list'
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class BoardWrite(FormView):
    template_name = 'board_write.html'
    form_class = WriteForm
    success_url = '/board/'

    def form_valid(self, form):
        user = self.request.session['user']
        board = Board(
            title=form.data.get('title'),
            contents=form.data.get('contents'),
            writer=Kuser.objects.get(email=user)
        )
        board.save()

        return super().form_valid(form)


class BoardDetail(DetailView):
    template_name = 'board_detail.html'
    queryset = Board.objects.all()
    context_object_name = 'board'
