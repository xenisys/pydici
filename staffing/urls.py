# -*- coding: UTF-8 -*-
"""URL dispatcher for staffing module
@author: Sébastien Renard (sebastien.renard@digitalfox.org)
@license: AGPL v3 or newer (http://www.gnu.org/licenses/agpl-3.0.html)
"""

from django.conf.urls import url
import staffing.views as v
import staffing.tables as t

staffing_urls = [url(r'^pdcreview/?$', v.pdc_review, name='pdcreview-index'),
                 url(r'^pdcreview/(?P<year>\d+)/(?P<month>\d+)/?$', v.pdc_review, name='pdcreview'),
                 url(r'^production-report/?$', v.prod_report, name='prod_report'),
                 url(r'^production-report/(?P<year>\d+)/(?P<month>\d+)/?$', v.prod_report, name='prod_report'),
                 url(r'^fixed-price-mission-report/?$', v.fixed_price_missions_report, name="fixed_price_missions_report"),
                 url(r'^mission/$', v.missions, name='missions'),
                 url(r'^mission/all', v.missions, {'onlyActive': False}, 'all-missions'),
                 url(r'^mission/(?P<mission_id>\d+)/$', v.mission_home, name="mission_home"),
                 url(r'^mission/update/$', v.mission_update, name="mission_inline_update"),
                 url(r'^mission/(?P<pk>\d+)/update$', v.MissionUpdate.as_view(), name='mission_update'),
                 url(r'^mission/newfromdeal/(?P<lead_id>\d+)/$', v.create_new_mission_from_lead, name="create_new_mission_from_lead"),
                 url(r'^forecast/mission/(?P<mission_id>\d+)/$', v.mission_staffing, {"form_mode": "manual"}, name="manual_mission_staffing"),
                 url(r'^forecast/automatic/mission/(?P<mission_id>\d+)/$',  v.mission_staffing, {"form_mode": "automatic"}, name="automatic_mission_staffing"),
                 url(r'^mission/(?P<mission_id>\d+)/deactivate$', v.deactivate_mission, name="deactivate_mission"),
                 url(r'^forecast/consultant/(?P<consultant_id>\d+)/$', v.consultant_staffing, name="consultant_staffing"),
                 url(r'^forecast/mass/$', v.mass_staffing, name="mass_staffing"),
                 url(r'^timesheet/global/?$', v.all_timesheet, name="all_timesheet"),
                 url(r'^timesheet/global/(?P<year>\d+)/(?P<month>\d+)/?$', v.all_timesheet, name="all_timesheet"),
                 url(r'^timesheet/detailed/?$', v.detailed_csv_timesheet, name="detailed_csv_timesheet"),
                 url(r'^timesheet/detailed/(?P<year>\d+)/(?P<month>\d+)/?$', v.detailed_csv_timesheet, name="detailed_csv_timesheet"),
                 url(r'^timesheet/consultant/(?P<consultant_id>\d+)/$', v.consultant_timesheet, name="consultant_timesheet"),
                 url(r'^timesheet/consultant/(?P<consultant_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/?$', v.consultant_timesheet, name="consultant_timesheet"),
                 url(r'^timesheet/consultant/(?P<consultant_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<week>\d+)/?$', v.consultant_timesheet, name="consultant_timesheet"),
                 url(r'^timesheet/mission/(?P<mission_id>\d+)/$', v.mission_timesheet, name="mission_timesheet"),
                 url(r'^holidays_planning/?$', v.holidays_planning, name="holidays_planning"),
                 url(r'^holidays_planning/(?P<year>\d+)/(?P<month>\d+)/?$', v.holidays_planning, name="holidays_planning"),
                 url(r'^holidays_report/(?P<year>\d+)$', v.missions_report, {"nature": "HOLIDAYS"}, name="holidays-pivotable-year"),
                 url(r'^holidays_report/?$', v.missions_report, {"nature": "HOLIDAYS"}, name="holidays-pivotable"),
                 url(r'^holidays_report/all$', v.missions_report, {"nature": "HOLIDAYS", "year": "all"}, name="holidays-pivotable-all"),
                 url(r'^non-prod_report/(?P<year>\d+)$', v.missions_report, {"nature": "NONPROD"}, name="nonprod-pivotable-year"),
                 url(r'^non-prod_report/?$', v.missions_report, {"nature": "NONPROD"}, name="nonprod-pivotable"),
                 url(r'^non-prod_report/all$', v.missions_report, {"nature": "NONPROD", "year": "all"}, name="nonprod-pivotable-all"),
                 url(r'^contacts/mission/(?P<mission_id>\d+)/$', v.mission_contacts, name="mission_contacts"),
                 url(r'^rate/?$', v.mission_consultant_rate, name="mission_consultant_rate"),
                 url(r'^pdc-detail/(?P<consultant_id>\d+)/(?P<staffing_date>\d+)/?$', v.pdc_detail, name="pdc_detail"),
                 url(r'^datatable/all-missions/data/$', t.MissionsTableDT.as_view(), name='all_mission_table_DT'),
                 url(r'^datatable/active-missions/data/$', t.ActiveMissionsTableDT.as_view(), name='active_mission_table_DT'),
                 url(r'^datatable/clientcompany-missions/(?P<clientcompany_id>\d+)/data/$', t.ClientCompanyActiveMissionsTablesDT.as_view(), name='client_company_mission_table_DT'),
                 url(r'^turnover-pivotable/$', v.turnover_pivotable, name="turnover_pivotable"),
                 url(r'^turnover-pivotable/(?P<year>\d+)$', v.turnover_pivotable, name="turnover_pivotable_year"),
                 url(r'^turnover-pivotable/all$', v.turnover_pivotable, {"year": "all"}, name="turnover_pivotable_all"),
                 url(r'^lunch-tickets-pivotable$', v.lunch_tickets_pivotable, name="lunch_tickets_pivotable"),
                 url(r'^rates_report/?$', v.rate_objective_report, name="rate_objective_report"),
                 url(r'^graph/timesheet-rates/?$', v.graph_timesheet_rates_bar, name="graph_timesheet_rates_bar"),
                 url(r'^graph/timesheet-rates/team/(?P<team_id>\d+)$', v.graph_timesheet_rates_bar, name="graph_timesheet_rates_bar"),
                 url(r'^graph/profile-rates/?$', v.graph_profile_rates, name="graph_profile_rates"),
                 url(r'^graph/profile-rates/team/(?P<team_id>\d+)$', v.graph_profile_rates, name="graph_profile_rates"),
                 url(r'^graph/rates/consultant/(?P<consultant_id>\d+)', v.graph_consultant_rates, name="graph_consultant_rates"),
                ]
