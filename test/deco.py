from helper import register


class ClassB:
    pass


@register(ClassB)
class ClassA:
    class Meta:
        title = 'class A'
