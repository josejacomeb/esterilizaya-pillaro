from django import template

register = template.Library()


@register.filter
def es_numero_con_whatsapp(n_telefono):
    """Chequea que el número sea de 9 dígitos."""
    str_n_telefono = str(n_telefono)
    if not str_n_telefono[0] == "9":
        return False
    if len(str_n_telefono) == 9:
        return True
    return False
