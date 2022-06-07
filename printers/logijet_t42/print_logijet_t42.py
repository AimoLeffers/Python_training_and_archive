import socket
import logging
from datetime import datetime


def main():
    message = setup_message("151104", "Test Customer", "Testprojekt", "92", datetime.today().strftime('%d.%m.%Y'))
    udp_print('192.168.1.134', message)
    return


def setup_message(p_nr: str, p_customer: str, p_desc: str, basket_nr: str, print_date: str):
    print_msg = f"""
    A50,200,0,5,1,1,N,"{p_nr}"\n
    A50,250,0,5,1,1,N,"{p_customer}"\n
    A50,300,0,5,1,1,N,"{p_desc}"\n
    A50,350,0,5,1,1,N,"Warenkorbnummer: {basket_nr}"\n
    A50,400,0,5,1,1,N,"Druckdatum: {print_date}"\n
    P1\n
    """

    logging.info(print_msg)
    return bytes(print_msg, 'utf-8')


def udp_print(printer_ip: str, print_message: bytes, printer_port: int = 9100):
    """
    Prints a message in RAW-Format on the specified printer

    :param printer_ip:  IP-Adresse of the printer
    :param printer_port: Port of the printer (Defaults to 9100)
    :param print_message: the message, which will be send
    :return:
    """
    logging.info(f"IP: {printer_ip}")
    logging.info(f"Port: {printer_port}")
    logging.info(f"Port: {print_message}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((printer_ip, printer_port))

    sock.sendall(print_message)

    sock.close()
    return


if __name__ == "__main__":
    main()
