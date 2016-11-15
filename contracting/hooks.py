from . import __version__ as app_version

app_name = "contracting"
app_title = "Contracting"
app_publisher = "Revant Nandgaonkar"
app_description = "App for Contracting Enterprises"
app_icon = "octicon octicon-zap"
app_color = "grey"
app_email = "revant.one@gmail.com"
app_license = "GPL v2"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/contracting/css/contracting.css"
# app_include_js = "/assets/contracting/js/contracting.js"

# include js, css files in header of web template
# web_include_css = "/assets/contracting/css/contracting.css"
# web_include_js = "/assets/contracting/js/contracting.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "contracting.install.before_install"
# after_install = "contracting.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

notification_config = "contracting.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"contracting.tasks.all"
# 	],
# 	"daily": [
# 		"contracting.tasks.daily"
# 	],
# 	"hourly": [
# 		"contracting.tasks.hourly"
# 	],
# 	"weekly": [
# 		"contracting.tasks.weekly"
# 	]
# 	"monthly": [
# 		"contracting.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "contracting.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "contracting.event.get_events"
# }

