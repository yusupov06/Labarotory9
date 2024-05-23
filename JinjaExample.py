from jinja2 import Template

if __name__ == '__main__':
    cities = [
        {'id': 1, 'name': 'Tashkent'},
        {'id': 2, 'name': 'Andijan'},
        {'id': 3, 'name': 'Namangan'}
    ]

    link = '''
         <select>
            {%- for c in cities -%}
                <option value="{{c['id']}}"> {{c['name']}} </option>
            {%- endfor -%}
         </select>
    '''

    tm = Template(link)

    res = tm.render(cities=cities)

    print(res)
