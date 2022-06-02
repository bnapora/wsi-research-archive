select  "Slides".id
,"Slides"."caseItemId"
-- ,"levelId"

,accession
,"Slides".label
,block
,"slideNumber"
,"CDR_CaseSpecimens".label as specimen_label
,"CDR_CaseSpecimens".description as specimen_description
,"imageGuid"
-- ,"specimenIdentifier"
-- ,"isImageAvailable"
-- ,"isImageArchived"
-- ,"isAssetAvailable"
,"Slides"."createdAt"
,"Slides"."updatedAt"
,"Slides"."deletedAt"

,"Slides".tags
,"Slides"."tagsUpdatedAt"
,"Slides"."caseSpecimenId"
,"CDR_CaseSpecimens".id

FROM "CDR"."Slides"
LEFT JOIN "public"."CDR_CaseSpecimens" ON "CDR_CaseSpecimens".id = "Slides"."caseSpecimenId"
where "Slides"."createdAt" > '2021-11-18' AND "slideNumber" > '3'
ORDER BY "createdAt", accession asc
LIMIT 1000