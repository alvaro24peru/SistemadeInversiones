from odoo import fields, models, api, _

class AccountPaymentReport(models.TransientModel):
	_name = "account.payment.report"
	_description = "Report payment"

	user_id = fields.Many2one('res.users', string="User", required=True, default=lambda self: self.env.user)
	date_from = fields.Date(string="Date From", required=True)
	date_to = fields.Date(string="Date To", required=True)

	def action_print(self):
		return self.env.ref('account_payment_report.account_payment_cash_report').report_action(self)
	
	def get_datas(self):
		payments = self.get_query()
		dic = {}
		for ap in payments:
			for inv in ap.reconciled_invoice_ids:
				dic.setdefault(inv.invoice_payment_term_id.id, {})
				# dic[inv.invoice_payment_term_id.id] = 
		return value

	def get_query(self):
		res_ap = self.env['account.payment'].search([
			('date','>=',self.date_from),
			('date','<=',self.date_to),
			('create_uid','=',self.user_id.id)
			])
		# self._cr.execute(query_str)
		# query = self._cr.dictfetchall()
		return res_ap