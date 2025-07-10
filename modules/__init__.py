#modules/__init__.py

# Bu paket yüklendiğinde alt modülleri import et
from .broken_access_control import test_broken_access_control
from .injection import test_injection
from .authentication_failure import test_authentication_failure
from .security_misconfiguration import test_security_misconfiguration
# Diğer modülleri de aynı şekilde ekle

# Böylece dışarıdan şöyle import edilebilir:
# from modules import test_broken_access_control