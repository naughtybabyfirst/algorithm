# -*- coding: utf-8 -*-
terms = ['Believe', 'believe', 'bargain']


def manhattan_distance(u, v, norm = False):
    if u.shape != v.shape:
        raise ValueError('length error..')
    return abs(u - v).sum() if not norm else abs(u - v).mean()


for term in terms:
    print(manhattan_distance())