from schema import  Vacancy, Resume, DodikSet, ExperienceItem, EducationItem
from typing import List


def expItem_to_str(e:ExperienceItem):
    if not e:
        return ""
    res = ""
    exp_dict = e.__dict__
    for field in exp_dict:
        res+=str(exp_dict[field]) + " "
    return res

def eduItem_to_str(e:EducationItem):
    if not e:
        return ""
    res = ""
    edu_dict = e.__dict__
    for field in edu_dict:
        res+=str(edu_dict[field]) + " "
    return res
 
def langItem_to_str(l:List[str]):
    if not l:
        return ""
    res = ""
    for lang in l:
        res+=lang + " "
    return res

def vacancy_to_str(v:Vacancy):
    if not v:
        return ""
    res = ""
    vac_dict = v.__dict__
    for field in vac_dict:
        res+=str(vac_dict[field]) + " "
    return res

def resume_to_str(r: Resume):
    if not r:
        return ""
    res = ""
    resu_dict = r.__dict__
    for field in resu_dict:
        if field=="experienceItem" and resu_dict[field]:
            for item in resu_dict[field]:
                res += expItem_to_str(item) + " "
        elif field=="educationItem" and resu_dict[field]:
            for item in resu_dict[field]:
                res += eduItem_to_str(item) + " "
        elif field=="languageItems":
            res += langItem_to_str(resu_dict[field]) + " "
        else:
            res += str(resu_dict[field]) + " "
    return res

def dset_to_dictList(d:List[DodikSet]):
    if not d:
        return []
    vacancy = ""
    resume = ""
    success = 0
    res = []
    for item in d:
        data_item = item.__dict__
        for key in data_item:
            if key == 'vacancy':
                vacancy = vacancy_to_str(data_item[key])
            elif key == 'failed_resumes':
                for resume in data_item[key]:
                    resume = resume_to_str(resume)
                    success = 0
                    res.append({"vacancy": vacancy, "resume":resume, "success":success})
            elif key == 'confirmed_resumes':
                for resume in data_item[key]:
                    resume = resume_to_str(resume)
                    success = 1
                    res.append({"vacancy": vacancy, "resume":resume, "success":success})
 
    return res


