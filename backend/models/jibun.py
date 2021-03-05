from django.db import models

class Jibun(models.Model):
    # Fields
    legal_dong_code = models.CharField(max_length=10, help_text='법정동코드')
    city_state_name = models.CharField(max_length=40, help_text='시도명')
    city_gungu_name = models.CharField(max_length=40, help_text='시군구명')
    legal_upmeundong_name = models.CharField(max_length=40, help_text='법정읍면동명')
    legal_lee_name = models.CharField(max_length=40, help_text='법정리명')
    is_mountain = models.BooleanField(help_text='산여부 (0:대지, 1:산)')
    jibun_bonbun_bunji = models.IntegerField(max_length=4, help_text='지번본번(번지)')
    jibun_boobun_ho = models.IntegerField(max_length=4, help_text='지번부번(호)')
    road_name_code = models.CharField(max_length=12, help_text='도로명코드 (시군구코드(5) + 도로명번호(7))')
    is_underground = models.CharField(max_length=1, help_text='지하여부 (0:지상, 1:지하, 2:공중)')
    building_bonbun = models.IntegerField(max_length=5, help_text='건물본번')
    building_boobun = models.IntegerField(max_length=5, help_text='건물부번')
    jibun_no = models.IntegerField(max_length=10, help_text='지번일련번호')
    move_reason_code = models.CharField(max_length=2, help_text='이동사유코드 (31:신규, 34:변동, 63:폐지')

    # Metadata
    class Meta:
        ordering = ['id', 'legal_dong_code']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name

