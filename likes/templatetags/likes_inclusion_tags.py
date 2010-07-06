from secretballot.models import Vote

from django import template

register = template.Library()

@register.inclusion_tag('likes/inclusion_tags/likes.html', takes_context=True)
def likes(context, obj):
    request = context['request']
    can_vote, vote_status = obj.can_vote(request)
    context.update({
        'content_obj': obj,
        'can_vote': can_vote,
        'vote_status': vote_status,
        'content_type': "-".join((obj._meta.app_label, obj._meta.module_name))
    })
    return context
