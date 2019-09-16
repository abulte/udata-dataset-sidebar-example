# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Blueprint

from udata import theme
from udata.frontend import conditionnal_template_hook

blueprint = Blueprint('dataset-sidebar-example', __name__,
                      template_folder='templates')


def example_condition(dataset):
    return True


@conditionnal_template_hook(example_condition)
def dataset_sidebar_example_block(dataset):
    return theme.render('dataset-block.html',
                        dataset=dataset)
