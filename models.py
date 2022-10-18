from jsonmodels import models, fields, errors, validators


class Collection(models.Base):
    id = fields.StringField()
    unitid_ssm = fields.ListField(str)
    title_ssm = fields.ListField(str)
    #title_teim = fields.ListField(str)
    unitdate_ssm = fields.ListField(str)
    #unitdate_bulk_ssim
    #unitdate_inclusive_ssm
    #unitdate_other_ssim
    extent_ssm = fields.ListField(str)
    language_ssm = fields.ListField(str)
    abstract_ssm = fields.ListField(str)
    collection_ssm = fields.ListField(str)
    #collection_sim
    #collection_ssi
    #collection_title_tesim
    accessrestrict_ssm = fields.ListField(str)
    scopecontent_ssm = fields.ListField(str)
    repository_ssm = fields.ListField(str)
    #repository_sim
    ead_ssi = fields.ListField(str)
    level_ssm = fields.ListField(str)
    has_online_content_ssm = fields.ListField(str)
    normalized_title_ssm = fields.ListField(str)
    normalized_date_ssm = fields.ListField(str)
    names_coll_ssim = fields.ListField(str)
    accruals_ssm = fields.ListField(str)
    altformavail_ssm = fields.ListField(str)
    appraisal_ssm = fields.ListField(str)
    arrangement_ssm = fields.ListField(str)
    bibliography_ssm = fields.ListField(str)
    bioghist_ssm = fields.ListField(str)
    custodhist_ssm = fields.ListField(str)
    fileplan_ssm = fields.ListField(str)
    note_ssm = fields.ListField(str)
    odd_ssm = fields.ListField(str)
    originalsloc_ssm = fields.ListField(str)
    otherfindaid_ssm = fields.ListField(str)
    phystech_ssm = fields.ListField(str)
    prefercite_ssm = fields.ListField(str)
    processinfo_ssm = fields.ListField(str)
    relatedmaterial_ssm = fields.ListField(str)
    separatedmaterial_ssm = fields.ListField(str)
    userestrict_ssm = fields.ListField(str)
    materialspec_ssm = fields.ListField(str)
    physloc_ssm = fields.ListField(str)

class Component(Collection):
    parent_ssim = fields.ListField(str)
    parent_unittitles_ssm = fields.ListField(str)
    component_level_isim = fields.ListField(int)
    collection_unitid_ssm = fields.ListField(str)
    child_component_count_isim = fields.ListField(int)
    parent_access_restrict_ssm = fields.ListField(str)
    parent_access_terms_ssm = fields.ListField(str)
    containers_ssim = fields.ListField(str)
    title_filing_si = fields.StringField()