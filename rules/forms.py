from django import forms
from .models import Rule

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ['rule_string']
        widgets = {
            'rule_string': forms.TextInput(attrs={'class': 'input-field'}),
        }

class CombineRulesForm(forms.Form):
    rule_ids = forms.CharField(
        label='Rule IDs (comma-separated)',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'input-field'})
    )

class EvaluateRuleForm(forms.Form):
    mega_rule_id = forms.IntegerField(
        label='Mega Rule ID',
        widget=forms.NumberInput(attrs={'class': 'input-field'})
    )
    data = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'textarea-field', 'rows': 5}),
        label='Data (JSON)'
    )

class ModifyRuleForm(forms.Form):
    rule_id = forms.IntegerField(
        label='Rule ID',
        widget=forms.NumberInput(attrs={'class': 'input-field'})
    )
    new_rule_string = forms.CharField(
        label='New Rule String',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'input-field'})
    )
