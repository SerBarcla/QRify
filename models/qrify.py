import base64
import qrcode
import io
from odoo import models, fields, api
from odoo.exceptions import UserError

def generate_qr_code(product_name):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(product_name)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        qr_code = base64.b64encode(buffer.getvalue()).decode()
    except Exception as e:
        raise UserError("Error generating QR code: {}".format(str(e)))
    return qr_code

class QrifyProduct(models.Model):
    _name = 'qrify.product'

    product_id = fields.Many2one('product.template', string="Product", required=True)
    qr_code = fields.Binary(string="QR Code")

    @api.model
    def create(self, vals):
        record = super(QrifyProduct, self).create(vals)
        qr_code = generate_qr_code(record.product_id.name)
        record.write({'qr_code': qr_code})
        return record
