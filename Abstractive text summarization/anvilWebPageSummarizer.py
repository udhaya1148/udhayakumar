from ._anvil_designer import web_page_summarizationTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class web_page_summarization(web_page_summarizationTemplate):
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

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    url = self.text_box_1.text
    inter = anvil.server.call('web_page_summary',url)
    self.text_area_1.text = inter
