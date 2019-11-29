
/etc/check_mk/mrpe.cfg:
  file.managed:
    - source: salt://deploy/templates/mrpe.cfg
    - user: root
    - group: root
    - mode: 644
    - template: jinja
    - context: {{ pillar['mrpe'] }}
    - makedirs: True

