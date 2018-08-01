from collections import defaultdict
import openpyxl


class Xl:

    all = defaultdict(list)

    def __init__(self, *args, **kwargs):
        self.arg_0 = args[0]
        self.arg_1 = args[1]
        self.arg_2 = args[2]
        self.arg_3 = args[3]
        self.arg_4 = args[4]
        self.arg_5 = args[5]
        self.arg_6 = args[6]
        self.arg_7 = args[7]
        self.arg_8 = args[8]
        self.arg_9 = args[9]
        self.arg_10 = args[10]
        self.arg_11 = args[11]
        self.arg_12 = args[12]
        self.arg_13 = args[13]
        self.arg_14 = args[14]
        self.arg_15 = float(args[15])
        self.arg_16 = args[16]
        self.arg_17 = args[17]
        self.arg_18 = args[18]
        self.arg_19 = args[19]
        self.arg_20 = args[20]
        self.arg_21 = args[21]
        self.arg_22 = args[22]
        self.arg_23 = args[23]
        self.arg_24 = args[24]
        self.arg_25 = args[25]
        self.arg_26 = args[26]
        self.arg_27 = args[27]
        self.arg_28 = args[28]
        self.arg_29 = args[29]
        self.arg_30 = args[30]
        self.arg_31 = args[31]
        self.arg_32 = args[32]
        self.arg_33 = args[33]
        self.arg_34 = args[34]
        self.arg_35 = args[35]
        self.arg_36 = args[36]
        self.arg_37 = args[37]
        self.arg_38 = args[38]
        self.arg_39 = args[39]
        self.arg_40 = args[40]
        self.all[kwargs['filename']].append(self)
        item = self.search(kwargs.get('filename'), self.arg_11)
        if item:
            if self.arg_15 > item.arg_15:
                item.arg_15 = self.arg_15
            del self
        else:
            self.all[kwargs.get('filename')].append(self)

    def __str__(self):
        return str(self.arg_11)

    def __repr__(self):
        return str(self.arg_11)

    def search(self, filename, attr):
        it = self.all[filename]
        for item in it:
            if item.arg_11 == attr:
                return item
        return None

    @classmethod
    def equal(cls):
        old_list = []
        new_list = []
        first, second = cls.all.keys()
        for item in cls.all[second]:
            old_item = item.search(first, item.arg_11)
            if old_item:
                old_item.arg_15 = item.arg_15
                old_list.append(old_item)
            else:
                new_list.append(item)
        print(old_list + new_list)

    @classmethod
    def load(cls, *args):
        for arg in args:
            file = openpyxl.load_workbook(filename=arg)
            for item in file['Products']:
                if item[0].value and item[0].value != 'product_id':
                    Xl(*(cell.value for cell in item), filename=arg)

Xl.load("1.xlsx", "2.xlsx")
print(Xl.all)
