from ciphers.cipher_helper import get_character_map


class CaeserCipher:
    def __init__(self, rotation: int = None):
        self.default_character_map = get_character_map()
        self.flipped_default_character_map = self.flip_dict(
            self.default_character_map
        )

        if rotation:
            self.rotation = rotation
        else:
            self.rotation = len(self.default_character_map) // 2

        self.cipher_map = self.update_cipher_dict()
        self.flipped_cipher_map = self.flip_dict(self.cipher_map)

    @staticmethod
    def flip_dict(regular_dict):
        return {value: key for key, value in regular_dict.items()}

    def update_cipher_dict(self):
        # update map for new cipher
        character_map_length = len(self.default_character_map)
        return {
            key: ((value + self.rotation) % character_map_length)
            for key, value in self.default_character_map.items()
        }

    def encrypt(self, plain_text):
        encrypted = ""
        for character in plain_text:
            encrypted += self.flipped_cipher_map[
                self.default_character_map[character]
            ]

        return encrypted

    def decrypt(self, encrypted):
        plain_text = ""
        for character in encrypted:
            plain_text += self.flipped_default_character_map[
                self.cipher_map[character]
            ]

        return plain_text
