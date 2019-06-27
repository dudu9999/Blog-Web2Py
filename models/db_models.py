# -*- coding: utf-8 -*-


db.define_table(
	'posts'
	,Field('author','reference auth_user', default=auth.user_id)
	,Field('titulo','string',notnull=True)
	,Field('imagem','upload',notnull=True)
	,Field('postagem','text',notnull=True)
	,Field('criado_em','datetime',default=request.now)
	,Field('data_modificacao','datetime',default=request.now)
	,format="%(titulo)s"
	)

db.posts.author.writable=False

db.define_table(
	'comments'
	,Field('author','reference auth_user')
	,Field('post_id','reference posts')
	,Field('criado_em','datetime',default=request.now)
	,Field('re_coment','reference comments')
	,Field('comentario','text')
	)

