import PIL.Image


class TextureBaker:
    class TextureReference:
        def __init__(self):
            pass

        def get_texture(self):
            pass

        def get_texture_group(self):
            pass

        def get_uv(self, section=(0, 0, 1, 1)):
            pass

    def __init__(self):
        pass

    def add_texture(self, texture: PIL.Image.Image):
        pass

    def bake(self):
        pass
