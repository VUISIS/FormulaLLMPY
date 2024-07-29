#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <errno.h>

// Function to convert a single hexadecimal digit to its integer value
static int hex_digit_to_int(char c) {
    if (isdigit(c))
        return c - '0';
    else if (isxdigit(c))
        return tolower(c) - 'a' + 10;
    else
        return -1; // Invalid hexadecimal character
}

// Simplified inet_pton implementation for IPv6
int inet_pton(int af, const char *src, void *dst) {
    if (af != AF_INET6) {
        errno = EAFNOSUPPORT;
        return -1;
    }

    struct in6_addr *out = (struct in6_addr *)dst;
    unsigned char tmp[sizeof(struct in6_addr)];
    unsigned char *tp = tmp;
    const char *curtok = src;
    const char *endp = src + strlen(src);
    int saw_digit = 0, colonp = -1;

    while (curtok < endp) {
        int ch = *curtok++;
        int val = hex_digit_to_int(ch);

        if (val != -1) {
            if (saw_digit == 0) {
                *tp = val;
                saw_digit = 1;
            } else {
                if (*tp & 0xf0) return 0; // Overflow
                *tp = (*tp << 4) | val;
            }
        } else if (ch == ':') {
            curtok++; // Skip the colon
            if (!saw_digit) {
                if (colonp != -1) return 0; // Multiple "::" found
                colonp = tp - tmp;
            } else if (curtok == endp) {
                return 0; // Trailing ":" is invalid
            }
            saw_digit = 0;
        } else {
            return 0; // Invalid character
        }
        if (saw_digit) tp++;
    }

    if (colonp != -1) {
        memmove(tmp + sizeof(tmp) - (tp - tmp), tmp + colonp, tp - tmp - colonp);
        memset(tmp + colonp, 0, sizeof(tmp) - (tp - tmp));
    }

    memcpy(out, tmp, sizeof(struct in6_addr));
    return 1;
}
