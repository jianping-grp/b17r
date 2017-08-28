import graphene
from graphene import relay, resolve_only_args
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from . import models
import django_filters


class MoleculeFilter(django_filters.FilterSet):
    mol_id = django_filters.NumberFilter()

    class Meta:
        model = models.Molecule
        exclude = ['structure', 'torsionbv', 'atompairbv', 'mfp2', 'ffp2']


class MoleculeNode(DjangoObjectType):
    class Meta:
        model = models.Molecule
        exclude_fields = ['structure', 'torsionbv', 'atompairbv', 'mfp2', 'ffp2']
        interfaces = (relay.Node,)


class TargetFilter(django_filters.FilterSet):
    target_id = django_filters.NumberFilter

    class Meta:
        model = models.Target
        # fields = ['tid', 'target_id', 'related_targets']
        exclude = []


class TargetInteractionFilter(django_filters.FilterSet):
    ti_id = django_filters.NumberFilter()
    first_target = django_filters.NumberFilter()
    second_target = django_filters.NumberFilter()

    class Meta:
        model = models.TargetInteraction
        fields = {
            'mean': {'gt', 'gte', 'lt', 'lte'},
            'max': {'gt', 'gte', 'lt', 'lte'},
            'median': {'gt', 'gte', 'lt', 'lte'},
            'min': {'gt', 'gte', 'lt', 'lte'}
        }


class TargetInteractionNode(DjangoObjectType):
    class Meta:
        model = models.TargetInteraction
        filter_fields = ['max', 'max', 'mean', 'median']
        interfaces = (relay.Node,)


class TargetNode(DjangoObjectType):
    related_targets = relay.ConnectionField(TargetInteractionNode)

    @resolve_only_args
    def resolve_related_targets(self, **kwargs):
        return models.TargetInteraction.objects.get_target_interaction(self.target_id)

    class Meta:
        model = models.Target
        # only_fields = ['target_id', 'tid', 'related_targets']
        filter_fields = {
            'tid__pref_name': ['icontains']
        }
        # filter_fields = {
        #     'target_id': ['exact']
        # }
        interfaces = (relay.Node,)


class Query(graphene.AbstractType):
    target = relay.Node.Field(TargetNode)
    all_target = DjangoFilterConnectionField(TargetNode, filterset_class=TargetFilter)
    molecule = relay.Node.Field(MoleculeNode)
    all_molecule = DjangoFilterConnectionField(MoleculeNode, filterset_class=MoleculeFilter)
    target_interaction = relay.Node.Field(TargetInteractionNode)
    all_target_interaction = DjangoFilterConnectionField(
        TargetInteractionNode,
        filterset_class=TargetInteractionFilter
    )
