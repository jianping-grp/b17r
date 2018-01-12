import json


def parse_ds_json(ds_json_file):
    """

    :param ds_json_file:
    :return: id, name, parent_id
    """
    json_data = json.load(open(ds_json_file))
    li = []

    def _get_children_names(item, parent=''):
        children = item.get('children')
        name = item.get('name')
        idx = name.find(' ')
        kegg_id = ''
        if idx >= 1:
            kegg_id, kegg_name = name[: idx].strip(), name[idx:].strip()
            if parent:
                li.append((kegg_id, kegg_name, parent))
            else:
                li.append((kegg_id, kegg_name))

        if children:
            for child in children:
                _get_children_names(child, kegg_id)

    _get_children_names(json_data)
    return li