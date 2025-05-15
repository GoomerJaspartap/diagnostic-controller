from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
import asyncio
import logging

# Configure logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

async def run_server():
    # Initialize data store
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [0]*100),    # Discrete Inputs
        co=ModbusSequentialDataBlock(0, [0]*100),    # Coils
        hr=ModbusSequentialDataBlock(0, [0]*100),    # Holding Registers
        ir=ModbusSequentialDataBlock(0, [0]*100)     # Input Registers
    )
    context = ModbusServerContext(slaves=store, single=True)

    # Start the server
    address = ("127.0.0.1", 5020)  # Using IPv4 explicitly and non-privileged port
    server = await StartAsyncTcpServer(
        context=context,
        address=address
    )
    
    log.info(f"Modbus Server started on {address}")
    
    # Keep the server running
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(run_server()) 