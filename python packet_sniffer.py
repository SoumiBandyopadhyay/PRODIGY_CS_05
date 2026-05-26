from scapy.all import sniff, IP, TCP, UDP, Raw


def analyze_packet(packet):
    print("\n" + "=" * 60)

    # Check for IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]

        print(f"Source IP      : {ip_layer.src}")
        print(f"Destination IP : {ip_layer.dst}")
        print(f"Protocol Number: {ip_layer.proto}")

        # TCP Analysis
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            print("Protocol       : TCP")
            print(f"Source Port    : {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")

        # UDP Analysis
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            print("Protocol       : UDP")
            print(f"Source Port    : {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")

        else:
            print("Protocol       : Other")

        # Payload Preview
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            try:
                decoded_payload = payload.decode(errors='ignore')
                print("Payload Preview:")
                print(decoded_payload[:200])
            except Exception:
                print("Payload could not be decoded.")

    print("=" * 60)


def start_sniffer():
    print("Starting packet sniffer...")
    print("Press CTRL + C to stop.\n")

    try:
        sniff(prn=analyze_packet, store=False)
    except KeyboardInterrupt:
        print("\nSniffer stopped.")


if __name__ == "__main__":
    start_sniffer()
