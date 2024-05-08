import socket
import threading
from database import save_message, fetch_pending_messages, mark_messages_as_sent

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

def handle_client(client_socket, addr):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Received message: {message}")
            from_user, msg = message.split(": ", 1)
            save_message(from_user, f"{addr[0]}:{addr[1]}", msg)
            # Fetch pending messages for the user and send them
            pending_messages = fetch_pending_messages(f"{addr[0]}:{addr[1]}")
            for message in pending_messages:
                client_socket.send(message[0].encode())
            mark_messages_as_sent(f"{addr[0]}:{addr[1]}")
    except ConnectionResetError:
        print(f"Connection reset by peer {addr}")
    except ConnectionAbortedError:
        print(f"Connection aborted by host {addr}")
    finally:
        client_socket.close()
        print(f"Connection closed with {addr}")

def connect_to_peer(host, port):
    """
    Create a socket connection to the specified host and port.
    """
    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        peer_socket.connect((host, port))
    except socket.error as e:
        print(f"Failed to connect to {host}:{port}, error: {e}")
        peer_socket.close()
        return None
    return peer_socket

def send_message(peer_socket, message):
    """
    Send a message to a connected peer socket.
    """
    try:
        peer_socket.sendall(message.encode())
    except socket.error as e:
        print(f"Failed to send message, error: {e}")