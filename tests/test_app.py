import os
import sys

# Make project root importable
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from app import app


def find_ids(component):
    found = []
    if hasattr(component, 'id') and component.id:
        found.append(component.id)

    if hasattr(component, 'children'):
        children = component.children
        if not isinstance(children, list):
            children = [children]
        for c in children:
            found.extend(find_ids(c))

    return found


def find_text(component, target):
    if hasattr(component, 'children'):
        children = component.children
        if isinstance(children, str):
            return target in children
        if isinstance(children, list):
            return any(find_text(child, target) for child in children)
        return find_text(children, target)
    return False


def test_header_is_present():
    assert find_text(app.layout, "Pink Morsel Sales Visualiser")


def test_graph_is_present():
    ids = find_ids(app.layout)
    assert "sales-line-chart" in ids


def test_region_picker_is_present():
    ids = find_ids(app.layout)
    assert "region-selector" in ids
