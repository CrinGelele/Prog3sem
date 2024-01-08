# Файл tests.py

import unittest
from main import *


class Test(unittest.TestCase):
    disks = [Disk(1, 'Alphaville - Jerusalem', 'WEA', 1986, 1),
             Disk(2, 'Orden Ogan - Final Days', 'AFM', 2021, 1),
             Disk(3, 'George Orwell - 1984', 'Verlag', 2007, 3),
             Disk(4, 'Read dead redemption 2', 'Rockstar', 2018, 2),
             Disk(5, 'God of War: Ragnarok', 'Sony', 2022, 2)
             ]

    libs = [Library(1, 'Max Sergeev'),
            Library(2, 'Name Nickname'),
            Library(3, 'MGTU')
            ]

    disk_lib = [DiskLibrary(1, 1),
                DiskLibrary(2, 1),
                DiskLibrary(1, 2),
                DiskLibrary(4, 2),
                DiskLibrary(3, 2),
                DiskLibrary(3, 3),
                DiskLibrary(2, 2),
                DiskLibrary(5, 2)
                ]

    def test_1(self):
        otm = [(i, j) for i in disks for j in libs if i.lib_id == j.id[0]]
        otm.sort(key=lambda x: x[1].id)
        ans = []
        for i in otm:
            if i[1].owner[0] == 'M':
                ans.append(i[1].owner)
        ans1 = sorted(list(set(ans)))
        self.assertEqual(ans1, ['MGTU', 'Max Sergeev'])

    def test_2(self):
        otm = [(i, j) for i in disks for j in libs if i.lib_id == j.id[0]]
        otm.sort(key=lambda x: x[1].id)
        dic = {}
        for i in otm:
            if i[1].owner in dic:
                dic[i[1].owner] = min(dic[i[1].owner], i[0].release_date)
            else:
                dic[i[1].owner] = i[0].release_date
        sorted_dic = sorted(dic.items(), key=lambda x: x[1])
        self.assertEqual(sorted_dic, [('Max Sergeev', 1986), ('MGTU', 2007), ('Name Nickname', 2018)])

    def test_3(self):
        mtm_tmp = [(i.owner, j.disk_id) for i in libs for j in disk_lib if i.id[0] == j.lib_id]
        mtm = [(i[0], str(j)) for i in mtm_tmp for j in disks if i[1] == j.id[0]]
        ans3 = sorted(mtm, key=lambda x: x[0])
        self.assertEqual(ans3, [('MGTU', 'George Orwell - 1984 by Verlag(2007)'), ('Max Sergeev', 'Alphaville - Jerusalem by WEA(1986)'), ('Max Sergeev', 'Orden Ogan - Final Days by AFM(2021)'), ('Name Nickname', 'Alphaville - Jerusalem by WEA(1986)'), ('Name Nickname', 'Read dead redemption 2 by Rockstar(2018)'), ('Name Nickname', 'George Orwell - 1984 by Verlag(2007)'), ('Name Nickname', 'Orden Ogan - Final Days by AFM(2021)'), ('Name Nickname', 'God of War: Ragnarok by Sony(2022)')])

