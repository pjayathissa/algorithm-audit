SELECT
pat.NHI_number,
tr.taskrequest_id,
obs.observation_report_id,
pp.stream_id,
'R' + pp.stream_id as referralencounter,
pp.patient_programme_id,
tr.due_date,
tt.display_name,
obs.date_completed,
case
when obs.observation_report_status = 'F' then 'Completed'
when obs.observation_report_status = 'S' then 'In Progress'
when obs.observation_report_status = 'X' then 'Declined'
when obs.observation_report_status = 'A' then 'Finalised' end as status,
obs.provider_given_name + ' ' + obs.provider_family_name as prof_carer
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164484362684) as [BergOutcome]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 4516272358684) as [Form_Spacer1]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 4516408397332) as [Form_Spacer2]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164413226308) as [BergItem9]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164413849496) as [BergItem12]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164412962556) as [BergItem8]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164173534368) as [BergItem1]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164177493868) as [BergItem3]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164414237184) as [BergItem14]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164177747056) as [BergItem4]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164177287868) as [BergItem2]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164414104496) as [BergItem13]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164180512056) as [BergItem6]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164412462996) as [BergItem7]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164414397184) as [Total_Score]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164178133120) as [BergItem5]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164413607868) as [BergItem11]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 6164413499996) as [BergItem10]
FROM
wdhb_cdsswe.dbo.TaskRequest tr with (nolock),
wdhb_cdsswe.dbo.PatientProgramme pp with (nolock),
wdhb_cdsswe.dbo.Patient pat with (nolock),
wdhb_cdsswe.dbo.TaskType tt with (nolock),
wdhb_cdsswe.dbo.ObservationReport obs with (nolock)
WHERE
tr.patient_programme_id = pp.patient_programme_id and
pp.patient_id = pat.patient_id and
tr.tasktype_id = tt.tasktype_id and
tr.taskrequest_id = obs.taskrequest_id and
obs.record_status = 'A' AND
obs.observation_report_status in ('A','F','S') AND
tt.tasktype_id in (6175472932440,6175464762376,6175472153500,6175468870312)