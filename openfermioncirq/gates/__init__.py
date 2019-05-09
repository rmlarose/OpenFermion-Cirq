# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Gates useful for simulating fermions."""

from openfermioncirq.gates.common_gates import (
    FSWAP,
    FSwapPowGate,
    Rxxyy,
    Ryxxy,
    Rzz,
    rot11,
    XXYY,
    XXYYPowGate,
    YXXY,
    YXXYPowGate)

from openfermioncirq.gates.three_qubit_gates import (
    CRxxyy,
    CRyxxy,
    CXXYY,
    CYXXY,
    CXXYYPowGate,
    CYXXYPowGate,
    rot111)

from openfermioncirq.gates.fermionic_simulation import (
    QuadraticFermionicSimulationGate,
    CubicFermionicSimulationGate,
    QuarticFermionicSimulationGate)

from openfermioncirq.gates.four_qubit_gates import (
    DoubleExcitation,
    DoubleExcitationGate)
