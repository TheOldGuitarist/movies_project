from django.shortcuts import render, redirect, get_object_or_404
from .models import Director, Movie
from .forms import DirectorForm, MovieForm

# -------- DASHBOARD --------
def dashboard(request):
    """Vista principal: muestra directores y películas en una sola página"""
    directors = Director.objects.all()
    movies = Movie.objects.select_related('fk_director').all()

    director_form = DirectorForm()
    movie_form = MovieForm()

    # Procesar formularios de agregar
    if request.method == 'POST':
        if 'add_director' in request.POST:
            director_form = DirectorForm(request.POST)
            if director_form.is_valid():
                director_form.save()
                return redirect('dashboard')

        elif 'add_movie' in request.POST:
            movie_form = MovieForm(request.POST)
            if movie_form.is_valid():
                movie_form.save()
                return redirect('dashboard')

    return render(request, 'dashboard.html', {
        'directors': directors,
        'movies': movies,
        'director_form': director_form,
        'movie_form': movie_form
    })


# -------- DIRECTORES --------
def edit_director(request, id):
    """Editar un director desde modal"""
    director = get_object_or_404(Director, id=id)
    if request.method == 'POST':
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
    return redirect('dashboard')


def delete_director(request, id):
    """Eliminar un director"""
    director = get_object_or_404(Director, id=id)
    director.delete()
    return redirect('dashboard')


# -------- PELÍCULAS --------
def edit_movie(request, id):
    """Editar una película desde modal"""
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
    return redirect('dashboard')


def delete_movie(request, id):
    """Eliminar una película"""
    movie = get_object_or_404(Movie, id=id)
    movie.delete()
    return redirect('dashboard')
