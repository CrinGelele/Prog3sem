class Disk:
    def __init__(self, id, name, publisher, release_date, lib_id):
        self.id = id,
        self.name = name,
        self.publisher = publisher,
        self.release_date = release_date
        self.lib_id = lib_id

    def __str__(self):
        return f"{self.name[0]} by {self.publisher[0]}({self.release_date})"


class Library:
    def __init__(self, id, owner):
        self.id = id,
        self.owner = owner

    def __str__(self):
        return f"{self.owner}"


class DiskLibrary:
    def __init__(self, disk_id, lib_id):
        self.disk_id = disk_id
        self.lib_id = lib_id

    def __str__(self):
        return f"{self.disk_id[0]} - {self.lib_id[0]}"


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


def main():
    print('MGTU' > 'Max')
    otm = [(i, j) for i in disks for j in libs if i.lib_id == j.id[0]]
    otm.sort(key=lambda x: x[1].id)
    mtm_tmp = [(i.owner, j.disk_id) for i in libs for j in disk_lib if i.id[0] == j.lib_id]
    mtm = [(i[0], str(j)) for i in mtm_tmp for j in disks if i[1] == j.id[0]]
    print('-----------------Task 1:-----------------')
    print('...............Their CDs:...............')
    ans = []
    for i in otm:
        if i[1].owner[0] == 'M':
            ans.append(i[1].owner)
            print(i[1], 'owns', i[0])
    print('.......................................')
    print('Owners name start with m:', list(set(ans)))

    print('-----------------Task 2:-----------------')
    dic = {}
    for i in otm:
        if i[1].owner in dic:
            dic[i[1].owner] = min(dic[i[1].owner], i[0].release_date)
        else:
            dic[i[1].owner] = i[0].release_date
    sorted_dic = sorted(dic.items(), key=lambda x: x[1])
    print(sorted_dic)

    print('-----------------Task 3:-----------------')
    print(sorted(mtm, key=lambda x: x[0]))


if __name__ == '__main__':
    main()
