# QRify

QRify is an Odoo app that allows users to turn records into QR codes. Scanning the QR code will open the concerned record in the Odoo system. The app creates a unique QR code each time a new record is created.

Installation
Install the app by downloading the code from the GitHub repository or by installing it directly from the Odoo app store.

Make sure the required library qrcode is installed. If not, install it using the following command:

Copy code:
pip install qrcode

Usage
Go to the Odoo app menu and select the QRify app.

Select the model for which you want to generate QR codes (e.g., product.template).

Create a new record for the model.

The app will generate a unique QR code for the new record.

