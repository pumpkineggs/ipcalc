default_ip = (192, 168, 0, 1)
prefix = 16
default_mask_decimal = (255, 255, 255, 0)
mask_full_octets = prefix // 8
mask_remain_bits = prefix % 8
mask_binary = ['0' * 8, '0' * 8, '0' * 8, '0' * 8]
mask_decimal = [0, 0, 0, 0]
wildcard_decimal = [0, 0, 0, 0]
print 'Default Mask: {:08b} {:08b} {:08b} {:08b}'.format(default_mask_decimal[0], default_mask_decimal[1],
                                                         default_mask_decimal[2], default_mask_decimal[3])
print 'Prefix: ', prefix
print 'Full octets: ', mask_full_octets
print 'Mask remain bits: ', mask_remain_bits
if mask_full_octets > 0:
    for i in range(mask_full_octets):
        mask_decimal[i] = 255
        mask_binary[i] = '1' * 8
    print 'Mask first stage preparation: ', mask_decimal
    print 'Msk binary preparation: ', mask_binary
    if mask_full_octets == 4:
        print "It's a single host mask: ", '.'.join(str(e) for e in mask_decimal)
    if mask_remain_bits > 0:
        remain_octet_index = mask_full_octets - 4
        print 'Remain octet index:', remain_octet_index
        mask_remain_octet_str = ('1' * mask_remain_bits) + '0' * (8 - mask_remain_bits)
        mask_remain_octet = int(mask_remain_octet_str, 2)
        print 'Remain octet value: ', mask_remain_octet
        mask_decimal[remain_octet_index] = mask_remain_octet
        mask_binary[remain_octet_index] = ('1' * mask_remain_bits) + '0' * (8 - mask_remain_bits)
        print 'New mask binary: ', mask_binary
        print 'New mask: ', '.'.join(str(e) for e in mask_decimal)
    else:
        print 'No remain bits!'
        print "New mask", '.'.join(str(e) for e in mask_decimal)
        print 'New mask binary: ', mask_binary
wildcard_binary = []
print 'Initial wildcard: ', wildcard_binary
wc_str = ''
for i in range(4):
    wildcard_binary.insert(i, '')
    for bit in mask_binary[i]:
        if bit == '1':
            wildcard_binary[i] += '0'
        else:
            wildcard_binary[i] += '1'
print wildcard_binary
