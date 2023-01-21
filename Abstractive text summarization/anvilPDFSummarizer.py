from ._anvil_designer import pdf_summarizationTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class pdf_summarization(pdf_summarizationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  
  def primary_color_1_click(self, **event_args):
    user_input = self.text_area_1.text
    percentage = self.percentage.text
    result = anvil.server.call('abstractive_summmary',user_input,percentage)
    self.summary.text = result[0]
    self.words_original.text = result[1]
    self.words_summary.text = result[2]

  def button_1_click(self, **event_args):
    open_form('text_summarization.home_page')

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    a = self.file_loader_1.file.name
    c = anvil.server.call("pdf",file,a)
    self.text_area_1.text = c  
