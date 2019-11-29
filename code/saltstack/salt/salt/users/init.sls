{% for username, details in pillar.get('users', {}).items() %}                 
{% set uid = details.get('uid', '') %}                                         
{% set gid = details.get('gid', '') %}                                         
{{ username }}:                                                                
                                                                               
    group.present:                                                             
        - name: {{username}}                                                   
        {% if gid %}                                                           
        - gid: {{ gid }}                                                       
        {% endif %}                                                            
                                                                               
    user.present:                                                              
        - fullname: {{ details.get('fullname','') }}                           
        - shell: /bin/bash                                                     
        - home: /home/{{ username }}                                           
        - uid: {{ uid }}                                                       
        - password: {{ details.get('crypt','') }}                              
        - enforce_password: True                                               
        - remove_groups: False                                                 
        {% if 'groups' in details %}                                           
        - groups:                                                              
        {% for group in details.get('groups', []) %}                           
            - {{ group }}                                                      
        {% endfor %}                                                           
        {% endif %}                                                            
        {% if gid %}                                                           
        - gid: {{ gid }}                                                       
        - require:                                                             
            - group: {{ username }}                                            
        {% else %}                                                             
        - gid_from_name: True                                                  
        {% endif %}                                                            
                                                                               
    {% if 'pub_ssh_keys' in details %}                                         
    ssh_auth.present:                                                          
        - user: {{ username }}                                                 
        - names:                                                               
        {% for pub_ssh_key in details.get('pub_ssh_keys', []) %}               
            - {{ pub_ssh_key }}                                                
        {% endfor %}                                                           
        - require:                                                             
            - user: {{ username }}                                             
    {% endif %}                                                                
                                                                               
{% endfor %}                                                                   
                                                                               
{% for username, details in pillar.get('users_absent', {}).items() %}          
{% set uid = details.get('uid', '') %}                                         
{% set gid = details.get('gid', '') %}                                         
remove-user-{{ username }}:                                                    
    user.absent:                                                               
        - name: {{ username }}                                                 
        - purge: True                                                          
                                                                               
remove-group-{{ username }}:                                                   
    group.absent:                                                              
        - name: {{ username }}                                                 

{% endfor %}
