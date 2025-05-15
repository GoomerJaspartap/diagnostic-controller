from pymodbus.client import AsyncModbusTcpClient
import asyncio
import logging

# Configure logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

async def run_client():
    # Create client
    client = AsyncModbusTcpClient('127.0.0.1', port=5020)  # Using IPv4 explicitly and matching server port
    
    try:
        # Connect to the server
        await client.connect()
        log.info("Connected to Modbus server")

        # Example 1: Read holding registers
        result = await client.read_holding_registers(address=0, count=5)
        if not result.isError():
            log.info(f"Holding registers: {result.registers}")
        else:
            log.error(f"Error reading holding registers: {result}")

        # Example 2: Write to holding registers
        values = [10, 20, 30, 40, 50]
        result = await client.write_registers(address=0, values=values)
        if not result.isError():
            log.info("Successfully wrote to holding registers")
        else:
            log.error(f"Error writing to holding registers: {result}")

        # Example 3: Read coils
        result = await client.read_coils(address=0, count=5)
        if not result.isError():
            log.info(f"Coils: {result.bits}")
        else:
            log.error(f"Error reading coils: {result}")

        # Example 4: Write to coils
        values = [True, False, True, False, True]
        result = await client.write_coils(address=0, values=values)
        if not result.isError():
            log.info("Successfully wrote to coils")
        else:
            log.error(f"Error writing to coils: {result}")

    except Exception as e:
        log.error(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(run_client()) 