# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
	return dict()

@auth.requires_login()
def posts():
	grid = SQLFORM.smartgrid(
		db.posts
		,paginate=20
		,csv=False
		,orderby=~db.posts.data_modificacao
		)
	return dict(grid=grid)