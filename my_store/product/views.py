from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Review


def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )

            return redirect('product:detail', slug=slug)

    return render(request, 'product/detail.html', {'product': product})

def hx_product_list(request):
    products = Product.objects.all()

    return render(request, 'product/partials/list_product.html', {
        'products': products,
    })