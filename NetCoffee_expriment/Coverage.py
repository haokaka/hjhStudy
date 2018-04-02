from sys import argv


def coverage(ali_path, net_path):
    protein_set = set()
    fr = open(net_path, 'r')
    for interaction in fr.readlines():
        temp = interaction.strip().split('\t')
        protein_set.add(temp[1])
        protein_set.add(temp[2])
    fr.close()
    # print('number of all proteins:', len(protein_set))

    protein_ali_set = set()
    fr_ali = open(ali_path)
    for each in fr_ali.readlines():
        for pro in each.strip().split('\t'):
            protein_ali_set.add(pro)
    # print('number of alignment proteins:', len(protein_ali_set))
    _cov = float(len(protein_ali_set) / len(protein_set))
    print('coverage:', _cov)
    return _cov



# ali_path_netcoffee = 'F:\my_study\GO\\test_coverage\Result1.ali'
# ali_path_isorank = 'F:\my_study\GO\\test_coverage\Res_test1.txt'
# ali_path_multi = 'F:\my_study\GO\\test_coverage\Res_test1_CIQ_10_100_100.txt'
# net_path = 'F:\my_study\GO\\test_coverage\dataset1_nets.txt'
#
# coverage(ali_path_netcoffee, net_path)
# coverage(ali_path_isorank, net_path)
# coverage(ali_path_multi, net_path)


if '__name__' == '__main__':
    ali_path = argv[1]
    net_path = argv[2]
    coverage(ali_path, net_path)
