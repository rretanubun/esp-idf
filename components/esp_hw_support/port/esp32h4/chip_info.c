/*
 * SPDX-FileCopyrightText: 2025 Espressif Systems (Shanghai) CO LTD
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <string.h>
#include "esp_chip_info.h"
#include "hal/efuse_hal.h"

void esp_chip_info(esp_chip_info_t *out_info)
{
    memset(out_info, 0, sizeof(*out_info));
    out_info->model = CHIP_ESP32H4;
    out_info->revision = efuse_hal_chip_revision();
    out_info->cores = 2;
    out_info->features = CHIP_FEATURE_BLE | CHIP_FEATURE_IEEE802154;
}
