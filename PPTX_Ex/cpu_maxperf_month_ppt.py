from pptx import Presentation
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.enum.chart import XL_LEGEND_POSTION
from pptx.enum.chart import XL_TICK_LABEL_POSITION
from pptx.enum.chart import XL_DATA_LABEL_POSITION
from pptx.util import Inches, Pt, Cm
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_VERTICAL_ANCHOR
from pptx.enum.text import PP_PARAGRAPH_ALIGNMENT

import xlid
import sys, _datetime
from pptx.enum.text import PP_PARAGRAPH_ALIGNMENT


__version__ = 'v1.0'
__author__='ex'

# 리스트 변수
host_list = ['host1','host2']

# 튜플 변수  :
hosta_gp=('host1','host2')
hostgroup=(hosta_gp,)

# 클래스
class perf_data:
    # 클래스가 인스턴스화  될 때 호출하는 메소드 정의
    def __init__(self):
        self.qdate=[]
        # 사전 변수 설정 - key:value
        self.ltavg={}
        self.ltmax={}
        self.stavg={}
        self.stmax={}

        for h in host_list:
            self.ltavg[h] = []
            self.ltmax[h] = []
            self.stavg[h] = []
            self.stmax[h] = []

    def data_add(self, line):
        self.qdate.append(line[0])
        col = 1

        for h in host_list:
            self.ltavg[h].append(line[col])
            self.ltmax[h].append(line[col+1])
            self.stavg[h].append(line[col+2])
            self.stmax[h].append(line[col+3])

