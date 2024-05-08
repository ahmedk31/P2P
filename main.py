from network import start_server, connect_to_peer, send_message
from database import setup_database,save_message
import threading

def user_interface():
    host = input("Enter your host (e.g., localhost): ")
    port = int(input("Enter your port (e.g., 12345): "))
    username = input("Enter your username: ")

    server_thread = threading.Thread(target=start_server, args=(host, port))
    server_thread.daemon = True
    server_thread.start()

    while True:
        print("\n1. Send Message")
        print("2. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            peer_host = input("Enter peer's host: ")
            peer_port = int(input("Enter peer's port: "))
            message = f"{username}: {input('Enter message: ')}"
            peer_socket = connect_to_peer(peer_host, peer_port)
            send_message(peer_socket, message)
            save_message(username, f"{peer_host}:{peer_port}", message)
            peer_socket.close()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    setup_database()  # Ensure the database is set up
    user_interface()  # Start the user interface
