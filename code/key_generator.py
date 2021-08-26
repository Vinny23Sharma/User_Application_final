from cryptography.fernet import Fernet


class Keys:
    @staticmethod
    def generate_key():
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    @staticmethod
    def load_key():
        return open("secret.key", "rb").read()

    @staticmethod
    def encrypt_message(message):
        key = Keys.load_key()
        encoded_message = message.encode("utf-8")
        f = Fernet(key)
        encrypted_message = f.encrypt(encoded_message)
        return encrypted_message

    @staticmethod
    def decrypt_message(encrypted_message):
        key = Keys.load_key()
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message)
        return decrypted_message


# x = Keys.encrypt_message(msg).decode("utf-8")
# y = Keys.decrypt_message(msg.encode("utf-8")).decode("utf-8")

