# rules/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RuleForm, CombineRulesForm, EvaluateRuleForm, ModifyRuleForm
from .models import Rule
from .node import Node, parse_rule_string, evaluate_ast
import json

# Main Page
def main_page(request):
    return render(request, 'rules/main_page.html')

# Create a new rule
def create_rule(request):
    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            rule_string = form.cleaned_data['rule_string']
            ast = parse_rule_string(rule_string)
            rule = Rule(rule_string=rule_string, ast=json.dumps(ast.to_dict()))
            rule.save()
            return render(request,'rules/create_rule.html',{"msg":f"Created SuccessFully with id{rule.id}"})
    else:
        form = RuleForm()

    return render(request, 'rules/create_rule.html', {'form': form})

# Combine multiple rules into one
def combine_rules(request):
    if request.method == 'POST':
        form = CombineRulesForm(request.POST)
        if form.is_valid():
            rule_ids = form.cleaned_data['rule_ids'].split(',')
            rules = Rule.objects.filter(id__in=rule_ids)
            combined_ast = Node('operator', 'AND', *[Node.from_dict(json.loads(rule.ast)) for rule in rules])
            combined_rule_string = " AND ".join([rule.rule_string for rule in rules])
            combined_rule = Rule(rule_string=combined_rule_string, ast=json.dumps(combined_ast.to_dict()))
            combined_rule.save()
            return render(request,'rules/combine_rules.html',{"msg":f"Combined SuccessFully with id{combined_rule.id}"})
    else:
        form = CombineRulesForm()

    return render(request, 'rules/combine_rules.html', {'form': form})

# Evaluate a rule based on its ID and provided data
def evaluate_rule(request):
    if request.method == 'POST':
        form = EvaluateRuleForm(request.POST)
        if form.is_valid():
            mega_rule_id = form.cleaned_data['mega_rule_id']
            data = json.loads(form.cleaned_data['data'])
            rule = Rule.objects.get(id=mega_rule_id)
            ast = Node.from_dict(json.loads(rule.ast))
            result = evaluate_ast(ast, data)
            return JsonResponse({'result': result})  # Respond as JSON
    else:
        form = EvaluateRuleForm()

    return render(request, 'rules/evaluate_rule.html', {'form': form})

# Modify an existing rule
def modify_rule(request):
    if request.method == 'POST':
        form = ModifyRuleForm(request.POST)
        if form.is_valid():
            rule_id = form.cleaned_data['rule_id']
            new_rule_string = form.cleaned_data['new_rule_string']
            rule = Rule.objects.get(id=rule_id)
            rule.rule_string = new_rule_string
            rule.ast = json.dumps(parse_rule_string(new_rule_string).to_dict())
            rule.save()
            return render(request, 'rules/modify_rule.html', {"msg":"Modified Successfully"})
    else:
        form = ModifyRuleForm()

    return render(request, 'rules/modify_rule.html', {'form': form})
#Show All Rules
def show_all_rules(request):
    rules = Rule.objects.all()
    return render(request, 'rules/show_all_rules.html', {'rules': rules})
