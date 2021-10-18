from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for item in positions:
            new_stock_product = StockProduct.objects.create(product=item['product'], stock=stock, quantity=item['quantity'], price=item['price'])
            stock.positions.add(new_stock_product)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        print(type(stock))
        for item in positions:
            sp = StockProduct.objects.update_or_create(product=item['product'], stock=stock, quantity=item['quantity'], price=item['price'])
        return stock

    class Meta:
        model = Stock
        fields = ["address", "positions"]
