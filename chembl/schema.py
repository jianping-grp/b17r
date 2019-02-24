from graphene import relay
from graphene_django import DjangoConnectionField, DjangoObjectType

from . import models


class ActionTypeNode(DjangoObjectType):
    class Meta:
        model = models.ActionType
        filter_fields = ['action_type', 'parent_type']
        interfaces = (relay.Node,)


class ActivitiesNode(DjangoObjectType):
    class Meta:
        model = models.Activities
        filter_fields = [
            'activity_id', 'assay', 'doc', 'record', 'molregno',
            'standard_relation', 'published_value', 'published_units',
            'pchembl_value', 'type', 'toid', 'published_type', 'data_validity_comment',
            'units'
        ]
        interfaces = (relay.Node,)


class ActivityPropertiesNode(DjangoObjectType):
    class Meta:
        model = models.ActivityProperties
        filter_fields = [
            'ap_id', 'activity', 'type', 'value', 'units', 'standard_type', 'standard_relation',
            'standard_value', 'standard_units', 'standard_text_value', 'comments'
        ]
        interfaces = (relay.Node,)


class ActivityStdsLookupNode(DjangoObjectType):
    class Meta:
        model = models.ActivityStdsLookup
        filter_fields = ['std_act_id']
        interfaces = (relay.Node,)


class ActivitySuppNodeNode(DjangoObjectType):
    class Meta:
        model = models.ActivitySupp
        filter_fields = ['as_id', 'standard_type', 'standard_value', 'standard_units']
        interfaces = (relay.Node,)


class AssaysNode(DjangoObjectType):
    class Meta:
        model = models.Assays
        filter_fields = [
            'assay_id', 'doc', 'assay_type', 'assay_tissue', 'tid', 'tissue', 'variant',
            'chembl', 'src'
        ]
        interfaces = (relay.Node,)


class BindingSitesNode(DjangoObjectType):
    class Meta:
        model = models.BindingSites
        filter_fields = ['site_id', 'site_name', 'tid']
        interfaces = (relay.Node,)


class TargetDictionaryNode(DjangoObjectType):
    class Meta:
        model = models.TargetDictionary
        filter_fields = [
            'tid', 'target_type', 'pref_name', 'tax_id', 'organism', 'chembl'
        ]
        interfaces = (relay.Node,)


class Query(object):
    action_type = relay.Node.Field(ActionTypeNode)
    all_action_types = DjangoConnectionField(ActionTypeNode)

    activities = relay.Node.Field(ActivitiesNode)
    all_activities = DjangoConnectionField(ActivitiesNode)

    target_dictionary = relay.Node.Field(TargetDictionaryNode)
    all_target_dictionaries = DjangoConnectionField(TargetDictionaryNode)