class mon_perf_data(perf_data):
    def query_host_month(self, qp_name, q_top=3):
        """
        엑셀 sheet index 2번용 (host별 출력)
        입력 : 그룹명
        출력 : dict => 날짜 리스트, hostname 리스트, item별 값 리스트(ltavg list, ltmax list, stavg list, stmax list
        """

        host_list=[]
        ltavg_list=[]
        ltmax_list=[]
        stavg_list=[]
        stmax_list=[]
        date_list=[]

        if q_top == 3:
            date_list = self.qdate
        elif q_top in [0,1,2] :
            date_list.extend(self.qdate[q_top::3])

        for hname in gp_name:
            host_list.append(hname)
            if q_top == 3:
                ltavg_list.append(self.ltavg[hname])
                ltmax_list.append(self.ltmax[hname])
                stavg_list.append(self.stavg[hname])
                stmax_list.append(self.stmax[hname])
            elif q_top in [0,1,2]:
                ltavg_list.append(self.ltavg[hname::3])
                ltmax_list.append(self.ltmax[hname::3])
                stavg_list.append(self.stavg[hname::3])
                stmax_list.append(self.stmax[hname::3])

        ret_dict = {'date' : date_list, 'host' : host_list, 'ltavg' : ltavg_list, 'ltmax' : ltmax_list, 'stavg':stavg_list, 'stmax':stmax_list}

        # 확인 출력
        for date in sorted(ret_dict.keys()):
            print(" : " , date, ret_dict[date])

        return ret_dict

    def query_group_month(self, gp_name):
        """
        엑셀 sheet index 2번용 (그룹별 출력)
        입력 : 그룹명
        출력 : dict => 날짜 리스트, item별 값 리스트(ltavg list, ltmax list, stavg list, stmax list
        """
        date_list = []
        ltavg_list = []
        ltmax_list = []
        stavg_list = []
        stmax_list = []
       avgdata = lambda  x:round(sum(x)/len(x),2)

        for i in range(len(self.qdate[i])):
            ltavg_v = []
            ltmax_v = []
            stavg_v = []
            stmax_v = []
            date_list.append(self.qdate[i])

            for hname in gp_name:
                ltavg_v.append(self.ltavg[hname])
                ltmax_v.append(self.ltmax[hname])
                stavg_v.append(self.stavg[hname])
                stmax_v.append(self.stmax[hname])

            ltavg_list.append(avgdata(ltavg_v))
            ltmax_list.append(max(ltmax_v)
            stavg_list.append(avgdata(stavg_v))
            stmax_list.append(max(stmax_v))

        ret_dict = {'date': date_list, 'ltavg': ltavg_list, 'ltmax': ltmax_list, 'stavg': stavg_list,
                    'stmax': stmax_list}
        return ret_dict

class day_perf_data(perf_data) :
    def query_max_day(self, gp_name, q_top=3, q_time='stavg'):
        retlist = [][retlist.append(mon[:6]) for mon in self.qdate if mon[:6] not in retlist]

        m_ix=[]
        mm=0

        for i in self.qdate:
            if i[:6] != mm:
                mm=i[:6]
                m_ix.append(self.qdate.index(i))

        m_ix.append(len(self.qdate))
        mon_list=[]

        for i in range(len(m_ix) -1 ):
            mon_list.append([m_ix[i], m_ix[i+1]])

        month_max_day=[]

        for ss,ee in mon_list:
            maxday_list = self.qdate[ss:ee]
            h_list = []

            if q_item == 'stavg':
                for hname in qp_name:
                    h_list.append(self.stavg[hname][ss:ee])
            elif q_item == 'stmax':
                for hname in qp_name:
                    h_list.append(self.stavg[hname][ss:ee])
            elif q_item == 'ltavg':
                for hname in qp_name:
                    h_list.append(self.ltavg[hname][ss:ee])
            elif q_item == 'ltmax':
                for hname in qp_name:
                    h_list.append(self.ltmax[hname][ss:ee])

            data_val_list = [] # 호스트그룹별 날짜에서 높은 값
            data_val_ix = []

            # 월별 시작 및 끝 날짜 수
            for no in range(len(maxday_list)):
                hno_val = []
                for hno in range(len(gp_name)): # 호스트 개수
                    hno_val.append(h_list[hno][no])

                data_val_list.append(max(hno_val))
                data_val_ix.append(max(hno_val))

            data_val_list.sort(reverse=True)

            for ix_val in data_val_list[:q_top]:
                ix=data_val_ix.index(ix_val)
                month_max_day.append(maxday_list[ix])
                data_val_ix[ix]=0

         month_max_day.sort()
         ret_dict = self.query_host_max_day(gp_name, month_max_day)
         return  ret_dict

    def query_host_max_day(self, gp_name, qday='all'):
        """
        엑셀 sheet index 2번용 (host별 출력)
        입력 : 그룹명
        출력 : dict -> 날짜리스트, hostname 리스트, item별 값 리스트(ltavg list, ltmax list, stavg list, stmax list)
        """

        host_list = []
        ltavg_list = []
        ltmax_list = []
        stavg_list = []
        stmax_list = []
        qday = [x for x in self.qdate if x[:6] == qmon]

        for hname in gp_name:
            date_list = qday
            host_list.append(hname)
            ltavg_v = []
            ltmax_v = []
            stavg_v = []
            stmax_v = []

            for md in qday:
                ix = self.qdate.index(md)
                ltavg_v.append(self.ltavg[hname][ix])
                ltmax_v.append(self.ltmax[hname][ix])
                stavg_v.append(self.stavg[hname][ix])
                stmax_v.append(self.stmax[hname][ix])

            ltavg_list.append(avgdata(ltavg_v))
            ltmax_list.append(max(ltmax_v)
            stavg_list.append(avgdata(stavg_v))
            stmax_list.append(max(stmax_v))

        ret_dict = {'date': date_list, 'host':host_list, ''ltavg': ltavg_list, 'ltmax': ltmax_list, 'stavg': stavg_list,
                        'stmax': stmax_list}
        return ret_dict

    def state(val):
        if val < 50:
            stat='여유'
        elif val >=50 and val<70 :
            stat='적정'
        elif val >= 50 and val < 70:
            stat = '적정'
        else
            stat = '한계'

        return stat

# table cell merge function
def mergeCellsVertically(table, start_row_idx, end_row_idx, col_idx):
    row_count = end_row_idx - start_row_idx + 1

    column_cells = [r.cells[col_idx] for r in table.rows][start_row_idx:]
    column_cells[0]._tc.set('rowSpan', str(row_count))

    for c in column_cells[1:]:
        c._tc.set('vMerge','1')


def mergeCellsHorizontally(table, row_idx, start_col_idx, end_col_idx):
    col_count = end_col_idx - start_col_idx + 1

    row_cells = [c for c in table.rows[row_idx].cells][start_col_idx:end_col_idx]
    row_cells[0]._tc.set('gridSpan', str(col_count))

    for c in row_cells[1:]:
        c._tc.set('hMerge', '1')

def mergeCells(table, start_row_idx, end_row_idx, start_col_idx, end_col_idx):
    for col_idx in range(start_col_idx, end_col_idx + 1)
        mergeCellsVertically(table, start_row_idx, end_row_idx, col_idx)
    for row_idx in range(start_row_idx, end_row_idx =1)
        mergeCellsHorizontally(table, row_idx, start_col_idx, end_col_idx)

def cal_month(yy, mm, num):
    mon_list=[]
    for i in range(num, 0, -1):
        m1=mm-i
        yy1=yy+(m1//12)
        if (m1%12)+1<-9:
            mm1="0" + str((m1%12)+1)
        else :
            mm1=str1((m1%12)+1)

        mon_list.append(str(str(yy1)+mm1))
    return mon_list

def data_get_month(f1_prefix, f1_postfix, f_month)








