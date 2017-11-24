from polls.models import Question, Choice

# 1) Crea una nuova question e 5 choices associate a quella question
q = Question(question_text="What's up?", pub_date=timezone.now())
q.save()
q = Question.objects.get(id=1)
q.choice_set.create(choice_text='Fine,thanks!', votes=0)
q.choice_set.create(choice_text='So-so', votes=0)
q.choice_set.create(choice_text='Everything is fine', votes=0)
q.choice_set.create(choice_text='The sun', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
q.save()

# 2) Modifica il valore del campo text della terza choices
c = q.choice_set.filter(choice_text__startswith='Everything is fine')
c.choice_text = 'Everything is bad'


# 3) Elimina la quarta choice
a = q.choice_set.filter(choice_text__startswith='The sun')
a.delete()

# 4)Stampa la lista delle questions presenti nel database
Question.objects.all()

# 5)Stampa la lista delle choices presenti nel database e 
#   per ogni choice stampa anche il testo della domanda associata
q = Question.objects.get(id=1)
b = q.choice_set.all()
print(q,b[0])
print(q,b[1])
print(q,b[2])
print(q,b[3])