from telegrambot.handlers.conf import command

from .views import StartView

urlpatterns = [
    command('start', StartView.as_command_view()),

]
