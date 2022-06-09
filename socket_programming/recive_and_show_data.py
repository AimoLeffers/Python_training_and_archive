import socket
import logging


def main():
    logging.basicConfig(level=logging.INFO)
    ip = '127.0.0.1'
    port = 9100

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.bind((ip, port))
        soc.listen()
        conn, addr = soc.accept()
        with conn:
            logging.info(f"Connected by: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                logging.info(f"Data recived: {str(data)}")


if __name__ == "__main__":
    main()
