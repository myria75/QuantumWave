'''Module with DB Manager for Pattern Table'''
# Don't execute directly with the interpreter
# Use the PatternManager object with the Django shell:
#   $ python manage.py shell
from QCPDWeb.models import Pattern

class PatternManager():
    '''Class for managing patterns in the Patterns Table'''
    csv = open('patterns.csv', 'r', encoding='utf-8')

    def update_from_csv(self):
        '''Add the patterns in the "patterns.csv" file into DB'''
        for i, line in enumerate(self.csv.readlines()):
            if i > 0:
                raw_data = line.split(';')
                pattern = Pattern(name=raw_data[1],
                                  json=raw_data[2],
                                  xml=raw_data[3],
                                  desc=raw_data[4],
                                  url=raw_data[5])
                pattern.save()
                print(f'Pattern "{pattern.name}" saved correctly')

    def create(self, pat_name, json, xml, desc, url):
        '''Create a new pattern with given data'''
        new_pat = Pattern(name=pat_name, json=json, xml=xml, desc=desc, url=url)
        new_pat.save()
        print(f'Pattern "{pat_name}" saved correctly')

    # pylint: disable=E1101
    def read_all(self):
        '''Read all the patterns in the DB'''
        result = Pattern.objects.all().order_by('name').values()
        return result

    def read(self, pat_name):
        '''Read the pattern with the given name from DB'''
        try:
            return Pattern.objects.get(name=pat_name)
        except Pattern.DoesNotExist:
            print(f'Pattern "{pat_name}" does not exist.')
            return None
    # pylint: enable=E1101

    def remove(self, pat_name):
        '''Delete the pattern with the given name from DB'''
        pattern = self.read(pat_name)
        pattern.delete()
        print(f'Pattern "{pat_name}" deleted correctly')

    def set(self, pat_name, json=None, xml=None, desc=None, url=None):
        '''Update attributes from the pattern with the given name in the DB'''
        pattern = self.read(pat_name)
        if pattern is None:
            return None

        if (json is None) and (xml is None) and (desc is None) and (url is None):
            print('A value for "json"/"xml"/"desc"/"url" is needed')
            return None

        if json is not None:
            pattern.json = json
        if xml is not None:
            pattern.xml = xml
        if desc is not None:
            pattern.desc = desc
        if url is not None:
            pattern.url = url

        pattern.save()
        print(f'Pattern "{pat_name}" updated correctly')
