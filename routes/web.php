<?php

use App\Models\Product;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::middleware('tenant')->get('a', function () {
    return 'You are in ' . app('currentTenant')->name;
});

Route::middleware('tenant')->group(function () {
    Route::get('/products', function () {
        return Product::all();
    });

    Route::get('/seed', function () {
        $t = app('currentTenant');
        Product::create([
            'name' => $t->name . ' Shirt',
            'sku' => 'SH-' . rand(100, 999),
            'price' => 49900,
        ]);
        return 'ok';
    });
});
