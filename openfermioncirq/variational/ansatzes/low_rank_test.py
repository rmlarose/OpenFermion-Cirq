#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import openfermion
import sympy

from openfermioncirq.variational.ansatzes import LowRankTrotterAnsatz


# 4-qubit LiH 2-2 with bond length 1.45
bond_length = 1.45
geometry = [('Li', (0., 0., 0.)), ('H', (0., 0., bond_length))]
lih_hamiltonian = openfermion.load_molecular_hamiltonian(
        geometry, 'sto-3g', 1, format(bond_length), 2, 2)


def test_low_rank_trotter_ansatz_params():

    n = openfermion.count_qubits(lih_hamiltonian)
    final_rank = 2
    ansatz = LowRankTrotterAnsatz(
            lih_hamiltonian,
            final_rank=final_rank,
            include_all_cz=True,
            include_all_z=True)
    assert len(list(ansatz.params())) == n + final_rank*(n + n*(n-1)//2)

    ansatz = LowRankTrotterAnsatz(lih_hamiltonian, final_rank=2)
    assert set(ansatz.params()) == {
            sympy.Symbol(name) for name in {
                'U_0_0', 'U_0_0_0', 'U_0_1_0', 'U_1_0',
                'U_1_0_0', 'U_1_1_0', 'U_2_0', 'U_2_0_0',
                'U_2_1_0', 'U_3_0', 'U_3_0_0', 'U_3_1_0',
                'V_0_1_0_0', 'V_0_1_1_0', 'V_0_2_0_0', 'V_0_2_1_0',
                'V_0_3_0_0', 'V_0_3_1_0', 'V_1_2_0_0', 'V_1_2_1_0',
                'V_1_3_0_0', 'V_1_3_1_0', 'V_2_3_0_0', 'V_2_3_1_0'
                }
            }


def test_low_rank_trotter_ansatz_param_bounds():

    ansatz = LowRankTrotterAnsatz(lih_hamiltonian, final_rank=2)
    assert ansatz.param_bounds() == [(-1.0, 1.0)] * len(list(ansatz.params()))


def test_swap_network_trotter_ansatz_default_initial_params_length():

    ansatz = LowRankTrotterAnsatz(lih_hamiltonian)
    assert len(ansatz.default_initial_params()) == len(list(ansatz.params()))
