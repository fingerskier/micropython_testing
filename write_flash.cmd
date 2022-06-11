python -m esptool --chip esp32 --port COM14 erase_flash

python -m esptool --chip esp32 --port COM14 --baud 912600 write_flash -z 0x1000 ../tinypico-20220611-v1.18.bin