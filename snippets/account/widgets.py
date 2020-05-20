from django import forms
from django.utils.safestring import mark_safe


class ImagePreviewWidget(forms.widgets.FileInput):

    class Media:
        """Add media to this widget."""
        css = {
            'all': ('styles/imagePreview.css',)
        }
        js = ('scripts/imagePreview.js',)

    def render(self, name, value, attrs=None, **kwargs):
        """Render the widget."""
        input_html = super().render(name, value, attrs, **kwargs)
        id = attrs['id']
        if bool(value):
            img_html = mark_safe(
                f'<img src="{value.url}" id="{id}_preview" class="preview-widget"/>')
        else:
            img_html = '<p>Aucune image n\'est actuellement uploadée.</p>'
        script = mark_safe(
            f'<script>listenImagePreview("#{id}", "#{id}_preview")</script>')
        return f'{input_html}{img_html}{script}'
