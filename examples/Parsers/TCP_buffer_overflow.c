#include <stdio.h>
#include <stdint.h>
#include <string.h>

// Define a simplified TCP header structure
struct TCPHeader {
    uint16_t src_port;   // Source port
    uint16_t dst_port;   // Destination port
    uint32_t seq_num;    // Sequence number
    uint32_t ack_num;    // Acknowledgment number
    uint8_t data_offset; // Data offset (indicates the size of the TCP header)
    uint8_t flags;       // Flags
    uint16_t window;     // Window size
    uint16_t checksum;   // Checksum
    uint16_t urgent_ptr; // Urgent pointer
};

// Define a buffer size (smaller than the TCP header size to simulate out-of-bounds access)
#define BUFFER_SIZE 10

// Function to parse the TCP header
void parse_tcp_header(const uint8_t *buffer, size_t buffer_size) {
    // Check if the buffer is large enough to hold the TCP header
    // This prevent a buffer overflow
    if (buffer_size < sizeof(struct TCPHeader)) {
        printf("Error: Buffer size is too small for TCP header\n");
        return;
    }

    // Cast the buffer to a TCPHeader structure pointer
    const struct TCPHeader *header = (const struct TCPHeader *)buffer;

    // Print the TCP header fields
    printf("Source Port: %u\n", header->src_port);
    printf("Destination Port: %u\n", header->dst_port);
    printf("Sequence Number: %u\n", header->seq_num);
    printf("Acknowledgment Number: %u\n", header->ack_num);
    printf("Data Offset: %u\n", header->data_offset);
    printf("Flags: %u\n", header->flags);
    printf("Window Size: %u\n", header->window);
    printf("Checksum: %u\n", header->checksum);
    printf("Urgent Pointer: %u\n", header->urgent_ptr);
}

int main() {
    // Create a buffer with some data (smaller than the TCP header size)
    uint8_t buffer[BUFFER_SIZE];
    memset(buffer, 0, BUFFER_SIZE);

    // Call the parse_tcp_header function with the buffer
    parse_tcp_header(buffer, BUFFER_SIZE);

    return 0;
}
