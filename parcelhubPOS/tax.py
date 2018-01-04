from django_tables2 import RequestConfig
from django.shortcuts import render
from django.forms import modelformset_factory
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .tables import TaxTable
from .commons import *
from .models import Tax, UserBranchAccess
from django.http import HttpResponseRedirect
CONST_branchid = 'branchid'
#method to retrieve Courier tax list
@login_required
def taxlist(request):
    loggedusers = userselection(request)
    branchselectlist = branchselection(request)
    branchid = request.session.get(CONST_branchid)
    branchaccess = UserBranchAccess.objects.get(user__id=request.session.get('userid'), branch__id = request.session.get(CONST_branchid))
    menubar = navbar(request)
    tax_list = Tax.objects.all()
    formdata = {'taxcode':''}
    if request.method == "GET":
        submitted_taxcode = request.GET.get('taxcode') 
        if submitted_taxcode:
            formdata['taxcode'] = submitted_taxcode
            tax_list =  tax_list.filter(tax_code__icontains=submitted_taxcode)
    final_Tax_table = TaxTable(tax_list)
    
    RequestConfig(request, paginate={'per_page': 25}).configure(final_Tax_table)
    
    context = {
                'tax': final_Tax_table,
                'nav_bar' : sorted(menubar.items()),
                'branchselection': branchselectlist,
                'loggedusers' : loggedusers,
                'formdata' : formdata,
                'title': "Tax",
                'isedit' : branchaccess.masterdata_auth == 'edit',
                'statusmsg' : request.GET.get('msg'),
                }
    return render(request, 'tax.html', context)

@login_required
def edittax(request, taxid):
    loggedusers = userselection(request)
    branchselectlist = branchselection(request)
    menubar = navbar(request)
    taxid = request.GET.get('taxid')
    title = "New tax"
    if taxid:
        title = "Edit tax"
    taxqueryset = Tax.objects.filter(id=taxid)
    
    TaxFormSet = modelformset_factory(Tax, fields=('tax_code', 'gst'), max_num=1)
    if request.method == "POST":
        formset = TaxFormSet(request.POST, request.FILES,
                             queryset=taxqueryset)
        if formset.is_valid():
            tax_code_name = request.POST['form-0-tax_code'] 
            if title == 'New tax':
                msg = 'Tax "%s" have been created successfully.' % tax_code_name
            else:
                msg = 'Tax "%s" have been updated successfully.' % tax_code_name
            formset.save()
            return HttpResponseRedirect("/parcelhubPOS/tax/?msg=%s" % msg)
    else:
        formset = TaxFormSet(queryset=taxqueryset)
    
    context = {
                'formset': formset,
                'headerselectiondisabled' : True,
                'nav_bar' : sorted(menubar.items()),
                'branchselection': branchselectlist,
                'loggedusers' : loggedusers,
                'title' : title
                }
    return render(request, 'edittax.html', context)

@login_required
def deletetax(request, dtaxid ):
    dtaxid = request.GET.get('dtaxid')
    tax = Tax.objects.filter(id = dtaxid )
    msg = 'Tax "%s" have been deleted successfully.' % tax.first().tax_code
    if tax:
        tax.delete()
    return HttpResponseRedirect("/parcelhubPOS/tax/?msg=%s" % msg)