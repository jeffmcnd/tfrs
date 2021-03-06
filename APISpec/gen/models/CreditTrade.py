"""
    REST API Documentation for the NRS TFRS Credit Trading Application

    The Transportation Fuels Reporting System is being designed to streamline compliance reporting for transportation fuel suppliers in accordance with the Renewable & Low Carbon Fuel Requirements Regulation.

    OpenAPI spec version: v1
        

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import datetime

from django.db import models
from django.utils import timezone
from .CreditTradeStatus import CreditTradeStatus
from .FuelSupplier import FuelSupplier
from .CreditTradeType import CreditTradeType
from .CreditTradeHistory import CreditTradeHistory

from auditable.models import Auditable

class CreditTrade(Auditable):	    
    creditTradeStatusFK = models.ForeignKey('CreditTradeStatus', related_name='CreditTradecreditTradeStatusFK')   
    initiatorFK = models.ForeignKey('FuelSupplier', related_name='CreditTradeinitiatorFK', blank=True, null=True)   
    respondentFK = models.ForeignKey('FuelSupplier', related_name='CreditTraderespondentFK')   
    creditTradeTypeFK = models.ForeignKey('CreditTradeType', related_name='CreditTradecreditTradeTypeFK')   
    numberOfCredits = models.IntegerField()   
    fairMarketValuePerCredit = models.CharField(blank=True, null=True, max_length=255)   
    tradeEffectiveDate = models.DateField(blank=True, null=True)   
    plainEnglishPhrase = models.CharField(max_length=2000)   
    historySet = models.ManyToManyField('CreditTradeHistory', related_name='CreditTradehistorySet', blank=True)   
    class Meta:
        db_table = 'CREDIT_TRADE'

