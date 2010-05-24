from content.models import ModelBase

from secretballot import views

def can_vote(request, content_type, object_id, vote):
    return content_type.model_class().objects.get(id=object_id).can_vote(request)
    
def like_modelbase(request, id, vote):
    redirect_url = request.META['HTTP_REFERER']
    return views.vote(request, content_type=ModelBase, object_id=id, vote=vote, redirect_url=redirect_url, can_vote_test=can_vote)

def like_modelbase_ajax(request, id, vote):
    return views.vote(request, content_type=ModelBase, object_id=id, vote=vote, template_name='likes/inclusion_tags/likes.html', can_vote_test=can_vote, extra_context={'can_vote': False})
