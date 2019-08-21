import serial.tools.list_ports

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

import os

port_list = serial.tools.list_ports.comports()

if len(port_list) == 0:
    print("没有有效的串口设备连接电脑")
    os._exit(0)

while True:
    print("----------------------------------------------------------------")
    print("串口设备列表:")
    for i, port in enumerate(port_list):
        print("(", i, ") ",port)
    print("----------------------------------------------------------------")

    str = input("选择设备序号: ");
    num = int(str)
    
    if num > len(port_list):
        print("无效的设备序号")
    else:
        break

print('================' + port_list[0])

ser = serial.Serial(port_list[num].device, 9600)

logger = modbus_tk.utils.create_logger("console")
master = modbus_rtu.RtuMaster(ser)
if(master._serial.is_open == False):
    print("串口未被打开")
    os._exit(0)

try:
    master.set_timeout(5)
    master.set_verbose(True)
    logger.info("connected")

    while 1:
        while 1:
            print("-------------------------")
            print("操作列表")
            print("(0) 读电压")
            print("(1) 读电流")
            print("(2) 关输出")
            print("(3) 开输出")
            print("-------------------------")
            str = input("选择操作编号: ")
            num = int(str)
            if num > 3:
                print("非法的操作编号")
            else:
                break
    
        if num == 0:
            logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 16, 1))
        elif num == 1:
            logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 17, 1))
        elif num == 2:
            logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 1, 1, 0))
        elif num == 3:
            logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 1, 1, 1))

except modbus_tk.modbus.ModbusError as exc:
    logger.error("%s- Code=%d", exc, exc.get_exception_code())
