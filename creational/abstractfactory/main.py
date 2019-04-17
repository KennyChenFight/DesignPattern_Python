from creational.abstractfactory.model \
    import Rectangle, DotSharpFactory

rect = Rectangle(20, 10)
rect.paint(DotSharpFactory())