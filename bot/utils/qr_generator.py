import io

from qrcode.main import QRCode


def generate_qr(text: str, box_size: int, border: int,
                fill_color: str | None, back_color: str | None,
                file_format: str) -> bytes:
    qr = QRCode(box_size=box_size, border=border)
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    buffer = io.BytesIO()
    img.save(buffer)
    buffer.seek(0)

    return buffer.getvalue()