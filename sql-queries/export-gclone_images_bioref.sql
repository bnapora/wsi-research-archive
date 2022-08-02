-- DECLARE created_date TIMESTAMP := "2022-6-02"

SELECT 
"Slides"."imageGuid"
,'/' || "Slides"."imageGuid" ||'/' || "Slides"."imageGuid" || '.svs'  as "src_image_path"
,"Slides".id 
,"Slides"."caseItemId"
,accession
,"Slides".label
,"Slides".block
,"Slides"."slideNumber"
,"CDR_CaseSpecimens".label as case_specimen_label
,"CDR_CaseSpecimens".description as case_specimen_description
,"Stains"."name" as stain_name
,date_trunc('day', "Slides"."createdAt")::date as "createdAt"
-- -- ,'Pop_' || accession || '_' || "Slides".label || "Slides".block || '-' || "Slides"."slideNumber" ||'.svs' as new_slide_name
-- ,'D:\PathologyV2\' || "imageGuid" ||'\' || "imageGuid" || '.svs' || ',Pop_' || accession || '\Pop_' || accession || '_' || "Slides".label || "Slides".block || '-' || "Slides"."slideNumber" ||'.svs' as "source, destination"

FROM "CDR"."Slides"
LEFT JOIN "public"."CDR_CaseSpecimens" ON "CDR_CaseSpecimens".id = "Slides"."caseSpecimenId"
LEFT JOIN "CDR"."SlideStains" ON "CDR"."Slides".id = "SlideStains"."slideId"
LEFT JOIN "CDR"."Stains" ON "CDR"."SlideStains"."stainId" = "Stains"."id"
WHERE "accession" IN (select accession from "CDR"."Slides" 
                        where "CDR"."Slides"."imageGuid" IS NOT NULL 
                            AND "createdAt" >= '2022-7-26' 
                        GROUP BY accession, "Slides".label || "Slides".block 
                        HAVING count(accession) > 2 
                            AND sum(CAST("Slides"."slideNumber" AS integer)) > 2 LIMIT 1000) 
AND "CDR"."Slides"."createdAt" >= '2022-7-26' 
AND "CDR"."Slides"."imageGuid" IS NOT NULL
AND "CDR"."Slides"."slideNumber" IS NOT NULL
-- AND "CDR"."Slides"."slideNumber" = '1'
ORDER BY "Slides"."accession", "Slides"."label", "Slides"."block", "Slides"."slideNumber" desc
