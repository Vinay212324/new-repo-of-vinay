from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
import random

class RegisterForm(models.Model):
    _name = 'registration.form'
    _description = 'Registration Form'

    name = fields.Char(string='Name')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    religion = fields.Selection([
        ('hindu', 'Hindu'),
        ('muslim', 'Muslim'),
        ('christian', 'Christian'),
        ('sikh', 'Sikh'),
        ('other', 'Other')
    ], string='Religion')
    caste = fields.Selection([
        ('general', 'General'),
        ('obc', 'OBC'),
        ('sc', 'SC'),
        ('st', 'ST'),
        ('other', 'Other')
    ], string='Caste')
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed')
    ], string='Marital Status')
    time_of_birth = fields.Float(string='Time of Birth')
    height = fields.Float(string='Height (in cm)')
    registered_by = fields.Selection([
        ('self', 'SELF'),
        ('parents', 'PARENTS'),
        ('siblings', 'SIBLINGS'),
        ('relative', 'RELATIVE'),
        ('friends', 'FRIEND')
    ], string='Registered By')

    education_id = fields.Many2one('education.model', string='Education')
    qualification = fields.Char(string='Qualification')
    specialization = fields.Char(string='Specialization')
    place_of_study = fields.Char(string='Place Of Study')
    year_of_pass = fields.Date(string='Year Of Pass')

    employment_status = fields.Selection(
        [('working', 'Working'), ('not working', 'Not Working')],
        string='Employment Status'
    )
    company_name = fields.Char(string='Company Name')
    experience = fields.Integer(string='Experience')
    location = fields.Char(string='Location')

    designation_id = fields.Many2one('designation.model', string='Designation')
    designation = fields.Selection([('Not working', 'Not working'), ('student', 'Student')], string='Designation')

    money_type = fields.Selection([('inr', 'INR'), ('usd', 'USD'), ('euro', 'EURO'), ('pounds', 'POUNDS')],
                                  string="Annual income")
    amount_inr = fields.Selection([('0-1000', '0 RS-1000 RS'), ('1000-2000', '1000 RS-2000 RS')], string="--->")
    amount_usd = fields.Selection([('0-1000', '0 USD-1000 USD'), ('1000-2000', '1000 USD-2000 USD')], string="--->")
    amount_euro = fields.Selection([('0-1000', '0 EURO-1000 EURO'), ('1000-2000', '1000 EURO-2000 EURO')],
                                   string="--->")
    amount_pound = fields.Selection([('0-1000', '0 POUNDS-1000 POUNDS'), ('1000-2000', '1000 POUNDS-2000 POUNDS')],
                                    string="--->")

    height_in_cms = fields.Selection([('cms', 'CMS')], string='Height In CMS')
    father_name = fields.Char(string='Father Name')
    father_occupation = fields.Selection(
        [("Accounting", "Accounting, Banking & Finance"), ("administration", "Administration & HR"),
         ("Architecture & Design", "Architecture & Design"), ("Beauty & Fashion", "Beauty & Fashion"),
         ("Defense, Airline & Aviation", "Defense, Airline & Aviation"),
         ("Education, Training & Science", "Education, Training & Science")])
    Accounting_Banking = fields.Selection(
        [("Accountant", "Accountant"), ("Banking", "Banking"), ("Chartered Accountant", "Chartered Accountant"),
         ("Company Secretary", "Company Secretary")], string="--->")
    administration_Hr = fields.Selection([("clerical Official", "Clerical Official"), ("Executive", "Executive")],
                                         string="--->")
    mother_name = fields.Char(string='Mother Name')
    mother_occupation = fields.Selection(
        [("Accounting", "Accounting, Banking & Finance"), ("administration", "Administration & HR")])
    mother_Accounting_Banking = fields.Selection(
        [("Accountant", "Accountant"), ("Banking", "Banking"), ("Chartered Accountant", "Chartered Accountant"),
         ("Company Secretary", "Company Secretary")], string="--->")
    mother_administration_Hr = fields.Selection(
        [("clerical Official", "Clerical Official"), ("Executive", "Executive")], string="--->")

    brother_married = fields.Selection([('1', '1'), ('2', '2'), ('3', '3')], string='Brothers Married')
    brother_unmarried = fields.Selection([('1', '1'), ('2', '2'), ('3', '3')], string='Brothers Unmarried')
    sisters_married = fields.Selection([('1', '1'), ('2', '2'), ('3', '3')], string='Sisters Married')
    sisters_unmarried = fields.Selection([('1', '1'), ('2', '2'), ('3', '3')], string='Sisters Unmarried')
    living_in = fields.Char(string='Family Currently Living In')
    family_hometown = fields.Char(string='Family Hometown')

    per_country_id = fields.Many2one("country.model", string='Country')
    per_state_id = fields.Many2one('state.model', string='State')
    per_district = fields.Char(string='City/District')
    per_town = fields.Char(string='Town/Village')
    per_address = fields.Char(string="Address")

    country_id = fields.Many2one("country.model", string='Country')
    state_id = fields.Many2one('state.model', string='State')
    district = fields.Char(string='City/District')
    town = fields.Char(string='Town/Village')
    address = fields.Char(string="Address")

    rasi_id = fields.Many2one("rasi.model", string="Rasi")
    star_id = fields.Many2one("star.model", string="Star")

    alternative_phone_number = fields.Char(string='Alternative Phone Number')
    other_r_number = fields.Char(string="Family / Friends / Other Contact Person Mobile Number")

    from_age = fields.Integer(string="Age:")
    to_age = fields.Integer(string="")

    willing_to_marry_other_caste = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                                    string='Willing to Marry Other Caste Or Religion')
    about_preferred_partner = fields.Char(string='About Preferred Partner')

    marital_status_ids = fields.One2many("marital.status", "statu_id", string="Marital status")
    employment_status_ids = fields.One2many("marital.status", "employ_id", string="Employment status")
    country_ids = fields.One2many("marital.status", "count_id", string="Country")
    state_ids = fields.One2many("marital.status", "sta_id", string="State")
    caste_ids = fields.One2many("marital.status", "caste_id", string="Caste")

    amoney_type = fields.Selection([('inr', 'INR'), ('usd', 'USD'), ('euro', 'EURO'), ('pounds', 'POUNDS')],
                                   string="Annual income")
    aamount_inr = fields.Selection([('0-1000', '0 RS-1000 RS'), ('1000-2000', '1000 RS-2000 RS')], string="--->")
    aamount_usd = fields.Selection([('0-1000', '0 USD-1000 USD'), ('1000-2000', '1000 USD-2000 USD')], string="--->")
    aamount_euro = fields.Selection([('0-1000', '0 EURO-1000 EURO'), ('1000-2000', '1000 EURO-2000 EURO')],
                                    string="--->")
    aamount_pound = fields.Selection([('0-1000', '0 POUNDS-1000 POUNDS'), ('1000-2000', '1000 POUNDS-2000 POUNDS')],
                                     string="--->")

    from_height = fields.Selection([('5ft 6in', '5ft 6in'), ('5ft 9in', '5ft 9in'), ('5ft 10in', '5ft 10in'),
                                    ('6ft 1in', '6ft 1in'), ('6ft 2in', '6ft 2in')], string='Height')

    to_height = fields.Selection(
        [('5ft 9in', '5ft 9in'), ('5ft 10in', '5ft 10in'), ('6ft 1in', '6ft 1in'), ('6ft 2in', '6ft 2in')],
        string='-->')

    rreligion = fields.Selection([
        ('hindu', 'Hindu'),
        ('muslim', 'Muslim'),
        ('christian', 'Christian'),
        ('sikh', 'Sikh'),
        ('other', 'Other')
    ], string='Religion')
    eeducation_id = fields.Many2one('education.model', string='Education')

    city_1 = fields.Char(string='City/District')
    otp = fields.Char(string="OTP")
    otp_visibility = fields.Boolean(string="OTP Visibility", compute='_compute_otp_visibility', store=True)

    @api.depends('phone_number')
    def _compute_otp_visibility(self):
        for record in self:
            if record.phone_number and len(record.phone_number) == 10:
                record.otp_visibility = True
            else:
                record.otp_visibility = False

    def action_click(self):
        self.otp = str(random.randint(100000, 999999))

    @api.constrains('alternative_phone_number', 'other_r_number')
    def _check_phone_numbers(self):
        phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
        for record in self:
            if record.alternative_phone_number and not phone_pattern.match(record.alternative_phone_number):
                raise ValidationError("Alternative phone number must be between 9 and 15 digits.")
            if record.other_r_number and not phone_pattern.match(record.other_r_number):
                raise ValidationError(
                    "Family / Friends / Other contact person mobile number must be between 9 and 15 digits.")

    @api.constrains('phone_number')
    def _check_phone_number(self):
        phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
        for record in self:
            if not phone_pattern.match(record.phone_number):
                raise ValidationError("Phone number must be between 9 and 15 digits.")

    @api.constrains('email')
    def _check_email(self):
        email_pattern = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$')
        for record in self:
            if not email_pattern.match(record.email):
                raise ValidationError("Invalid email format.")


