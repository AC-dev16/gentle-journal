from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.utils.decorators import method_decorator
from datetime import datetime
from .models import DiaryEntry
from .forms import QuickEntryForm, DetailedEntryForm

def homepage(request):
    """Homepage with site information and auth buttons"""
    return render(request, 'diary_entries/homepage.html')

@login_required
def dashboard(request):
    """Dashboard with welcome message and quick entry form"""
    if request.method == 'POST':
        form = QuickEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            # Set default values for required fields not in quick form
            entry.location = entry.location or 'Not specified'
            entry.sleep_hours = entry.sleep_hours or 0
            entry.save()
            messages.success(request, 'Quick entry saved successfully!')
            return redirect('dashboard')
    else:
        form = QuickEntryForm()
    
    # Get recent entries for dashboard display
    recent_entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')[:3]
    
    # Determine greeting based on time of day
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "morning"
    elif current_hour < 18:
        greeting = "afternoon"
    else:
        greeting = "evening"
    
    context = {
        'form': form,
        'recent_entries': recent_entries,
        'user': request.user,
        'greeting': greeting
    }
    return render(request, 'diary_entries/dashboard.html', context)

@login_required
def entries_page(request):
    """Entries page with detailed form and list of all entries"""
    if request.method == 'POST':
        form = DetailedEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Detailed entry saved successfully!')
            return redirect('entries')
    else:
        form = DetailedEntryForm()
    
    # Get all user's entries
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'form': form,
        'entries': entries
    }
    return render(request, 'diary_entries/entries.html', context)

@login_required
def delete_entry(request, entry_id):
    """Delete a diary entry"""
    entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
    entry.delete()
    messages.success(request, 'Entry deleted successfully!')
    return redirect('entries')

# Keep your existing ListView for admin purposes
@method_decorator(login_required, name='dispatch')
class DiaryEntryList(generic.ListView):
    template_name = 'diary_entries/diaryentry_list.html'
    context_object_name = 'diary_entries'
    paginate_by = 10

    def get_queryset(self):
        """Return the diary entries of the logged-in user ordered by creation date."""
        return DiaryEntry.objects.filter(user=self.request.user).order_by("-created_at")