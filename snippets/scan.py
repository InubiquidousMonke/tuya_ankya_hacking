import socket
import struct

camera_ip = 'Camera IP here' # Modify this to use

def send_cmd(cmd_id):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((camera_ip, 8012))
        s.send(struct.pack('<I', cmd_id))
        data = s.recv(512)
        s.close()
        return data
    except Exception as e:
        return b''

for i in range(16):
    response = send_cmd(i)
    print(f"CMD 0x{i:02X}: {response.hex()}")
