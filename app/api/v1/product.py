# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/17.
"""
__author__ = 'Alimazing'

from app.libs.success_code import Success
from app.libs.redprint import RedPrint
from app.models.product import Product
from app.validators.params import Count, IDMustBePositiveInt

__author__ = 'Alimazing'

api = RedPrint(name='product', description='产品')


@api.route('/recent', methods=['GET'])
def get_recent():
	count = Count().validate_for_api().count.data
	products = Product.get_most_recent(count=count)
	return Success(products)


@api.route('/by_category', methods=['GET'])
def get_all_in_category():
	id = IDMustBePositiveInt().validate_for_api().id.data
	products = Product.get_product_by_category_id(id=id)
	return Success(products)


@api.route('/<int:id>', methods=['GET'])
def get_one(id):
	id = IDMustBePositiveInt().validate_for_api().id.data
	product = Product.get_product_detail(id=id)
	return Success(product)


@api.route('/<int:id>', methods=['DELETE'])
def delete_one(id):
	id = IDMustBePositiveInt().validate_for_api().id.data
	product = Product.get_product_detail(id=id)
	return Success(code=202, error_code=2, msg='删除成功')
