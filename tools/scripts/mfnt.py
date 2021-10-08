import struct
import os

from PIL import Image, ImageDraw, ImageFont


class MFontEntry(object):
    def __init__(self, data):
        (self.x, self.y,
         self.width, self.height,
         self.attr1, self.attr2, self.attr3) = struct.unpack('hhhhhhh', data)
        self.bitmap = None

    def __cmp__(self, other):
        return self.width.__cmp__(other.width)

    def __repr__(self):
        return 'x: %d, y: %d, w: %d, h:%d' % (self.x, self.y, self.width, self.height)

    @property
    def right(self):
        return self.x + self.width

    @property
    def bottom(self):
        return self.y + self.height

    @property
    def box(self):
        return (self.x, self.y, self.right, self.bottom)

    @property
    def rect(self):
        return (self.x, self.y, self.width, self.height)


class MFont(object):
    def __init__(self, path=None):
        self.entries = []
        self.image_width = 0
        self.image_height = 0
        if path:
            self.load(path)
        print("Font size:", self.font_size)
        print("Count:", self.entry_count)

    def load(self, path):
        fs = open(path, 'rb')
        (magic, version, header_size,
         self.image_width, self.image_height,
         unk1, self.font_size,
         self.entry_count, ukn2, entry_offset, data_size) = struct.unpack('4siqiiiiiiqq',
                                                                          fs.read(struct.calcsize('4siqiiiiiiqq')))

        fs.seek(entry_offset, 0)
        self.entries = []
        for i in range(self.entry_count):
            self.entries.append(MFontEntry(fs.read(0x0E)))

        fs.close()

    def export_images(self, img_path, out_dir, char_table=None):
        img = Image.open(img_path)

        for i in range(len(self.entries)):
            im = img.crop(self.entries[i].box)
            path = '%d.png' % i
            if char_table:
                path = '%s.png' % chr(char_table[i])
            path = os.path.join(out_dir, path)
            try:
                if not os.path.exists(out_dir):
                    os.makedirs(out_dir)
                im.save(path)
                print('Save:', path)
            except:
                print('')
                continue

    def render_chars(self, out_path, img_path):
        img = Image.open(img_path)
        img_out = Image.new(
            "RGBA", (1024, int(self.font_size*self.entry_count/(1024/self.font_size))))

        x = 0
        y = 10
        for i in range(len(self.entries)):
            cim = img.crop(self.entries[i].box)
            # x += self.entries[i].attr1
            img_out.paste(cim, (x, y - self.entries[i].attr2))
            x += self.entries[i].attr3 - self.entries[i].attr1
            # x += self.font_size
            if x >= img_out.width-self.font_size:
                x = 0
                y += self.font_size

        img_out.save(out_path)


class CharTable(object):
    def __init__(self, path):
        fs = open(path, 'rb')
        (magic, version, entries_cnt, tbl_offset) = struct.unpack(
            '4siii', fs.read(16))
        fs.seek(tbl_offset, 0)

        self.entries = {}
        for i in range(entries_cnt):
            char, id = struct.unpack('ii', fs.read(8))
            self.entries[id] = char

    @property
    def chars(self):
        return list(self.entries.values())


def render(mfnt, png, png_out):
    MFont(mfnt).render_chars(png_out, png)


if __name__ == "__main__":
    import fire
    fire.Fire(render)
