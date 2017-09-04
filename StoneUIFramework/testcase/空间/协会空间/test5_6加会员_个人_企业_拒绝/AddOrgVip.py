__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.testcase.登录.test2_1退出登录.Loginout002_1 import Loginout
from StoneUIFramework.testcase.登录.test1_1登录.LoginA import LoginA

# +企业会员
class AddOrgVip:
    def __init__(self):  
        #初始化测试数据
        d = DataInfo("space.xls")  #创建DataInfo()对象
        self.vipname = d.cell("test007-会员",3,2)             #企业全称:明月俱乐部
        #创建Loginout和Login对象
        self.loginout = Loginout()
        self.login = LoginA()

    def addOrgVip(self, driver,orgname):
        '''+企业会员'''
        #创建_OrgSpaceTeamHandle公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(1)
        try:
        #1.空间首页
            # handle.Kjlb_click()
            # tools.getScreenShot(screen_path,"空间首页")
        #2.选择空间:测试空间123
            # handle.Kjlb_browseascspaceByName_click(self.spacename)
        #3.右上角:菜单栏选择+会员
            handle.Kjlb_browseascspace_menu_click()  #右上角菜单
            handle.Kjlb_browseascspace_menu_addvip_click()  #点击+会员
        #4.企业会员
            handle.Kjlb_browseascspace_menu_addvip_addcompany_click()
        #5.搜索栏搜索姓名添加
            handle.Kjlb_browseascspace_menu_addvip_addcompany_search_click()                        #点击搜索栏
            handle.Kjlb_browseascspace_menu_addvip_addcompany_search_search_sendkeys(orgname)       #搜索企业名称
            handle.Kjlb_browseascspace_menu_addvip_addcompany_searchbtn_click()                     #点击搜索
        #6.选择搜索结果，添加
            handle.Kjlb_browseascspace_menu_addvip_addcompany_choose_click(0)
            handle.Kjlb_browseascspace_menu_addvip_addcompany_confirm_click()
        #7.返回到空间主界面
            handle.Kjlb_browseascspace_back_click()
        except Exception as err:
            logging.error("Error_5_6 Information AddOrgVip Inside : %s" % err)
            raise err