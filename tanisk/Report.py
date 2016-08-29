class Report:
    report_num=0
    def __init__(self,report_ty,report_nm,):
        self.report_type=report_ty
        self.report_name=report_nm
        Report.report_num=+1
    def report_info(self):
        pass

class SalReport(Report):
    def get_report_type(self,Report):
        return self.report_type
    def get_report_name(self,Report):
        return self.report_name
class ExpanceReport(Report):
    def get_report_type(self,Report):
        return self.report_type
    def get_report_name(self,Report):
        return self.report_name
class ItReport(Report):
    def get_report_type(self,Report):
        return self.report_type
    def get_report_name(self,Report):
        return self.report_name
    
class Application:

