from django.db.models import Lookup
from django.db.models.fields import Field
from django.db.models.fields.related import RelatedField

@RelatedField.register_lookup
class HasAncestor(Lookup):
    """
    mmpt ancestor
    """
    lookup_name = 'has_ancestor'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' % (lhs, rhs), params
