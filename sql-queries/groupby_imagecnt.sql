select accession
,count(accession) AS count
-- ,"slideIdentifier"
-- ,block
-- ,"imageGuid"
-- ,"specimenIdentifier"
,"isImageAvailable"
,"isImageArchived"
,"isAssetAvailable"
-- ,"createdAt"
-- ,"updatedAt"
-- ,"deletedAt"
-- ,"slideNumber"
-- ,tags
-- ,"tagsUpdatedAt"
-- ,"caseSpecimenId"
,date_trunc('day', "createdAt")::date
from "CDR"."Slides"
where date_trunc('day', "createdAt")::date >= '2021-11-15'
GROUP BY accession,"isImageAvailable"
,"isImageArchived"
,"isAssetAvailable"
,date_trunc('day', "createdAt")::date
ORDER BY count desc
LIMIT 1000