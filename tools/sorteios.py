#!/usr/bin/env python3

#  Copyright 2019 Universidade Estadual de Santa Cruz
#
#  Author: Prof. Mathias Santos de Brito <msbrito@uesc.br>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
import copy
import random

from tabulate import tabulate


class Group:

    def __init__(self, numero, alunos=None):
        self.numero = numero
        self.alunos = alunos or []
        self.current = -1

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        try:
            if self.current >= 0:
                current = self.alunos[self.current]
                self.current += 1
                return current
            if self.current == -1:
                self.current += 1
                return self.numero
        except IndexError:
            raise StopIteration


def read_file(file_name):

    try:
        with open(file_name) as fd:
            values = fd.read().splitlines()
        return values
    except IOError as e:
        print("Erro ao abrir arquivo." + str(e), file=sys.stderr)


def qnt_de_grupos(alunos, alunos_por_grupo):
    return len(alunos) // alunos_por_grupo, len(alunos) % alunos_por_grupo


def sortear_equipes(alunos, alunos_por_grupo):
    embaralhados = copy.deepcopy(alunos)
    random.shuffle(embaralhados)
    groups = []

    qnt_grupos, resto = qnt_de_grupos(embaralhados, alunos_por_grupo)

    for i in range(qnt_grupos):
        group = Group(i)
        for j in range(alunos_por_grupo):
            group.alunos.append(embaralhados.pop())

        groups.append(group)

    alunos_sem_grupo = embaralhados
    return groups, alunos_sem_grupo


def sortear_aluno(alunos):
    return alunos[random.randint(0, len(alunos) - 1)]


def print_grupos(grupos):
    print('\n')
    print(tabulate(grupos, tablefmt="github"))
    print('\n')


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Erro: Após o comando digite apenas a quantidade de alunsos por "
              "grupo")
        print("Uso: ./criar_grupos.py <arquivo> <alunos_por_grupo>")
        sys.exit(-1)

    sortear_equipes(read_file(sys.argv[1]), sys.argv[2])


