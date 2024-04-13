import CloudFlare

def getdnsrecords(zoneid):
    dnsrecords = {}
    cf = CloudFlare.CloudFlare(raw=True)
    page_number = 0
    while True:
        page_number += 1
        raw_results = cf.zones.dns_records.get(zoneid, params={'per_page':5,'page':page_number})
        records = raw_results['result']

        for record in records:
            record_id = record['id']
            record_name = record['name']
            dnsrecords[record['name']] = record['id']

        total_pages = raw_results['result_info']['total_pages']
        if page_number == total_pages:
            break
    return dnsrecords



def getzoneids():
    zoneids = {}
    cf = CloudFlare.CloudFlare(raw=True)
    page_number = 0
    while True:
        page_number += 1
        raw_results = cf.zones.get(params={'per_page':5,'page':page_number})
        zones = raw_results['result']

        for zone in zones:
            zone_id = zone['id']
            zone_name = zone['name']
            zoneids[zone['name']] = zone['id']

        total_pages = raw_results['result_info']['total_pages']
        if page_number == total_pages:
            break
    return zoneids

def main():
    zoneids = getzoneids()
    print(zoneids['ign8.it'])
    recordids = getdnsrecords(zoneids['ign8.it'])
    dns_record = {
                'type':    'TXT',
                'name':    'swarmtoken',
                'content': 'Demor',
                'proxied': False
            }
    try:
        myid = print(recordids['swarmtoken.ign8.it'])
        dns_record = cf.zones.dns_records.put(zoneids['ign8.it'], recordids['swarmtoken.ign8.it'], data=dns_record)
    except:
        cf = CloudFlare.CloudFlare(raw=True)
        try:
            r = cf.zones.dns_records.post(zoneids['ign8.it'], data=dns_record)
        except:
            pass

if __name__ == '__main__':
    main()
