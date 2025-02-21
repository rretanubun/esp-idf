# SPDX-FileCopyrightText: 2022-2023 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0

import pytest
from pytest_embedded import Dut


@pytest.mark.esp32
@pytest.mark.esp32s3
@pytest.mark.esp32c6
# @pytest.mark.esp32h2  # IDF-6812
@pytest.mark.generic
@pytest.mark.parametrize(
    'config',
    [
        'release',
        'iram_safe',
    ],
    indirect=True,
)
def test_mcpwm(dut: Dut) -> None:
    dut.expect('Press ENTER to see the list of tests')
    dut.write('*')
    dut.expect_unity_test_output()
