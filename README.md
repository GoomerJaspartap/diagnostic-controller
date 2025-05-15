# Modbus Client-Server Example

This is a simple Modbus TCP client-server implementation using Python and the pymodbus library.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. First, start the Modbus server:
```bash
python modbus_server.py
```

2. In a separate terminal, run the client:
```bash
python modbus_client.py
```

## Code Explanation

### Server Code (modbus_server.py)

The server implements a Modbus TCP server that can handle client requests. Here's a detailed breakdown:

```python
# Import necessary modules
from pymodbus.server import StartAsyncTcpServer  # For creating an async TCP server
from pymodbus.datastore import ModbusSequentialDataBlock  # For storing register data
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext  # For managing Modbus data
import asyncio  # For async/await functionality
import logging  # For logging server events

# Initialize data store with different types of registers:
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),    # Discrete Inputs (binary inputs)
    co=ModbusSequentialDataBlock(0, [0]*100),    # Coils (binary outputs)
    hr=ModbusSequentialDataBlock(0, [0]*100),    # Holding Registers (16-bit registers)
    ir=ModbusSequentialDataBlock(0, [0]*100)     # Input Registers (read-only 16-bit registers)
)
```

#### Register Types Explained:
- **Discrete Inputs (DI)**: Read-only binary inputs (0 or 1)
- **Coils (CO)**: Read/write binary outputs (0 or 1)
- **Holding Registers (HR)**: Read/write 16-bit registers (0-65535)
- **Input Registers (IR)**: Read-only 16-bit registers (0-65535)

Each type has 100 registers initialized to 0.

### Client Code (modbus_client.py)

The client demonstrates various Modbus operations. Here's what each operation does:

```python
# Example 1: Read holding registers
result = await client.read_holding_registers(address=0, count=5)
# Reads 5 registers starting from address 0

# Example 2: Write to holding registers
values = [10, 20, 30, 40, 50]
result = await client.write_registers(address=0, values=values)
# Writes the values to 5 registers starting from address 0

# Example 3: Read coils
result = await client.read_coils(address=0, count=5)
# Reads 5 coils (binary values) starting from address 0

# Example 4: Write to coils
values = [True, False, True, False, True]
result = await client.write_coils(address=0, values=values)
# Writes boolean values to 5 coils starting from address 0
```

#### Common Modbus Operations:
1. **Reading Registers**:
   - `read_holding_registers`: Read values from holding registers
   - `read_input_registers`: Read values from input registers
   - `read_coils`: Read binary values from coils
   - `read_discrete_inputs`: Read binary values from discrete inputs

2. **Writing Registers**:
   - `write_registers`: Write values to holding registers
   - `write_coils`: Write binary values to coils

## Technical Details

- The server runs on `127.0.0.1` (localhost) port `5020`
- Using port 5020 instead of standard Modbus port 502 to avoid permission issues
- All operations are asynchronous (using `async/await`) for better performance
- The server maintains its state in memory (data is lost when server restarts)
- Each register type has 100 registers (addresses 0-99)
- The client demonstrates both reading and writing operations
- Error handling is implemented for all operations

## Testing the Implementation

When you run the client, it will:
1. Connect to the server
2. Read initial values from holding registers
3. Write new values to holding registers
4. Read coil values
5. Write new values to coils

You can modify the client code to test different operations or add more functionality as needed.

## Common Use Cases

- Reading sensor values (using input registers)
- Controlling actuators (using coils)
- Storing configuration data (using holding registers)
- Monitoring binary inputs (using discrete inputs)

## Notes

- The server must be running before the client can connect
- All operations are logged for debugging purposes
- The implementation uses IPv4 explicitly to avoid IPv6-related issues
- The server runs indefinitely until manually stopped 