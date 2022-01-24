import pandas as pd
import numpy as np
from functools import reduce
from itertools import combinations


class Object:
    def __init__(self, attributes, row):
        self.name = row[0]
        self.data = dict()
        for i in range(len(attributes)):
            self.data[attributes[i]] = row[i + 1]

    def __repr__(self):
        return f"({self.name}: {self.data})"

    def ind_to(self, obj, attrs):
        return self.get_attrs(attrs) == obj.get_attrs(attrs)

    def get_attrs(self, attrs):
        return tuple(map(lambda a: self.data[a], attrs))


class System:
    # attrs = B

    def __init__(self, attributes, objects, dec):
        self.dec = dec
        self.attributes = set(attributes)
        self.objects = objects
        self.core = set(
            filter(lambda a: not self.is_redundant(attributes, a), attributes)
        )
        self.reducts = self.find_reducts()
        self.indiff_matrix = self.__indiff_matrix__()
        self.nondeterministic_rules = self.__nondeterministic_rules__()
        self.consistent = len(self.nondeterministic_rules) == 0

    def from_file(filename):
        f = open(filename, "r")
        rows = list(map(lambda l: l.rstrip().split(" "), f.readlines()))
        attributes = rows[0][1:-1]
        objects = dict(map(lambda r: (r[0], Object(rows[0][1:], r)), rows[1:]))
        return System(attributes, objects, rows[0][-1])

    def __repr__(self):
        return f"""System(attributes={self.attributes}, 
                objects={self.objects}, 
                core={self.core}), 
                reducts={self.reducts},
                nondeterministic rules={self.nondeterministic_rules},
                consistent={self.consistent}"""

    def __str__(self):
        return self.__repr__()

    def ind(self, attrs):
        result = []
        for o1 in self.objects:
            result.append((o1.name, o1.name))
            for o2 in self.objects[1:]:
                if o1.ind_to(o2, attrs):
                    result.append((o1.name, o2.name))
        return result

    def abstract_classes(self, attrs):
        classes = dict()
        for x in self.objects.values():
            x_attrs = x.get_attrs(attrs)
            if x_attrs in classes.keys():
                classes[x_attrs].add(x.name)
            else:
                classes[x_attrs] = {x.name}
            for y in list(self.objects.values())[1:]:
                y_attrs = y.get_attrs(attrs)
                if x_attrs == y_attrs:
                    classes[x_attrs].add(y.name)
        return set(map(frozenset, classes.values()))

    def abstract_class(self, obj, attrs):
        return frozenset(
            [
                x.name
                for x in self.objects.values()
                if x.ind_to(self.objects[obj], attrs)
            ]
        )

    def lower_approx(self, X, attrs):
        abs_cl = self.abstract_classes(attrs)
        subsets = [cl for cl in abs_cl if cl.issubset(X)]
        return set(reduce(lambda acc, x: acc | x, subsets))

    def upper_approx(self, X, attrs):
        abs_cl = self.abstract_classes(attrs)
        cross = [cl for cl in abs_cl if cl.intersection(X) != set()]
        return set(reduce(lambda acc, x: acc | x, cross))

    # Współczynnik dokładności
    def ex_factor(self, X, attrs):
        return 1.0 * len(self.lower_approx(X, attrs)) / len(self.lower_approx(X, attrs))

    def is_b_exact(self, X, attrs):
        return self.ex_factor(X, attrs) == 1.0

    def is_redundant(self, X, attr):
        return self.abstract_classes(X) == self.abstract_classes(set(X) - set(attr))

    def is_reduct(self, X):
        return self.abstract_classes(X) == self.abstract_classes(
            self.attributes
        ) and not any(map(lambda a: self.is_redundant(X, a), X))

    def find_reducts(self):
        add_size = 0
        while len(self.core) + add_size <= len(self.attributes):
            attributes = self.attributes
            reducts = set(
                filter(
                    self.is_reduct,
                    map(
                        lambda c: frozenset(self.core | set(c)),
                        combinations(self.attributes - self.core, add_size),
                    ),
                )
            )
            if len(reducts) > 0:
                return reducts
            add_size += 1
        return []

    def __indiff_matrix__(self):
        matrix = []
        for x in self.objects.values():
            row = []
            for y in self.objects.values():
                row.append(
                    set([key for key in self.attributes if x.data[key] != y.data[key]])
                )
            matrix.append(row)
        return matrix

    def map_to_decisions(self, s):
        return frozenset(map(lambda x: self.objects[x].data[self.dec], s))

    def __nondeterministic_rules__(self):
        return list(
            filter(
                lambda s: len(self.map_to_decisions(s)) != 1,
                self.abstract_classes(self.attributes),
            )
        )

    def __recalculate__(self):
        self.core = set(
            filter(lambda a: not self.is_redundant(self.attributes, a), self.attributes)
        )
        self.reducts = self.find_reducts()
        self.indiff_matrix = self.__indiff_matrix__()
        self.nondeterministic_rules = self.__nondeterministic_rules__()
        self.consistent = len(self.nondeterministic_rules) == 0

    def remove_inconsistency(self, inconsistency, method="generalisation"):
        if method == "generalisation":
            generalised_dec = self.map_to_decisions(inconsistency)
            for obj in inconsistency:
                self.objects[obj].data[self.dec] = generalised_dec
        if method == "quality":
            pass
        if method == "quantity":
            pass
        self.__recalculate__()

    def latex_with_lines(df, *args, **kwargs):
        kwargs["column_format"] = "|".join(
            [""] + ["l"] * df.index.nlevels + ["r"] * df.shape[1] + [""]
        )
        res = df.to_latex(*args, **kwargs)
        return res.replace("\\\\\n", "\\\\ \\hline\n").replace("\\_", "_")

    def to_latex(self):
        return System.latex_with_lines(
            pd.DataFrame(
                self.indiff_matrix,
                index=self.objects.keys(),
                columns=self.objects.keys(),
            )
        )
