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
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5509873727776) as [Age]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5218627745512) as [Albumin]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 4823167401696) as [bmis]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504785754704) as [Cause]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504787942904) as [CVD]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504786623420) as [CHF]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504786102404) as [COPD]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504787630456) as [CAD]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504768310524) as [DateAccepted]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504768118632) as [DateFirstRRT]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504784907236) as [DateReferredtoTxCtr]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504788700804) as [Employed]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504788923876) as [EthnicGroup]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 4407445162912) as [Height]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504788179224) as [HT]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504786848428) as [Insulin]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504786483980) as [Nonambulatory]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5150930730124) as [PVD]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5510221126384) as [Survival_Probability_at_5yrs]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5504788562924) as [SmokerCurrent]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5508852774208) as [Survival_Factor]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5510223200268) as [Survival_Probability_at_1yr]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 5510223002948) as [Survival_Probability_at_3yrs]
,(select ato.value from wdhb_cdsswe.dbo.atomicobservation ato where obs.observation_report_id = ato.observation_report_id and ato.datatype_id = 4407444765224) as [Weight]
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
tt.tasktype_id = 5529178639884