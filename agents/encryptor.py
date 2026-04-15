import os
import hmac
import hashlib
import base64
from pathlib import Path
from dotenv import load_dotenv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

load_dotenv(dotenv_path=str(Path.home() / "member-system" / ".env"))


def _get_key(env_var: str) -> bytes:
    raw = os.getenv(env_var, "")
    key = raw.encode("utf-8")
    # 32바이트로 맞춤 (부족하면 패딩, 초과하면 자름)
    return (key + b"\x00" * 32)[:32]


def _encrypt(plaintext: str, key: bytes) -> str:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    enc = cipher.encryptor()
    # PKCS7 패딩
    data = plaintext.encode("utf-8")
    pad_len = 16 - (len(data) % 16)
    data += bytes([pad_len] * pad_len)
    ct = enc.update(data) + enc.finalize()
    return base64.b64encode(iv + ct).decode("utf-8")


def _decrypt(ciphertext: str, key: bytes) -> str:
    raw = base64.b64decode(ciphertext)
    iv, ct = raw[:16], raw[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    dec = cipher.decryptor()
    data = dec.update(ct) + dec.finalize()
    # PKCS7 언패딩
    pad_len = data[-1]
    return data[:-pad_len].decode("utf-8")


def encrypt_phone(phone: str) -> str:
    return _encrypt(phone, _get_key("PHONE_SECRET_KEY"))


def decrypt_phone(encrypted: str) -> str:
    return _decrypt(encrypted, _get_key("PHONE_SECRET_KEY"))


def encrypt_email(email: str) -> str:
    return _encrypt(email, _get_key("EMAIL_SECRET_KEY"))


def decrypt_email(encrypted: str) -> str:
    return _decrypt(encrypted, _get_key("EMAIL_SECRET_KEY"))


def hash_phone(phone: str) -> str:
    """중복 확인용 HMAC 해시 (결정론적)"""
    key = _get_key("PHONE_SECRET_KEY")
    return hmac.new(key, phone.encode("utf-8"), hashlib.sha256).hexdigest()


def hash_email(email: str) -> str:
    """중복 확인용 HMAC 해시 (결정론적)"""
    key = _get_key("EMAIL_SECRET_KEY")
    return hmac.new(key, email.lower().encode("utf-8"), hashlib.sha256).hexdigest()


def mask_phone(phone: str) -> str:
    """010-1234-5678 → 010-****-5678"""
    parts = phone.split("-")
    if len(parts) == 3:
        return f"{parts[0]}-****-{parts[2]}"
    return "***-****-****"


def encrypt_data(data: dict) -> dict:
    """전화번호, 이메일 암호화, 마스킹, 해시 처리"""
    phone = data.get("phone", "")
    email = data.get("email", "")
    return {
        "phone_encrypted": encrypt_phone(phone),
        "phone_masked": mask_phone(phone),
        "phone_hash": hash_phone(phone),
        "email_encrypted": encrypt_email(email),
        "email_hash": hash_email(email),
    }
