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

import click
from tools import sorteios


@click.group()
def cli():
    return


@cli.command(help='Opções para realizar sorteios diversos.')
@click.option('--file', '-f', default='./students.in', type=click.Path(
              exists=True))
@click.option('--tipo', '-t', nargs=1, type=click.Choice(['equipes',
                                                          'aluno']),
              help='Sorteios a partir de um arquivo com uma lista de alunos.')
@click.option('--n-alunos-por-grupo', '-n', type=int, default=2,
              help='Número de alunos por grupo.')
def sorteio(file, tipo, n_alunos_por_grupo):
    alunos = sorteios.read_file(file)
    if tipo == 'equipes':
        grupos, resto = sorteios.sortear_equipes(alunos, n_alunos_por_grupo)
        sorteios.print_grupos(grupos)
    if tipo == 'aluno':
        print(sorteios.sortear_aluno(alunos))


def main():
    cli(obj={})

