from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestProductMaterial(TransactionCase):

    # Create the supplier
    self.supplier_partner = self.env['res.partner'].create({
            'name': 'Your Supplier',
            'email': 'supplier@other.company.com',
            'supplier_rank': 10,
        })

    # Create the record
    def setUp(self, *args, **kwargs):
        """
        In the setUp() method, we create a record of the model and set the initial values 
        for 'code', 'name', 'type', 'price_unit', and 'partner_id'.
        """
        super(TestProductMaterial, self).setUp(*args, **kwargs)
        self.Model = self.env['product.material']
        self.record = self.Model.create({
            'code': 'K3D4',
            'name': 'Cotton 30S',
            'type': 'cotton',
            'price_unit': 150,
            'partner_id': self.partner_id.id,
        })

    # Update the record
    def test_update_field(self):
        """
        In the test_update_field() method, we update the value of 'code' using the write()
        method of the record object. Then, we use the assertEqual() method to check
        whether the value of 'field1' has been successfully updated. 
        """
        self.record.write({'code': 'T3CH'})
        self.assertEqual(self.record.code, 'T3CH')

    # Delete the record
    def test_delete_record(self):
        """
        In the test_delete_record() method, we first save the ID of the record to be deleted.
        Then, we use the unlink() method to delete the record.
        Finally, we use the browse() method to check if the record still exists,
        and use the assertFalse() method to confirm that the record has been successfully deleted.
        """
        record_id = self.record.id
        self.record.unlink()
        record = self.Model.browse(record_id)
        self.assertFalse(record.exists())

    # Validation Error on Price Unit
    def test_validation_error(self):
        """
        In the test_validation_error() method, we use the assertRaises() method to check if a 
        ValidationError is raised when creating a new record with an invalid value for 'price_unit'.
        If the validation error is raised, the test case passes.
        If the validation error is not raised, the test case fails.
        """
        with self.assertRaises(ValidationError):
            self.Model.create({
                'code': 'K3D4T3CH',
                'name': 'Levi',
                'type': 'jeans',
                'price_unit': 25,
                'partner_id': self.partner_id.id,
            })
