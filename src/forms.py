from wtforms import Form, SelectMultipleField, widgets
from markupsafe import Markup


class CheckboxListWidget(widgets.ListWidget):
    def __call__(self, field, **kwargs):
        lines = []
        lines.append(f'<{self.html_tag} {widgets.html_params(**kwargs)}>')
        for subfield in field:
            if self.prefix_label:
                lines.append(f'<li>{subfield()} {subfield.label}</li>')
            else:
                lines.append(f'<li>{subfield()}</li>')
        lines.append(f'</{self.html_tag}>')
        html = '\n'.join(lines)
        return Markup(html)


class MultiCheckboxField(SelectMultipleField):
    widget = CheckboxListWidget()
    option_widget = widgets.CheckboxInput()
