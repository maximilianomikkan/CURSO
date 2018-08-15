from selenium.webdriver.common.by import By

# DEFINIENDO LOCATORS AND WEB ELEMENTS


# Defino clase Locator
class Locator (object):


# Top menu locator
        # LEFT
        _lnk_home_loc = (By.XPATH, "//*[@id='top-menu']/ul/li[1]/a")

        _lnk_my_page_loc = (By.XPATH, "//*[@id='top-menu']/ul/li[2]/a")

        _lnk_projects_loc = (By.XPATH, "//*[@id='top-menu']/ul/li[3]/a")

        _lnk_administration_loc = (By.XPATH, "//*[@id='top-menu']/ul/li[4]/a")

        _lnk_help_loc = (By.XPATH, "//*[@id='top-menu']/ul/li[5]/a")

        # RIGHT
        _lnk_user_loc = (By.XPATH, "//*[@id='loggedas']/a")

        _lnk_my_account_loc = (By.XPATH, "//*[@id='account']/ul/li[1]/a")

        _lnK_sign_out_loc = (By.XPATH, "//*[@id='account']/ul/li[2]/a")


# Header locator
        _tbs_search_loc = (By.ID, "q")

        _drp_jump_to_a_project_loc = (By.XPATH, "//*[@id='project-jump']/span")

        _tbs_projects_quick_search_loc = (By.ID, "projects-quick-search")

        _lnk_all_projects_loc = (By.XPATH, "//*[@id='project-jump']/div/div[3]/a")


# Projects Header locator
        _lnk_projects_projects_loc = (By.XPATH, "//*[@id='main-menu']/ul/li[1]/a")

        _lnk_projects_activity_loc = (By.XPATH, "//*[@id='main-menu']/ul/li[2]/a")

        _lnk_projects_issues_loc = (By.XPATH, "//*[@id='main-menu']/ul/li[3]/a")

        _lnk_projects_spent_time_loc = (By.XPATH, "//*[@id='main-menu']/ul/li[4]/a")

        _lnk_projects_gantt_loc = (By.XPATH, "//*[@id='main-menu']/ul/li[5]/a")

        _lnk_projects_calendar_loc = (By.XPATH, "//*[@id='main-menu']/ul/li[6]/a")

        _lnk_projects_news_loc = (By.XPATH, "//*[@id='main-menu']/ul/li[7]/a")


# Projects - Projects locator
        _tbl_projects_list_loc = (By.XPATH, "//*[@id='projects-index']//a")

        _chk_view_closed_projects_loc = (By.ID, "closed")

        _btn_new_project_loc = (By.XPATH, "//a[text()='New project']")


# Projects - Projects - New Project locator
        _txt_project_name_loc = (By.ID, "project_name")

        _txt_project_description_loc = (By.ID, "project_description")

        _txt_project_identifier_loc = (By.ID, "project_identifier")

        _txt_homepage_loc = (By.ID, "project_homepage")

        _chk_public_loc = (By.ID, "project_is_public")

        _sel_subproject_of_loc = (By.ID, "project_parent_id")

        _chk_inherit_members_loc = (By.ID, "project_inherit_members")

        _chk_modules_list_loc = (By.XPATH, "//legend[text()='Modules']/parent::fieldset//input[@type='checkbox']")
####### _chk_modules_list_loc = (By.XPATH, //*[@id='new_project']/fieldset[1]")

        _chk_trackers_list_loc = (By.XPATH, "//legend[text()='Trackers']/parent::fieldset//input[@type='checkbox']")

        _btn_create_loc = (By.NAME, "commit")

        _btn_create_and_continue_loc = (By.NAME, "continue")

        _lbl_message_loc = (By.ID, "flash_notice")

        _btn_save_loc = (By.XPATH, "//form[@id='edit_project_1']/input[@value='Save']")