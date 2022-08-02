select accession
,"Slides".label || "Slides".block as block_label
,count(accession) AS count
-- ,sum(CAST("Slides"."slideNumber" AS integer)) as sumcheck
-- ,"slideIdentifier"
-- ,block
-- ,"imageGuid"
-- ,"specimenIdentifier"
,"isImageAvailable"
-- ,"createdAt"
-- ,"updatedAt"
-- ,"deletedAt"
-- ,"slideNumber"
-- ,tags
-- ,"tagsUpdatedAt"
-- ,"caseSpecimenId"
,date_trunc('day', "createdAt")::date
from "CDR"."Slides"
where date_trunc('day', "createdAt")::date >= '2022-6-02' 
AND "CDR"."Slides"."imageGuid" IS NOT NULL
AND "CDR"."Slides"."slideNumber" IS NOT NULL
GROUP BY accession
,"Slides".label || "Slides".block
,"isImageAvailable"
,date_trunc('day', "createdAt")::date
HAVING count(accession) > 1 AND sum(CAST("Slides"."slideNumber" AS integer)) > 2
ORDER BY accession desc
LIMIT 1000