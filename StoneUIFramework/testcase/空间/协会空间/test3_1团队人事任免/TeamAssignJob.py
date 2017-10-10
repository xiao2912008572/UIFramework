__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log
from StoneUIFramework.config.globalparam import GlobalParam


# 团队人事任免
class TeamAssignJob:
    def __init__(self):
        # 初始化测试数据
        d = DataInfo("space.xls")  # 创建DataInfo()对象
        self.spacename = d.cell("test003-团队", 4, 1)  # 协会测试123
        self.AdministratorLoc = int(d.cell("test003-团队", 4, 2))  # 管理员编辑
        self.SalespersonLoc = int(d.cell("test003-团队", 4, 2))  # 助理编辑
        self.AssistantLoc = int(d.cell("test003-团队", 4, 4))  # 理事编辑
        self.AdmNum = int(d.cell("test003-团队", 4, 5))  # 管理员人数
        self.SalNum = int(d.cell("test003-团队", 4, 6))  # 助理人数
        self.AssNum = int(d.cell("test003-团队", 4, 7))  # 理事人数
        self.Name = d.cell("test003-团队", 2, 8)  # 肖静远
        self.Director = int(d.cell("test003-团队", 4, 9))  # 秘书处
        self.Marketing = int(d.cell("test003-团队", 4, 10))  # 会员组
        self.HR = int(d.cell("test003-团队", 4, 11))  # 财务处
        # 创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 创建日志模块
        self.log = Log(self.logfile)

    def teamAssignJob(self, driver):
        # 创建工具类
        tools = Tools(driver)  # tools工具
        # 创建_OrgSpaceTeamHandle公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(1)
        try:
            self.log.info('------START:test3_1团队人事任免.TeamAssignJob.py------')
            # 1.空间首页
            # handle.Kjlb_click()
            # tools.getScreenShot(screen_path,"空间首页")
            # 2.选择空间:测试空间123
            # handle.Kjlb_browseascspaceByName_click(self.spacename)
            # 3.右上角:菜单栏选择团队
            handle.Kjlb_browseascspace_menu_click()  # 右上角菜单
            self.log.info('点击右上角菜单')
            handle.Kjlb_browseascspace_menu_team_click()  # 点击团队
            self.log.info('点击团队')
            # 4.团队编辑，编辑各职位人数
            # 4.1 管理员人数:2人
            handle.Kjlb_browseascspace_menu_team_teamedit_click()  # 点击编辑
            self.log.info('点击编辑')
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.AdministratorLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[0].click()
            self.log.info('编辑管理员人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(self.AdmNum)  # 2人
            self.log.info('设置管理员人数：%s' % self.AdmNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')
            # 4.2 销售员人数:3人
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.SalespersonLoc)#编辑销售员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[1].click()
            self.log.info('编辑销售员人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(self.SalNum)  # 3人
            self.log.info('设置销售员人数：%s' % self.SalNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')
            # 4.3 行政助理人数:4人
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.AssistantLoc)#编辑助理人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[3].click()
            self.log.info('编辑助理人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(self.AssNum)  # 4人
            self.log.info('设置助理人数：%s' % self.AssNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')
            # 5.检查各职位人数是否保存生效
            # 5.1 检查管理员人数编辑是否生效
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.AdministratorLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[0].click()
            self.log.info('点击编辑管理员人数')
            AdmNumm = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前管理员人数：{0}'.format(AdmNumm))
            self.log.info('预期管理员人数：{0}'.format(self.AdmNum))
            assert self.AdmNum == AdmNumm, "编辑管理员人数保存后未生效"
            self.log.info('检查管理员人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')
            # 5.2 检查助理人数编辑是否生效
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.SalespersonLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[1].click()
            self.log.info('点击编辑助理人数')
            SalNum = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前助理人数：{0}'.format(SalNum))
            self.log.info('预期助理人数：{0}'.format(self.SalNum))
            assert self.SalNum == SalNum, "编辑助理人数保存后未生效"
            self.log.info('检查助理人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')
            # 5.3 检查常务理事人数编辑是否生效
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.AssistantLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[3].click()
            self.log.info('点击常务理事人数')
            AssNum = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前常务理事人数：{0}'.format(AssNum))
            self.log.info('预期常务理事人数：{0}'.format(self.AssNum))
            assert self.AssNum == AssNum, "编辑行政助理人数后未生效"
            self.log.info('检查常务理事人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')
            # 6.关闭编辑
            handle.Kjlb_browseascspace_menu_team_teamedit_click()  # 点击编辑按钮
            self.log.info('点击编辑按钮')
            # 7.菜单栏-人事任免
            handle.Kjlb_browseascspace_menu_team_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_click()  # 点击人事任免
            self.log.info('点击人事任免')
            if driver.find_elements_by_id("com.yunlu6.stone:id/removaljobs_name") != []:  # 列表是否为空
                listT = handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact()
                for i in range(len(listT)):  # 遍历列表
                    if handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact()[i].text == self.Name:  # 再判断是否该人已被任免
                        handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
                        self.log.info('判断该人是否已被任免')
                        self.log.info('点击待任免联系人')
                        handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete_click()  # 点击移除
                        self.log.info('点击移除')
                    else:
                        pass
            else:
                pass
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_click()  # 点击人事任免新增按钮
            self.log.info('点击人事任免新增按钮')
            # 8.搜索姓名:肖静远
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_search_sendkeys(self.Name)  # 搜索关键字
            self.log.info('搜索人脉关键字：%s' % self.Name)
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtn_click()  # 点击搜索
            self.log.info('点击搜索')
            # 9.点击搜索的结果,添加
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_choose_click(0)  # 勾选
            self.log.info('勾选')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm_click()  # 添加
            self.log.info('添加')
            # 10.待任免列表点击联系人-任免职位-勾选-返回
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
            self.log.info('点击待任免联系人')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_department_click(self.Director)  # 秘书处
            self.log.info('点击秘书处')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobname_click(1)  # 秘书长
            self.log.info('勾选秘书长')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_confrim_click()  # 勾选
            self.log.info('勾选')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_back_click()  # 返回
            self.log.info('返回')
            name = driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_name")[1].text  # 获取秘书长姓名
            assert self.Name == name, "秘书长任免失败"
            self.log.info('判断该人脉秘书长职位是否任免成功')
            # 11.移除任免,还原
            handle.Kjlb_browseascspace_menu_team_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_click()  # 点击人事任免
            self.log.info('点击人事任免')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
            self.log.info('待任免联系人')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete_click()  # 点击移除
            self.log.info('点击移除')
            self.log.info('------END:test3_1团队人事任免.TeamAssignJob.py------')
        except Exception as err:
            self.log.error("Error Information TeamAssignJob Inside : %s" % err)
            raise err
