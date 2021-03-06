# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-21 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_auto_20170817_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='audit',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_audit_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='audit',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='audit',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_audit_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='credittrade',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='credittrade',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_credittrade_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='credittrade',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='credittrade',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_credittrade_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='credittradehistory',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradehistory',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_credittradehistory_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='credittradehistory',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradehistory',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_credittradehistory_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='credittradestatus',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradestatus',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_credittradestatus_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='credittradestatus',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradestatus',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_credittradestatus_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='credittradetype',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradetype',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_credittradetype_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='credittradetype',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradetype',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_credittradetype_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplier',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplier',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplier_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplier',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplier',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplier_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplieractionstype',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplieractionstype',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplieractionstype_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplieractionstype',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplieractionstype',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplieractionstype_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachment',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachment',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierattachment_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachment',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachment',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierattachment_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachmenttag',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachmenttag',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierattachmenttag_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachmenttag',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachmenttag',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierattachmenttag_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierbalance',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierbalance',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierbalance_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierbalance',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierbalance',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierbalance_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierccdata',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierccdata',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierccdata_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierccdata',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierccdata',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierccdata_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontact',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontact',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsuppliercontact_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontact',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontact',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsuppliercontact_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontactrole',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontactrole',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsuppliercontactrole_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontactrole',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontactrole',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsuppliercontactrole_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierhistory',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierhistory',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierhistory_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierhistory',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierhistory',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierhistory_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierstatus',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierstatus',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierstatus_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierstatus',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierstatus',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsupplierstatus_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliertype',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliertype',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsuppliertype_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliertype',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliertype',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_fuelsuppliertype_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='notification',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_notification_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='notification',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_notification_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_notificationevent_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_notificationevent_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_notificationtype_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_notificationtype_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_opportunity_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_opportunity_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='opportunityhistory',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunityhistory',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_opportunityhistory_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='opportunityhistory',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunityhistory',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_opportunityhistory_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='opportunitystatus',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunitystatus',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_opportunitystatus_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='opportunitystatus',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunitystatus',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_opportunitystatus_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='permission',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_permission_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='permission',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_permission_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='role',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_role_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='role',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_role_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_rolepermission_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_rolepermission_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_user_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_user_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='userfavourite',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userfavourite',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_userfavourite_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='userfavourite',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='userfavourite',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_userfavourite_UPDATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='userrole',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userrole',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_userrole_CREATE_USER', to='server.User'),
        ),
        migrations.AddField(
            model_name='userrole',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='userrole',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_userrole_UPDATE_USER', to='server.User'),
        ),
        migrations.AlterModelTable(
            name='audit',
            table='AUDIT',
        ),
        migrations.AlterModelTable(
            name='credittrade',
            table='CREDIT_TRADE',
        ),
        migrations.AlterModelTable(
            name='credittradehistory',
            table='CREDIT_TRADE_HISTORY',
        ),
        migrations.AlterModelTable(
            name='credittradestatus',
            table='CREDIT_TRADE_STATUS',
        ),
        migrations.AlterModelTable(
            name='credittradetype',
            table='CREDIT_TRADE_TYPE',
        ),
        migrations.AlterModelTable(
            name='fuelsupplier',
            table='FUEL_SUPPLIER',
        ),
        migrations.AlterModelTable(
            name='fuelsupplieractionstype',
            table='FUEL_SUPPLIER_ACTIONS_TYPE',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierattachment',
            table='FUEL_SUPPLIER_ATTACHMENT',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierattachmenttag',
            table='FUEL_SUPPLIER_ATTACHMENT_TAG',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierbalance',
            table='FUEL_SUPPLIER_BALANCE',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierccdata',
            table='FUEL_SUPPLIER_C_C_DATA',
        ),
        migrations.AlterModelTable(
            name='fuelsuppliercontact',
            table='FUEL_SUPPLIER_CONTACT',
        ),
        migrations.AlterModelTable(
            name='fuelsuppliercontactrole',
            table='FUEL_SUPPLIER_CONTACT_ROLE',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierhistory',
            table='FUEL_SUPPLIER_HISTORY',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierstatus',
            table='FUEL_SUPPLIER_STATUS',
        ),
        migrations.AlterModelTable(
            name='fuelsuppliertype',
            table='FUEL_SUPPLIER_TYPE',
        ),
        migrations.AlterModelTable(
            name='notification',
            table='NOTIFICATION',
        ),
        migrations.AlterModelTable(
            name='notificationevent',
            table='NOTIFICATION_EVENT',
        ),
        migrations.AlterModelTable(
            name='notificationtype',
            table='NOTIFICATION_TYPE',
        ),
        migrations.AlterModelTable(
            name='opportunity',
            table='OPPORTUNITY',
        ),
        migrations.AlterModelTable(
            name='opportunityhistory',
            table='OPPORTUNITY_HISTORY',
        ),
        migrations.AlterModelTable(
            name='opportunitystatus',
            table='OPPORTUNITY_STATUS',
        ),
        migrations.AlterModelTable(
            name='permission',
            table='PERMISSION',
        ),
        migrations.AlterModelTable(
            name='role',
            table='ROLE',
        ),
        migrations.AlterModelTable(
            name='rolepermission',
            table='ROLE_PERMISSION',
        ),
        migrations.AlterModelTable(
            name='user',
            table='USER',
        ),
        migrations.AlterModelTable(
            name='userfavourite',
            table='USER_FAVOURITE',
        ),
        migrations.AlterModelTable(
            name='userrole',
            table='USER_ROLE',
        ),
    ]
