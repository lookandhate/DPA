class MultiSerializerMixin:
    """
    Overridden to support several serializers for actions
    """

    serializer_classes = dict()
    default_serializer_class = None

    def get_serializer_class(self):
        return self.serializer_classes.get(
            self.action, self.default_serializer_class
        )
