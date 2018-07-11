# Generated by Django 2.0.4 on 2018-07-10 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='fkid_endereco',
        ),
        migrations.RemoveField(
            model_name='telefone',
            name='dt_alteracao',
        ),
        migrations.RemoveField(
            model_name='telefone',
            name='dt_cadastro',
        ),
        migrations.RemoveField(
            model_name='telefone',
            name='fkid_usuarioalteracao',
        ),
        migrations.AddField(
            model_name='endereco',
            name='fkid_pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Pessoa'),
        ),
        migrations.AddField(
            model_name='telefone',
            name='fkid_pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Pessoa'),
        ),
        migrations.AlterField(
            model_name='categoriaproduto',
            name='hide',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='categoriaproduto',
            name='nomecategoria',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='categoriaproduto',
            name='pkid_categoria',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cotacaocompra',
            name='dt_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cotacaocompra',
            name='dt_cadastro',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cotacaocompra',
            name='dt_cotacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cotacaocompra',
            name='dt_entrega',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cotacaocompra',
            name='formapamento',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='cotacaocompra',
            name='fornecedor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cotacaocompra',
            name='hide',
            field=models.TextField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cotacaocompra',
            name='pedidocompra_pkid_compra',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cotacaocompra',
            name='pkid_cotacao',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cotacaocompra',
            name='statuscotacao_pkid_status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='hide',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='logradouro',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='pkid_endereco',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='uf',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='dataentrega',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='dt_alteracao',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='dt_cadastro',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='fkid_usuario_alteracao',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='formaentrega',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='hide',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='nomecontarecebimento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='pkid_entrega',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='valorfrete',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formapagamento',
            name='dt_alteracao',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='formapagamento',
            name='dt_cadastro',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='formapagamento',
            name='fkid_usuario_alteracao',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='formapagamento',
            name='formapagamento',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='formapagamento',
            name='hide',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='formapagamento',
            name='pkid_formapag',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='formulaproduto',
            name='dt_alteracao',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='formulaproduto',
            name='dt_cadastro',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='formulaproduto',
            name='fkid_materiaprima',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='formulaproduto',
            name='fkid_produto',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='formulaproduto',
            name='fkid_usuario_alteracao',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='formulaproduto',
            name='hide',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='formulaproduto',
            name='pkid_formula',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='formulaproduto',
            name='tempomatucao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='descricaoproduto',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='dt_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='dt_cadastro',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='hide',
            field=models.TextField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='pedidocompra_pkid_compra',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='pkid_item',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='precounitario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='produto',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='statuscompra_pkid_status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='totalvenda',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='unidademedidacompra_pkid_unidademedida',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='itemcotacao',
            name='cotacaocompra_pkid_cotacao',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='itemcotacao',
            name='descricaoproduto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='itemcotacao',
            name='dt_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemcotacao',
            name='dt_cadastro',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemcotacao',
            name='hide',
            field=models.TextField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='itemcotacao',
            name='pkid_item',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='itemcotacao',
            name='precounitario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemcotacao',
            name='produto',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='itemcotacao',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemcotacao',
            name='totalvenda',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='descricaoproduto',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='dt_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='dt_cadastro',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='hide',
            field=models.TextField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='pkid_item',
            field=models.AutoField(max_length=45, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='precounitario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='produto',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='produtos_idprodutos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='totalvenda',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='unidademedida_pkid_unidademedida',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='usuario_pkid_usuario',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='linhavenda',
            name='dt_alteracao',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='linhavenda',
            name='dt_cadastro',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='linhavenda',
            name='fkid_produto',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='linhavenda',
            name='fkid_usuario_alteracao',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='linhavenda',
            name='hide',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='linhavenda',
            name='pedidovenda_pkid_venda',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='linhavenda',
            name='pkid_linhavenda',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='linhavenda',
            name='precovenda',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='linhavenda',
            name='quantidade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='materiaprima',
            name='dt_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='materiaprima',
            name='dt_cadastro',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='materiaprima',
            name='fkid_estoque',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='materiaprima',
            name='materiaprima',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='materiaprima',
            name='pkid_materiaprima',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='materiaprima',
            name='totalestoque',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='dt_alteracao',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='dt_cadastro',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='fkid_estoque',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='fkid_linhavenda1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='fkid_pedidofabri',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='fkid_produto',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='fkid_venda',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='hide',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='numentradas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='numsaidas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='pkid_movimentacao',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='tipomovimentacao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='cotacaocompra_pkid_cotacao',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='dt_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='dt_cadastro',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='dt_compra',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='dt_pagamento',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='dt_pedido',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='dt_recebimento',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='fornecedor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='hide',
            field=models.TextField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='pkid_compra',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='statuscompra_pkid_status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidofabricacao',
            name='dt_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidofabricacao',
            name='dt_cadastro',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidofabricacao',
            name='fkid_produto',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidofabricacao',
            name='fkid_statusfabricacao',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidofabricacao',
            name='fkid_usuario_alteracao',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidofabricacao',
            name='hide',
            field=models.TextField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pedidofabricacao',
            name='pkid_pedidofabri',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='dt_alteracao',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='dt_cadastro',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='dt_entrega',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='dt_pagamento',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='dt_pedido',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='fkid_entrega',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='fkid_formapag',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='fkid_pessoa',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='fkid_status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='fkid_usuario',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='fkid_usuarioalteracao',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='hide',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='pkid_venda',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='apelido_nomefantasia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cpf_cnpj',
            field=models.CharField(blank=True, max_length=19, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='dt_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='fkid_tipopessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Tipopessoa'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='genero',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='hide',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nomecompleto_razaosocial',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='pkid_pessoa',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='rg_ie',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='st_pessoajuridica',
            field=models.BooleanField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='produto',
            name='altura',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='codproduto',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='fkid_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Categoriaproduto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='fkid_unidademedida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Unidademedida'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='fotoproduto',
            field=models.FileField(blank=True, max_length=1000, null=True, upload_to='uploads/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='hide',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='largura',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='marca',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nomeproduto',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='produto',
            name='peso',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='produto',
            name='pkid_produto',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='produto',
            name='precocusto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='profundidade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='sabor',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='totalestoque',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='statuscompra',
            name='descricaostatus',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='statuscompra',
            name='pkid_status',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='statusfabricacao',
            name='descricaostatus',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='statusfabricacao',
            name='pkid_status',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='statusvenda',
            name='descricaostatus',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='statusvenda',
            name='pkid_status',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='ddd',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='ddi',
            field=models.CharField(default=55, max_length=2),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='hide',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='numero',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='pkid_telefone',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipopessoa',
            name='hide',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='tipopessoa',
            name='pkid_tipopessoa',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipopessoa',
            name='tipopessoa',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='unidademedida',
            name='hide',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='unidademedida',
            name='pkid_unidademedida',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unidademedida',
            name='unidademedida',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dt_alteracao',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dt_importacao',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='hide',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='login',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nomecompleto',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pkid_usuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='usuarioalteracao',
            name='dt_alteracao',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='usuarioalteracao',
            name='pkid_usuario_alteracao',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuarioalteracao',
            name='tipo_alteracao',
            field=models.TextField(),
        ),
        migrations.AlterModelTable(
            name='categoriaproduto',
            table=None,
        ),
        migrations.AlterModelTable(
            name='cotacaocompra',
            table=None,
        ),
        migrations.AlterModelTable(
            name='endereco',
            table=None,
        ),
        migrations.AlterModelTable(
            name='entrega',
            table=None,
        ),
        migrations.AlterModelTable(
            name='formapagamento',
            table=None,
        ),
        migrations.AlterModelTable(
            name='formulaproduto',
            table=None,
        ),
        migrations.AlterModelTable(
            name='itemcompra',
            table=None,
        ),
        migrations.AlterModelTable(
            name='itemcotacao',
            table=None,
        ),
        migrations.AlterModelTable(
            name='itemvenda',
            table=None,
        ),
        migrations.AlterModelTable(
            name='linhavenda',
            table=None,
        ),
        migrations.AlterModelTable(
            name='materiaprima',
            table=None,
        ),
        migrations.AlterModelTable(
            name='movimentacao',
            table=None,
        ),
        migrations.AlterModelTable(
            name='pedidocompra',
            table=None,
        ),
        migrations.AlterModelTable(
            name='pedidofabricacao',
            table=None,
        ),
        migrations.AlterModelTable(
            name='pedidovenda',
            table=None,
        ),
        migrations.AlterModelTable(
            name='pessoa',
            table=None,
        ),
        migrations.AlterModelTable(
            name='produto',
            table=None,
        ),
        migrations.AlterModelTable(
            name='statuscompra',
            table=None,
        ),
        migrations.AlterModelTable(
            name='statusfabricacao',
            table=None,
        ),
        migrations.AlterModelTable(
            name='statusvenda',
            table=None,
        ),
        migrations.AlterModelTable(
            name='telefone',
            table=None,
        ),
        migrations.AlterModelTable(
            name='tipopessoa',
            table=None,
        ),
        migrations.AlterModelTable(
            name='unidademedida',
            table=None,
        ),
        migrations.AlterModelTable(
            name='usuario',
            table=None,
        ),
        migrations.AlterModelTable(
            name='usuarioalteracao',
            table=None,
        ),
    ]