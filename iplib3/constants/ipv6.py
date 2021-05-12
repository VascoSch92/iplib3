"""IPv6 constants"""

# IPv6 constants
IPV6_NUMBER_BIT_COUNT  = 4
IPV6_SEGMENT_BIT_COUNT = 16
IPV6_MIN_SEGMENT_COUNT = 0 # Technically legal as long as there are at least two colons (::)
IPV6_MAX_SEGMENT_COUNT = 8
IPV6_MIN_SEGMENT_VALUE = 0x0 # (0)
IPV6_MAX_SEGMENT_VALUE = 0xFFFF # (65535)
IPV6_MIN_VALUE         = 0 # 0x0*0x10_000**0
IPV6_MAX_VALUE         = 340282366920938463463374607431768211455
                       # 0xFFFF*0x10_000**7 + ... + 0xFFFF*0x10_000**0
                       # 0xFFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF (32)
