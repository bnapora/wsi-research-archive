SELECT  "Slides".id
,accession
,"imageGuid"
,"Slides".label
,"Slides".block
,"Slides"."slideNumber"
,"CDR_CaseSpecimens".label as case_specimen_label
,"CDR_CaseSpecimens".description as case_specimen_description
,date_trunc('day', "Slides"."createdAt")::date as "createdAt"
-- ,'Pop_' || accession || '_' || "Slides".label || "Slides".block || '-' || "Slides"."slideNumber" ||'.svs' as new_slide_name
,'D:\PathologyV2\' || "imageGuid" ||'\' || "imageGuid" || '.svs' || ',Pop_' || accession || '\Pop_' || accession || '_' || "Slides".label || "Slides".block || '-' || "Slides"."slideNumber" ||'.svs' as "source, destination"

FROM "CDR"."Slides"
LEFT JOIN "public"."CDR_CaseSpecimens" ON "CDR_CaseSpecimens".id = "Slides"."caseSpecimenId"
WHERE "accession" = 'TGJ22-0238-0000102'
ORDER BY "Slides"."createdAt" asc
LIMIT 1000