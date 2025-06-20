from penyakit_logbook import isi_logbook_penyakit
from ketrampilan_logbook import isi_logbook_ketrampilan
from eval_akhir import isi_eval_akhir
from approve_penyakit import approve_logbook_penyakit
from approve_ketrampilan import approve_logbook_ketrampilan

def isi_semua_logbook(username, password, id_stase, tanggal):
    isi_logbook_penyakit(username, password, id_stase, tanggal)
    isi_logbook_ketrampilan(username, password, id_stase, tanggal)
    isi_eval_akhir(username, password, id_stase)
    approve_logbook_penyakit(username, password, id_stase, tanggal)
    approve_logbook_ketrampilan(username, password, id_stase, tanggal)