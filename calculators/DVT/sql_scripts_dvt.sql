SELECT DISTINCT b.NMPI,b.TESTDATE,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTWELLS') as DVTWELLS,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTAltDiag') as  DVTAltDiag,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTBed') as DVTBed,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTCircum') as DVTCircum,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTCollateral') as DVTCollateral,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTHist') as DVTHist,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTImmob') as DVTImmob,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTMalig') as DVTMalig,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTOedema') as DVTOedema,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTRisk') as DVTRisk,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTSwollen') as DVTSwollen,
(SELECT DISTINCT a.[RESULTTEXT] from [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] a where a.NMPI=b.NMPI and a.TESTDATE=b.TESTDATE and a.FIELDID='DVTTender') as DVTTender
FROM  [WDHB_RAD_LAB].[eclair].[tDVTWELLS_Dataset] b
order by NMPI;
