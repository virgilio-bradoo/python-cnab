
from cnab240.registro import RegistroBase

class Evento(dict):
    
    def __init__(self, **kwargs):
        if not self.SEGMENTOS_VALIDOS:
            raise NotImplementedError

        self.versao_layout = kwargs.get('versao')
        self._segmentos = dict.fromkeys(self.SEGMENTOS_VALIDOS)
       
    def adicionar_segmento(self, segmento):
    
        if not isinstance(segmento, RegistroBase):
            raise TypeError
        
        if segmento.servico_segmento not in self.SEGMENTOS_VALIDOS:
            raise TypeError 

        self._segmentos.update({segmento.servico_segmento: segmento})
         
    def __unicode__(self):
        return u'\n'.join(unicode(seg) for seg in self._segmentos.values()
                          if seg) 
