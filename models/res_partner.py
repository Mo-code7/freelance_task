from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def default_salesperson(self):
        return self.env.user.id  # Set the logged-in user as the default salesperson

    @api.model
    def default_country(self):
        return self.env.user.company_id.country_id.id  # Get country from the user's company

    @api.model
    def default_state(self):
        return self.env.user.company_id.state_id.id  # Get state from the user's company

    user_id = fields.Many2one(
        'res.users', string="Salesperson", default=default_salesperson)

    country_id = fields.Many2one(
        'res.country', string="Country", default=default_country)

    state_id = fields.Many2one(
        'res.country.state', string="State", default=default_state)
