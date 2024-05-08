# Chat Application

## Introduction
This project is a simple chat application implemented in Python. It uses socket programming for network communication and SQLite for storing messages. The application allows users to start a server, connect to other peers, and exchange messages.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)

## Installation
Clone this repository or download the source code. Python 3.6 or higher is required. No external libraries are needed, as the application uses Python's standard library.

```bash
git clone https://github.com/ahmedk31/P2P.git
```

## Usage
Run the application by executing the `main.py` file:

```bash
python main.py
```

Follow the on-screen prompts to start the server and connect to peers.

## Features
- **Server Initialization:** Start a chat server that listens on a specified host and port.
- **Connect to Peers:** Connect to a peer using their host and port.
- **Message Exchange:** Send and receive messages in real-time.
- **Database Interaction:** Store messages and retrieve pending messages from a local SQLite database.

## Dependencies
- Python 3.6 or higher
- SQLite 

## Configuration
No additional configuration is required to use the basic functionality of this application.

## Documentation
The project is documented inline within the source code.

## Examples
**Starting the server:**
```plaintext
Enter your host (e.g., localhost): localhost
Enter your port (e.g., 12345): 12345
Enter your username: user1
```
**Sending a message:**
```plaintext
1. Send Message
2. Exit
Enter choice: 1
Enter peer's host: localhost
Enter peer's port: 12346
Enter message: Hello, how are you?
```
## Troubleshooting
- **Firewall Issues:** Ensure that the ports you are using are not blocked by your firewall.
- **Server Availability:** Confirm that the server you are trying to connect to is currently running.

## Contributors
- Kawsar Ahmed

