#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

typedef struct {
    uint32_t ack_number;  // Acknowledgment number (32 bits)
    uint16_t window;      // Window size (16 bits)
    bool ack_flag;        // ACK flag (1 bit)
} TCPPacketConstraints;

// Function to check the constraints
bool check_tcp_constraints(TCPPacketConstraints *packet) {
    // TCP Window fields must not be zero
    if (packet->window == 0) {
        return false;
    }

    // If ACK flag is set, ACK number must be non-zero
    if (packet->ack_flag && packet->ack_number == 0) {
        return false;
    }

    // If ACK flag is not set, ACK number should not be checked
    return true;
}

int main() {
    TCPPacketConstraints packet1 = {12345, 512, true};
    TCPPacketConstraints packet2 = {0, 512, false};
    TCPPacketConstraints packet3 = {0, 512, true};
    TCPPacketConstraints packet4 = {12345, 0, true};

    if (check_tcp_constraints(&packet1)) {
        printf("Packet 1 meets the constraints.\n");
    } else {
        printf("Packet 1 does not meet the constraints.\n");
    }

    if (check_tcp_constraints(&packet2)) {
        printf("Packet 2 meets the constraints.\n");
    } else {
        printf("Packet 2 does not meet the constraints.\n");
    }

    if (check_tcp_constraints(&packet3)) {
        printf("Packet 3 meets the constraints.\n");
    } else {
        printf("Packet 3 does not meet the constraints.\n");
    }

    if (check_tcp_constraints(&packet4)) {
        printf("Packet 4 meets the constraints.\n");
    } else {
        printf("Packet 4 does not meet the constraints.\n");
    }

    return 0;
}
