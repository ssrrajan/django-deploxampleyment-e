from django import template

register = template.Library()

@register.filter(name='cutter')
def cutter(value,arg):
    """
    THIS CUTS OUT ALL VALUES OF "arg" FROM THE STRING!
    """

    return value.replace(arg,'')

# register.filter('cut',cutter)