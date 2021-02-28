from django.db import models

class Building(models.Model):
    # Fields
    legal_dong_code = models.CharField(max_length=10, help_text='법정동코드')
    city_state_name = models.CharField(max_length=40, help_text='시도명')
    city_gungu_name = models.CharField(max_length=40, help_text='시군구명')
    legal_upmeundong_name = models.CharField(max_length=40, '법정읍면동명')
    legal_lee_name = models.CharField(max_length=40, '법정리명')
    is_mountain = models.BooleanField(help_text='산여부 (0:대지, 1:산)')
    jibun_bonbun_bunji = models.IntegerField(max_length=4, help_text='지번본번(번지)')
    jibun_boobun_ho = models.IntegerField(max_length=4, help_text='지번부번(호)')
    road_name_code = models.CharField(max_length=12, '도로명코드 (시군구코드(5) + 도로명번호(7))')
    road_name = models.CharField(max_length=80, '도로명')
    is_underground = models.CharField(max_length=1, '지하여부 (0:지상, 1:지하, 2:공중)')
    building_bonbun = models.IntegerField(max_length=5, help_text='건물본번')
    building_boobun = models.IntegerField(max_length=5, help_text='건물부번')
    construction_document_building_name = models.CharField(max_length=40, '건축물대장 건물명')
    detail_building_name = models.CharField(max_length=100, '상세건물명')
    building_management_no = models.CharField(max_length=25, help_text='건물관리번호')
    upmeondong_no = models.CharField(max_length=2, help_text='읍면동일련번호')
    administration_dong_no = models.CharField(max_length=2, help_text='행정동일련번호')
    administration_code = models.CharField(max_length=10, help_text='행정동코드')
    administration_name = models.CharField(max_length=40, help_text='행정동명')
    zip_code = models.CharField(max_length=5, help_text='우편번호')
    zip_no = models.CharField(max_length=3, help_text='우편일련번호')
    multi_delievery_address_name = models.CharField(max_length=40, help_text='다량배달처명')
    move_reason_code = models.CharField(max_length=2, help_text='이동사유코드')
    create_time = models.CharField(max_length=8, help_text='고시일자')
    before_road_name_address = models.CharField(max_length=25, help_text='변동전도로명주소')
    city_gungu_building_name = models.CharField(max_length=40, help_text='시군구용 건물명')
    is_multi_building = models.CharField(max_length=1, help_text='공동주택여부')
    base_area_no = models.CharField(max_length=5, help_text='기초구역번호')
    is_detail_address = models.CharField(max_length=1, help_text='상세주소여부')
    empty_one = models.CharField(max_length=15, help_text='비고1')
    empty_two = models.CharField(max_length=15, help_text='비고2')

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name