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

import os
import pytest

from collections import Counter
from tools import sorteios


@pytest.fixture()
def sample_list_as_in_file():
    return [
        '323 Foo Bar',
        '342 X Y Z',
        '543 Bar Foo',
        '342 John Doe',
        '983 Fulano de Tal'
    ]


@pytest.fixture()
def sample_list_different_from_file():
    return [
        '323 Bar Bar',
        '983 Cicrano de Tal'
    ]


@pytest.fixture()
def filename():
    file_path = os.path.join(os.path.dirname(__file__), 'data/students.in')
    return file_path


@pytest.fixture()
def empty_group():
    return sorteios.Group(2)


@pytest.fixture()
def populated_group():
    return sorteios.Group(123, ["abc", "xyz"])


def test_new_empty_group(empty_group):
    assert empty_group.current == -1
    assert empty_group.alunos == []
    assert empty_group.numero == 2


def test_new_group(populated_group):
    assert populated_group.current == -1
    assert len(populated_group.alunos) == 2
    assert populated_group.numero == 123


def test_group_iteration(populated_group):
    assert populated_group.current == -1

    group_num = next(populated_group)
    assert group_num == populated_group.numero
    assert populated_group.current == 0

    first_student = next(populated_group)
    assert first_student == populated_group.alunos[0]
    assert populated_group.current == 1

    second_student = next(populated_group)
    assert second_student == populated_group.alunos[1]
    assert populated_group.current == 2

    with pytest.raises(StopIteration):
        next(populated_group)


def test_qnt_de_grupos(sample_list_as_in_file):
    assert sorteios.qnt_de_grupos(sample_list_as_in_file, 2) == (2, 1,)
    assert sorteios.qnt_de_grupos(sample_list_as_in_file, 3) == (1, 2,)
    assert sorteios.qnt_de_grupos(sample_list_as_in_file, 1) == (5, 0,)


def test_read_file(filename, sample_list_as_in_file,
                   sample_list_different_from_file):

    result = sorteios.read_file(filename)

    assert len(result) == len(sample_list_as_in_file)
    assert result == sample_list_as_in_file
    assert result != sample_list_different_from_file


@pytest.mark.parametrize('alunos_por_grupo, n_grupos_experado, resto_experado',
                         [(2, 2, 1), (3, 1, 2), (1, 5, 0)])
def test_sorteio(sample_list_as_in_file, alunos_por_grupo, n_grupos_experado,
                 resto_experado):
    grupos, resto = sorteios.sortear_equipes(sample_list_as_in_file,
                                             alunos_por_grupo)

    assert len(grupos) == n_grupos_experado
    assert len(resto) == resto_experado


def test_sorteio_unicidade_de_aluno(sample_list_as_in_file):
    grupos, alunos_sem_grupo = sorteios.sortear_equipes(
        sample_list_as_in_file, 2)

    merged = []
    for grupo in grupos:
        merged.extend(grupo.alunos)
    merged.extend(alunos_sem_grupo)

    assert Counter(merged) == Counter(sample_list_as_in_file)


def test_print_groups(sample_list_as_in_file):
    grupos, alunos_sem_grupo = sorteios.sortear_equipes(
        sample_list_as_in_file, 2)

    sorteios.print_grupos(grupos)