class EducationDetails(models.Model):
    _name = 'education.model'
    _description = "For education details"

    edudetail_ids = fields.One2many('registration.form', 'education_id', string='Education Details')
    eedudetail_ids = fields.One2many('registration.form', 'eeducation_id', string='Education Details')


class Designation(models.Model):
    _name = 'designation.model'
    _description = "For designation"

    name = fields.Char(required=True)
    designation_ids = fields.One2many('registration.form', 'designation_id', string='Designation Category')


class Country(models.Model):
    _name = "country.model"
    _description = "For country details"

    name = fields.Char(string='Country Name')
    permanent_location_ids = fields.One2many('registration.form', "per_country_id", string="Permanent Locations")
    current_location_ids = fields.One2many('registration.form', "country_id", string="Current Locations")


class State(models.Model):
    _name = "state.model"
    _description = "For states information purposes"

    name = fields.Char(string='State Name')
    permanent_location_ids = fields.One2many('registration.form', "per_state_id", string="Permanent Locations")
    current_location_ids = fields.One2many('registration.form', "state_id", string="Current Locations")


class Rasi(models.Model):
    _name = "rasi.model"
    _description = "For generating the rasi"

    name = fields.Char(string="Rasi Name")
    rasi_ids = fields.One2many('registration.form', "rasi_id", string="Rasi")


class Star(models.Model):
    _name = "star.model"
    _description = "For generating the star"

    name = fields.Char(string="Star Name")
    star_ids = fields.One2many('registration.form', "star_id", string="Star")


class Marital(models.Model):
    _name = "marital.status"
    _description = "For marital status"

    statu_id = fields.Many2one('registration.form', string="Status")
    employ_id = fields.Many2one('registration.form', string="Employment Status")
    count_id = fields.Many2one('registration.form', string="Country")
    caste_id = fields.Many2one('registration.form', string="Caste")
    sta_id = fields.Many2one('registration.form', string="State")
