from spider import Spider
import re

class HaocheSpider(Spider):
    def __init__(self):
        super(HaocheSpider, self).__init__(
            rt=r'alt="(.*?)"',
            ru=r'href="(.*?)">',
            rp=r'<span class="value">(.*?)</span>',
            ri=r'class="iunit"(?:[\s\S]*?)target([\s\S]*?)</a>',
            u=r'',
            up=r'http://%s.haoche51.com/vehicle_list/f_p%d-%d/p%d.html'
        )

    def get_description(self, detail):
        pass

    def get_time_distance(self, i):
        return re.findall(
            r'\'timcs(?:.*?)\'>([\d\.]*)(?:\D*)([\d\.]*)(?:.*?)</div>',
            i)[0]
