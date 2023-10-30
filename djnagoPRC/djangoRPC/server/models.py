from django.db import models


class ScanInfo(models.Model):
    ip_status = models.CharField(max_length=20)
    protocols = models.CharField(max_length=20)
    open_ports = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    data_chunk = models.TextField()


class ClientBD(models.Model):

    ip_client = models.CharField(max_length=20)

    def __str__(self):
        return self.ip_client


class DataServer(models.Model):
    client = models.ForeignKey(ClientBD, on_delete=models.SET_NULL, null=True)
    tag = models.CharField(max_length=10, default=False)
    ip = models.CharField(max_length=20)
    port = models.CharField(max_length=20)
    mode = models.CharField(max_length=20)


class SegmentScan(models.Model):

    MODE_CHOICES = (
        ('', 'Выберите режим'), 
        ('TCP', 'TCP'),
        ('UDP', 'UDP'),
        ('OS', 'OS')
    )
    
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='')
    ip = models.CharField(max_length=20)
    mask = models.CharField(max_length=20)
    state_scan = models.CharField(max_length=20, default=False)
    cve_report = models.BooleanField(default=False)
    full_scan = models.BooleanField(default=False)


class IPAddress(models.Model):
    address = models.GenericIPAddressField()
    client = models.ForeignKey(
        ClientBD, on_delete=models.SET_NULL, null=True)
    tag = models.CharField(max_length=20, default=False)
    seg_scan = models.ForeignKey(SegmentScan, on_delete=models.CASCADE)


class SegmentResult(models.Model):
    host = models.CharField(max_length=20)
    state_scan = models.CharField(max_length=20)
    state_ports = models.CharField(max_length=10)
    full_name = models.CharField(max_length=30)
    vendor = models.CharField(max_length=20)
    osfamily = models.CharField(max_length=20)
    osgen = models.CharField(max_length=20)
    accuracy = models.CharField(max_length=20)
    result = models.ForeignKey(
        IPAddress, on_delete=models.CASCADE)


class ResultPorts(models.Model):
    port = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    service = models.CharField(max_length=20)
    one_cve = models.TextField()
    cve_information = models.TextField()
    all_info = models.ForeignKey(SegmentResult, on_delete=models.CASCADE)

# class CveInformation(models.Model):
#     host = models.CharField(max_length=20)
#     port = models.CharField(max_length=10)
#     cve_information = models.TextField()



# class ResultOs(models.Model):
#     full_name = models.CharField(max_length=30)
#     vendor = models.CharField(max_length=20)
#     osfamily = models.CharField(max_length=20)
#     osgen = models.CharField(max_length=20)
#     accuracy = models.CharField(max_length=20)
#     all_info = models.ForeignKey(SegmentResult, on_delete=models.CASCADE)

