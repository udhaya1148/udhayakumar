from ._anvil_designer import home_pageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class home_page(home_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.

  def text_click(self, **event_args):
    open_form('text_summarization')

  def docx_click(self, **event_args):
    open_form('docx_summarization')
   
  def url_click(self, **event_args):
    open_form('web_page_summarization')

  def pdf_click(self, **event_args):
    open_form('pdf_summarization')
