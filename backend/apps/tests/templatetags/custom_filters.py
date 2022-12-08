from django import template

register = template.Library()

@register.filter
def correct_percentage(correct, un_correct):
    try:
        result = float(correct)*100/(float(correct) + float(un_correct))
        return "%.2f" % result + '%'
    except (ValueError, ZeroDivisionError):
        return ""
