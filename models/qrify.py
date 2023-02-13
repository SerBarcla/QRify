from odoo import models, fields, api
from odoo.exceptions import UserError
import base64
import qrcode
import io

class QrifyProduct(models.Model):
    _name = 'qrify.product'

    product_id = fields.Many2one('product.template', string="Product", required=True)
    qr_code = fields.Binary(string="QR Code")

    @api.model
    def generate_qr_code(self, product):
        # Get the product record
        product_record = self.env['product.template'].browse(product.id)

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(product_record.name)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        qr_code = base64.b64encode(buffer.getvalue()).decode()
        return qr_code

    @api.model
    def create(self, vals):
        # Create the record
        record = super(QrifyProduct, self).create(vals)

        # Generate QR code
        qr_code = self.generate_qr_code(record.product_id)

        # Save the QR code in the record
        record.write({'qr_code': qr_code})
        return record
