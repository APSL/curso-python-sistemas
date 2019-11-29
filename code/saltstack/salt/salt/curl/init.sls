
install-curl:
  pkg.installed:
    - name: curl

varios:
  pkg.installed:
    - pkgs:
        - python-requests
        - python-click
  
