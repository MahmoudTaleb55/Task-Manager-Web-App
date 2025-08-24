from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, TaskSearchForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    search_form = TaskSearchForm(request.GET or None)
    
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search')
        category = search_form.cleaned_data.get('category')
        priority = search_form.cleaned_data.get('priority')
        status = search_form.cleaned_data.get('status')
        
        # Apply search filters
        if search_query:
            tasks = tasks.filter(
                Q(title__icontains=search_query) |
                Q(category__icontains=search_query)
            )
        
        if category:
            tasks = tasks.filter(category__icontains=category)
        
        if priority:
            tasks = tasks.filter(priority=priority)
        
        if status:
            if status == 'completed':
                tasks = tasks.filter(status=True)
            elif status == 'pending':
                tasks = tasks.filter(status=False)
    
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'search_form': search_form
    })

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Associate task with the logged-in user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Ensure user can only toggle their own tasks
    task.status = not task.status
    task.save()
    return redirect('task_list')

@login_required
def delete_all_tasks(request):
    if request.method == 'POST':
        Task.objects.filter(user=request.user).delete()  # Only delete tasks belonging to the logged-in user
    return redirect('task_list')
