default_ip = (192, 168, 0, 1)
prefix = 27
default_mask_decimal = (255, 255, 255, 0)
mask_full_octets = prefix // 8
mask_remain_bits = prefix % 8
mask_binary = []
mask_decimal = [0, 0, 0, 0]
wildcard_decimal = [0, 0, 0, 0]
print 'Default Mask: {:08b} {:08b} {:08b} {:08b}'.format(default_mask_decimal[0], default_mask_decimal[1],
                                                 default_mask_decimal[2], default_mask_decimal[3])
print 'Prefix: ', prefix
print 'Full octets will first: ', mask_full_octets
print 'Mask remain bits: ', mask_remain_bits
if mask_full_octets > 0:
    for i in range(mask_full_octets):
        mask_decimal[i] = 255
    print 'Mask first stage preparation: ', mask_decimal
    if mask_remain_bits > 0:
        remain_octet_index = mask_full_octets - 4
        print 'Remain octet index:', remain_octet_index
        mask_remain_octet_str = ('1' * mask_remain_bits) + '0' * (8 - mask_remain_bits)
        mask_remain_octet = int(mask_remain_octet_str, 2)
        print 'Remain octet: ', mask_remain_octet
        mask_decimal[remain_octet_index] = mask_remain_octet
        wildcard_decimal[remain_octet_index] = mask_remain_octet
        print 'New mask: ', mask_decimal
        print 'Wildcard: ', wildcard_decimal
        print '.'.join(str(e) for e in wildcard_decimal)
    else:
        print 'No remain bits!'


