from ._anvil_designer import text_summarizationTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class text_summarization(text_summarizationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.

  def primary_color_1_click(self, **event_args):
    user_input = self.user_input.text
    percentage = self.percentage.text
    result = anvil.server.call('abstractive_summmary',user_input,percentage)
    self.summary.text = result[0]
    self.words_original.text = result[1]
    self.words_summary.text = result[2]

  def button_1_click(self, **event_args):
   open_form('text_summarization.home_page')
