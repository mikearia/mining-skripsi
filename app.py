from flask import Flask, jsonify
import pymysql
from flask_cors import CORS
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import requests
import json 
from pandas import Series, DataFrame

db = pymysql.connect('ramdhanrizki.net', 'root', 'code@labs', 'ketahanan_tanaman')
cursor = db.cursor()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"status": "success"})



@app.route('/api/tanaman/', methods=['GET'])
def getTanaman():
    try:
        cursor.execute("SELECT * FROM tanaman")
        results = cursor.fetchall()
        data = []
        for item in results:
            data.append({'id_tanaman': item[0], 'nama_tanaman': item[1]})
        return jsonify(data)
    except Exception as e:
        return jsonify({'response': 404, 'error': e})



def modus(tanaman):
	data = requests.get('https://ews-mining.herokuapp.com/rest-api/identifikasi').json()
	
	nama_penyakit = [];
	nama_tanaman = [];
	provinsi = [];
	identifikasi = [];
	modus = data['result']
	
	for val in modus:
	    nama_penyakit.append(val['nama_penyakit'])
	    nama_tanaman.append(val['nama_tanaman'])
	    provinsi.append(val['provinsi'])
	
	identifikasi = np.array(list(zip(nama_penyakit, nama_tanaman, provinsi)), dtype=np.str)
	dframe = DataFrame(identifikasi,columns=['Nama Penyakit','Nama Tanaman','Provinsi'])
	
	sortbyfruit = dframe.sort_values(['Nama Tanaman','Provinsi'])
	# modus eggplant
	is_eggplant = sortbyfruit['Nama Tanaman']=="Eggplant"
	sortbyfruit_is_eggplant = sortbyfruit[is_eggplant]
	
	is_aceh = sortbyfruit_is_eggplant['Provinsi']=="Aceh"
	sortbyfruit_is_eggplant_Aceh = sortbyfruit_is_eggplant[is_aceh]
	egp1 = {'penyakit':sortbyfruit_is_eggplant_Aceh.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_Aceh.mode().iat[0,2]}
	
	is_bengkulu = sortbyfruit_is_eggplant['Provinsi']=="Bengkulu"
	sortbyfruit_is_eggplant_bengkulu = sortbyfruit_is_eggplant[is_bengkulu]
	egp2 = {'penyakit':sortbyfruit_is_eggplant_bengkulu.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_bengkulu.mode().iat[0,2]}

	is_diy = sortbyfruit_is_eggplant['Provinsi']=="DI Yogyakarta"
	sortbyfruit_is_eggplant_diy = sortbyfruit_is_eggplant[is_diy]
	egp3 = {'penyakit':sortbyfruit_is_eggplant_diy.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_diy.mode().iat[0,2]}

	is_jabar = sortbyfruit_is_eggplant['Provinsi']=="Jawa Barat"
	sortbyfruit_is_eggplant_jabar = sortbyfruit_is_eggplant[is_jabar]
	egp4 = {'penyakit':sortbyfruit_is_eggplant_jabar.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_jabar.mode().iat[0,2]}

	is_bali = sortbyfruit_is_eggplant['Provinsi']=="Bali"
	sortbyfruit_is_eggplant_bali = sortbyfruit_is_eggplant[is_bali]
	egp5 = {'penyakit':sortbyfruit_is_eggplant_bali.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_bali.mode().iat[0,2]}

	is_jateng = sortbyfruit_is_eggplant['Provinsi']=="Jawa Tengah"
	sortbyfruit_is_eggplant_jateng = sortbyfruit_is_eggplant[is_jateng]
	egp6 = {'penyakit':sortbyfruit_is_eggplant_jateng.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_jateng.mode().iat[0,2]}

	is_jatim = sortbyfruit_is_eggplant['Provinsi']=="Jawa Timur"
	sortbyfruit_is_eggplant_jatim = sortbyfruit_is_eggplant[is_jatim]
	egp7 = {'penyakit':sortbyfruit_is_eggplant_jatim.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_jatim.mode().iat[0,2]}

	is_kalbar = sortbyfruit_is_eggplant['Provinsi']=="Kalimantan Barat"
	sortbyfruit_is_eggplant_kalbar = sortbyfruit_is_eggplant[is_kalbar]
	egp8 = {'penyakit':sortbyfruit_is_eggplant_kalbar.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_kalbar.mode().iat[0,2]}

	is_kalsel = sortbyfruit_is_eggplant['Provinsi']=="Kalimantan Selatan"
	sortbyfruit_is_eggplant_kalsel = sortbyfruit_is_eggplant[is_kalsel]
	egp9 = {'penyakit':sortbyfruit_is_eggplant_kalsel.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_kalsel.mode().iat[0,2]}

	is_kaltim = sortbyfruit_is_eggplant['Provinsi']=="Kalimantan Timur"
	sortbyfruit_is_eggplant_kaltim = sortbyfruit_is_eggplant[is_kaltim]
	egp10 = {'penyakit':sortbyfruit_is_eggplant_kaltim.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_kaltim.mode().iat[0,2]}

	is_lpg = sortbyfruit_is_eggplant['Provinsi']=="Lampung"
	sortbyfruit_is_eggplant_lpg = sortbyfruit_is_eggplant[is_lpg]
	egp11 = {'penyakit':sortbyfruit_is_eggplant_lpg.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_lpg.mode().iat[0,2]}

	is_ntb = sortbyfruit_is_eggplant['Provinsi']=="Nusa Tenggara Barat"
	sortbyfruit_is_eggplant_ntb = sortbyfruit_is_eggplant[is_ntb]
	egp12 = {'penyakit':sortbyfruit_is_eggplant_ntb.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_ntb.mode().iat[0,2]}

	is_sumbar = sortbyfruit_is_eggplant['Provinsi']=="Sumatra Barat"
	sortbyfruit_is_eggplant_sumbar = sortbyfruit_is_eggplant[is_sumbar]
	egp13 = {'penyakit':sortbyfruit_is_eggplant_sumbar.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_sumbar.mode().iat[0,2]}

	is_sumut = sortbyfruit_is_eggplant['Provinsi']=="Sumatra Utara"
	sortbyfruit_is_eggplant_sumut = sortbyfruit_is_eggplant[is_sumut]
	egp14 = {'penyakit':sortbyfruit_is_eggplant_sumut.mode().iat[0,0],'provinsi':sortbyfruit_is_eggplant_sumut.mode().iat[0,2]}

	egp = [egp1,egp2,egp3,egp4,egp5,egp6,egp7,egp8,egp9,egp10,egp11,egp12,egp13,egp14]

	#modus bird's eye pepper
	is_bep = sortbyfruit['Nama Tanaman']=="Bird's Eye Pepper"
	sortbyfruit_is_bep = sortbyfruit[is_bep]

	is_jatim = sortbyfruit_is_bep['Provinsi']=="Jawa Timur"
	sortbyfruit_is_bep_jatim = sortbyfruit_is_bep[is_jatim]
	bep1 = {'penyakit':sortbyfruit_is_bep_jatim.mode().iat[0,0],'provinsi':sortbyfruit_is_bep_jatim.mode().iat[0,2]}

	is_lpg = sortbyfruit_is_bep['Provinsi']=="Lampung"
	sortbyfruit_is_bep_lpg = sortbyfruit_is_bep[is_lpg]
	bep2 = {'penyakit':sortbyfruit_is_bep_lpg.mode().iat[0,0],'provinsi':sortbyfruit_is_bep_lpg.mode().iat[0,2]}

	bep = [bep1,bep2]

	# modus curly pepper
	is_cp = sortbyfruit['Nama Tanaman']=="Curly Pepper"
	sortbyfruit_is_cp = sortbyfruit[is_cp]

	is_bengkulu = sortbyfruit_is_cp['Provinsi']=="Bengkulu"
	sortbyfruit_is_cp_bengkulu = sortbyfruit_is_cp[is_bengkulu]
	cp1 = {'penyakit':sortbyfruit_is_cp_bengkulu.mode().iat[0,0],'provinsi':sortbyfruit_is_cp_bengkulu.mode().iat[0,2]}

	is_diy = sortbyfruit_is_cp['Provinsi']=="DI Yogyakarta"
	sortbyfruit_is_cp_diy = sortbyfruit_is_cp[is_diy]
	cp2 = {'penyakit':sortbyfruit_is_cp_diy.mode().iat[0,0],'provinsi':sortbyfruit_is_cp_diy.mode().iat[0,2]}

	is_jatim = sortbyfruit_is_cp['Provinsi']=="Jawa Timur"
	sortbyfruit_is_cp_jatim = sortbyfruit_is_cp[is_jatim]
	cp3 = {'penyakit':sortbyfruit_is_cp_jatim.mode().iat[0,0],'provinsi':sortbyfruit_is_cp_jatim.mode().iat[0,2]}

	is_sumbar = sortbyfruit_is_cp['Provinsi']=="Sumatra Barat"
	sortbyfruit_is_cp_sumbar = sortbyfruit_is_cp[is_sumbar]
	cp4 = {'penyakit':sortbyfruit_is_cp_sumbar.mode().iat[0,0],'provinsi':sortbyfruit_is_cp_sumbar.mode().iat[0,2]}

	cp = [cp1,cp2,cp3,cp4]

	#modus common bean
	is_cb = sortbyfruit['Nama Tanaman']=="Common Bean"
	sortbyfruit_is_cb = sortbyfruit[is_cb]

	is_kalsel = sortbyfruit_is_cb['Provinsi']=="Kalimantan Selatan"
	sortbyfruit_is_cb_kalsel = sortbyfruit_is_cb[is_kalsel]
	cb1 = {'penyakit':sortbyfruit_is_cb_kalsel.mode().iat[0,0],'provinsi':sortbyfruit_is_cb_kalsel.mode().iat[0,2]}

	is_sumbar = sortbyfruit_is_cb['Provinsi']=="Sumatra Barat"
	sortbyfruit_is_cb_sumbar = sortbyfruit_is_cb[is_sumbar]
	cb2 = {'penyakit':sortbyfruit_is_cb_sumbar.mode().iat[0,0],'provinsi':sortbyfruit_is_cb_sumbar.mode().iat[0,2]}

	cb = [cb1,cb2]

	#modus cucumber
	is_ccb = sortbyfruit['Nama Tanaman']=="Cucumber"
	sortbyfruit_is_ccb = sortbyfruit[is_ccb]

	is_aceh = sortbyfruit_is_ccb['Provinsi']=="Aceh"
	sortbyfruit_is_ccb_aceh = sortbyfruit_is_ccb[is_aceh]
	ccb1 = {'penyakit':sortbyfruit_is_ccb_aceh.mode().iat[0,0],'provinsi':sortbyfruit_is_ccb_aceh.mode().iat[0,2]}

	is_jabar = sortbyfruit_is_ccb['Provinsi']=="Jawa Barat"
	sortbyfruit_is_ccb_jabar = sortbyfruit_is_ccb[is_jabar]
	ccb2 = {'penyakit':sortbyfruit_is_ccb_jabar.mode().iat[0,0],'provinsi':sortbyfruit_is_ccb_jabar.mode().iat[0,2]}

	is_jateng = sortbyfruit_is_ccb['Provinsi']=="Jawa Tengah"
	sortbyfruit_is_ccb_jateng = sortbyfruit_is_ccb[is_jateng]
	ccb3 = {'penyakit':sortbyfruit_is_ccb_jateng.mode().iat[0,0],'provinsi':sortbyfruit_is_ccb_jateng.mode().iat[0,2]}

	is_jatim = sortbyfruit_is_ccb['Provinsi']=="Jawa Timur"
	sortbyfruit_is_ccb_jatim = sortbyfruit_is_ccb[is_jatim]
	ccb4 = {'penyakit':sortbyfruit_is_ccb_jatim.mode().iat[0,0],'provinsi':sortbyfruit_is_ccb_jatim.mode().iat[0,2]}

	is_kalbar = sortbyfruit_is_ccb['Provinsi']=="Kalimantan Barat"
	sortbyfruit_is_ccb_kalbar = sortbyfruit_is_ccb[is_kalbar]
	ccb5 = {'penyakit':sortbyfruit_is_ccb_kalbar.mode().iat[0,0],'provinsi':sortbyfruit_is_ccb_kalbar.mode().iat[0,2]}

	is_kalsel = sortbyfruit_is_ccb['Provinsi']=="Kalimantan Selatan"
	sortbyfruit_is_ccb_kalsel = sortbyfruit_is_ccb[is_kalsel]
	ccb6 = {'penyakit':sortbyfruit_is_ccb_kalsel.mode().iat[0,0],'provinsi':sortbyfruit_is_ccb_kalsel.mode().iat[0,2]}

	is_kaltim = sortbyfruit_is_ccb['Provinsi']=="Kalimantan Timur"
	sortbyfruit_is_ccb_kaltim = sortbyfruit_is_ccb[is_kaltim]
	ccb7 = {'penyakit':sortbyfruit_is_ccb_kaltim.mode().iat[0,0],'provinsi':sortbyfruit_is_ccb_kaltim.mode().iat[0,2]}

	is_lpg = sortbyfruit_is_ccb['Provinsi']=="Lampung"
	sortbyfruit_is_ccb_lpg = sortbyfruit_is_ccb[is_lpg]
	ccb8 = {'penyakit':sortbyfruit_is_ccb_lpg.mode().iat[0,0],'provinsi':sortbyfruit_is_ccb_lpg.mode().iat[0,2]}

	is_sumut = sortbyfruit_is_ccb['Provinsi']=="Sumatra Utara"
	sortbyfruit_is_ccb_sumut = sortbyfruit_is_ccb[is_sumut]
	ccb9 = {'penyakit':sortbyfruit_is_ccb_sumut.mode().iat[0,0],'provinsi':sortbyfruit_is_ccb_sumut.mode().iat[0,2]}

	ccb = [ccb1,ccb2,ccb3,ccb4,ccb5,ccb6,ccb7,ccb8,ccb9]

	#modus Green Bean
	is_gb = sortbyfruit['Nama Tanaman']=="Green Bean"
	sortbyfruit_is_gb = sortbyfruit[is_gb]

	is_jabar = sortbyfruit_is_gb['Provinsi']=="Jawa Barat"
	sortbyfruit_is_gb_jabar = sortbyfruit_is_gb[is_jabar]
	gb1 = {'penyakit':sortbyfruit_is_gb_jabar.mode().iat[0,0],'provinsi':sortbyfruit_is_gb_jabar.mode().iat[0,2]}

	gb = [gb1]

	#modus cauli flower
	is_cl = sortbyfruit['Nama Tanaman']=="Cauli Flower"
	sortbyfruit_is_cl = sortbyfruit[is_cl]

	is_btn = sortbyfruit_is_cl['Provinsi']=="Banten"
	sortbyfruit_is_cl_btn = sortbyfruit_is_cl[is_btn]
	cl1 = {'penyakit':sortbyfruit_is_cl_btn.mode().iat[0,0],'provinsi':sortbyfruit_is_cl_btn.mode().iat[0,2]}

	is_diy = sortbyfruit_is_cl['Provinsi']=="DI Yogyakarta"
	sortbyfruit_is_cl_diy = sortbyfruit_is_cl[is_diy]
	cl2 = {'penyakit':sortbyfruit_is_cl_diy.mode().iat[0,0],'provinsi':sortbyfruit_is_cl_diy.mode().iat[0,2]}

	is_jabar = sortbyfruit_is_cl['Provinsi']=="Jawa Barat"
	sortbyfruit_is_cl_jabar = sortbyfruit_is_cl[is_jabar]
	cl3 = {'penyakit':sortbyfruit_is_cl_jabar.mode().iat[0,0],'provinsi':sortbyfruit_is_cl_jabar.mode().iat[0,2]}

	is_jateng = sortbyfruit_is_cl['Provinsi']=="Jawa Tengah"
	sortbyfruit_is_cl_jateng = sortbyfruit_is_cl[is_jateng]
	cl4 = {'penyakit':sortbyfruit_is_cl_jateng.mode().iat[0,0],'provinsi':sortbyfruit_is_cl_jateng.mode().iat[0,2]}

	is_jatim = sortbyfruit_is_cl['Provinsi']=="Jawa Timur"
	sortbyfruit_is_cl_jatim = sortbyfruit_is_cl[is_jatim]
	cl5 = {'penyakit':sortbyfruit_is_cl_jatim.mode().iat[0,0],'provinsi':sortbyfruit_is_cl_jatim.mode().iat[0,2]}

	is_ntb = sortbyfruit_is_cl['Provinsi']=="Nusa Tenggara Barat"
	sortbyfruit_is_cl_ntb = sortbyfruit_is_cl[is_ntb]
	cl6 = {'penyakit':sortbyfruit_is_cl_ntb.mode().iat[0,0],'provinsi':sortbyfruit_is_cl_ntb.mode().iat[0,2]}

	is_ppa = sortbyfruit_is_cl['Provinsi']=="Papua"
	sortbyfruit_is_cl_ppa = sortbyfruit_is_cl[is_ppa]
	cl7= {'penyakit':sortbyfruit_is_cl_ppa.mode().iat[0,0],'provinsi':sortbyfruit_is_cl_ppa.mode().iat[0,2]}

	is_sulteng = sortbyfruit_is_cl['Provinsi']=="Sulawesi Tengah"
	sortbyfruit_is_cl_sulteng = sortbyfruit_is_cl[is_sulteng]
	cl8 = {'penyakit':sortbyfruit_is_cl_sulteng.mode().iat[0,0],'provinsi':sortbyfruit_is_cl_sulteng.mode().iat[0,2]}

	is_sumbar = sortbyfruit_is_cl['Provinsi']=="Sumatra Barat"
	sortbyfruit_is_cl_sumbar = sortbyfruit_is_cl[is_sumbar]
	cl9 = {'penyakit':sortbyfruit_is_cl_sumbar.mode().iat[0,0],'provinsi':sortbyfruit_is_cl_sumbar.mode().iat[0,2]}

	is_sumsel = sortbyfruit_is_cl['Provinsi']=="Sumatra Selatan"
	sortbyfruit_is_cl_sumsel = sortbyfruit_is_cl[is_sumsel]
	cl10 = {'penyakit':sortbyfruit_is_cl_sumsel.mode().iat[0,0],'provinsi':sortbyfruit_is_cl_sumsel.mode().iat[0,2]}

	cl = [cl1,cl2,cl3,cl4,cl5,cl6,cl7,cl8,cl9,cl10]

	#modus luffa
	is_lf = sortbyfruit['Nama Tanaman']=="Luffa"
	sortbyfruit_is_lf = sortbyfruit[is_lf]

	is_jatim = sortbyfruit_is_lf['Provinsi']=="Jawa Timur"
	sortbyfruit_is_lf_jatim = sortbyfruit_is_lf[is_jatim]
	lf1 = {'penyakit':sortbyfruit_is_lf_jatim.mode().iat[0,0],'provinsi':sortbyfruit_is_lf_jatim.mode().iat[0,2]}

	lf = [lf1]

	#modus melon
	is_mln = sortbyfruit['Nama Tanaman']=="Melon"
	sortbyfruit_is_mln = sortbyfruit[is_mln]

	is_aceh = sortbyfruit_is_mln['Provinsi']=="Aceh"
	sortbyfruit_is_mln_aceh = sortbyfruit_is_mln[is_aceh]
	mln1 = {'penyakit':sortbyfruit_is_mln_aceh.mode().iat[0,0],'provinsi':sortbyfruit_is_mln_aceh.mode().iat[0,2]}

	is_btn = sortbyfruit_is_mln['Provinsi']=="Banten"
	sortbyfruit_is_mln_btn = sortbyfruit_is_mln[is_btn]
	mln2 = {'penyakit':sortbyfruit_is_mln_btn.mode().iat[0,0],'provinsi':sortbyfruit_is_mln_btn.mode().iat[0,2]}

	is_jmb = sortbyfruit_is_mln['Provinsi']=="Jambi"
	sortbyfruit_is_mln_jmb = sortbyfruit_is_mln[is_jmb]
	mln3 = {'penyakit':sortbyfruit_is_mln_jmb.mode().iat[0,0],'provinsi':sortbyfruit_is_mln_jmb.mode().iat[0,2]}

	is_jabar = sortbyfruit_is_mln['Provinsi']=="Jawa Barat"
	sortbyfruit_is_mln_jabar = sortbyfruit_is_mln[is_jabar]
	mln4 = {'penyakit':sortbyfruit_is_mln_jabar.mode().iat[0,0],'provinsi':sortbyfruit_is_mln_jabar.mode().iat[0,2]}

	is_jateng = sortbyfruit_is_mln['Provinsi']=="Jawa Tengah"
	sortbyfruit_is_mln_jateng = sortbyfruit_is_mln[is_jateng]
	mln5 = {'penyakit':sortbyfruit_is_mln_jateng.mode().iat[0,0],'provinsi':sortbyfruit_is_mln_jateng.mode().iat[0,2]}

	is_jatim = sortbyfruit_is_mln['Provinsi']=="Jawa Timur"
	sortbyfruit_is_mln_jatim = sortbyfruit_is_mln[is_jatim]
	mln6 = {'penyakit':sortbyfruit_is_mln_jatim.mode().iat[0,0],'provinsi':sortbyfruit_is_mln_jatim.mode().iat[0,2]}

	is_kalbar = sortbyfruit_is_mln['Provinsi']=="Kalimantan Barat"
	sortbyfruit_is_mln_kalbar = sortbyfruit_is_mln[is_kalbar]
	mln7 = {'penyakit':sortbyfruit_is_mln_kalbar.mode().iat[0,0],'provinsi':sortbyfruit_is_mln_kalbar.mode().iat[0,2]}

	is_kalsel = sortbyfruit_is_mln['Provinsi']=="Kalimantan Selatan"
	sortbyfruit_is_mln_kalsel = sortbyfruit_is_mln[is_kalsel]
	mln8 = {'penyakit':sortbyfruit_is_mln_kalsel.mode().iat[0,0],'provinsi':sortbyfruit_is_mln_kalsel.mode().iat[0,2]}

	is_kaltim = sortbyfruit_is_mln['Provinsi']=="Kalimantan Timur"
	sortbyfruit_is_mln_kaltim = sortbyfruit_is_mln[is_kaltim]
	mln9 = {'penyakit':sortbyfruit_is_mln_kaltim.mode().iat[0,0],'provinsi':sortbyfruit_is_mln_kaltim.mode().iat[0,2]}

	is_sumut = sortbyfruit_is_mln['Provinsi']=="Sumatra Utara"
	sortbyfruit_is_mln_sumut = sortbyfruit_is_mln[is_sumut]
	mln10 = {'penyakit':sortbyfruit_is_mln_sumut.mode().iat[0,0],'provinsi':sortbyfruit_is_mln_sumut.mode().iat[0,2]}

	mln = [mln1,mln2,mln3,mln4,mln5,mln6,mln7,mln8,mln9,mln10]

	#modus pepper
	is_ppr = sortbyfruit['Nama Tanaman']=="Pepper"
	sortbyfruit_is_ppr = sortbyfruit[is_ppr]

	is_bkl = sortbyfruit_is_ppr['Provinsi']=="Bengkulu"
	sortbyfruit_is_ppr_bkl = sortbyfruit_is_ppr[is_bkl]
	ppr1 = {'penyakit':sortbyfruit_is_ppr_bkl.mode().iat[0,0],'provinsi':sortbyfruit_is_ppr_bkl.mode().iat[0,2]}

	is_jmb = sortbyfruit_is_ppr['Provinsi']=="Jambi"
	sortbyfruit_is_ppr_jmb = sortbyfruit_is_ppr[is_jmb]
	ppr2 = {'penyakit':sortbyfruit_is_ppr_jmb.mode().iat[0,0],'provinsi':sortbyfruit_is_ppr_jmb.mode().iat[0,2]}

	is_jabar = sortbyfruit_is_ppr['Provinsi']=="Jawa Barat"
	sortbyfruit_is_ppr_jabar = sortbyfruit_is_ppr[is_jabar]
	ppr3 = {'penyakit':sortbyfruit_is_ppr_jabar.mode().iat[0,0],'provinsi':sortbyfruit_is_ppr_jabar.mode().iat[0,2]}

	is_jatim = sortbyfruit_is_ppr['Provinsi']=="Jawa Timur"
	sortbyfruit_is_ppr_jatim = sortbyfruit_is_ppr[is_jatim]
	ppr4 = {'penyakit':sortbyfruit_is_ppr_jatim.mode().iat[0,0],'provinsi':sortbyfruit_is_ppr_jatim.mode().iat[0,2]}

	is_jateng = sortbyfruit_is_ppr['Provinsi']=="Jawa Tengah"
	sortbyfruit_is_ppr_jateng = sortbyfruit_is_ppr[is_jateng]
	ppr5 = {'penyakit':sortbyfruit_is_ppr_jateng.mode().iat[0,0],'provinsi':sortbyfruit_is_ppr_jateng.mode().iat[0,2]}

	is_kaltim = sortbyfruit_is_ppr['Provinsi']=="Kalimantan Timur"
	sortbyfruit_is_ppr_kaltim = sortbyfruit_is_ppr[is_kaltim]
	ppr6 ={'penyakit':sortbyfruit_is_ppr_kaltim.mode().iat[0,0],'provinsi':sortbyfruit_is_ppr_kaltim.mode().iat[0,2]}

	is_ntb = sortbyfruit_is_ppr['Provinsi']=="Nusa Tenggara Barat"
	sortbyfruit_is_ppr_ntb = sortbyfruit_is_ppr[is_ntb]
	ppr7 = {'penyakit':sortbyfruit_is_ppr_ntb.mode().iat[0,0],'provinsi':sortbyfruit_is_ppr_ntb.mode().iat[0,2]}

	is_riau = sortbyfruit_is_ppr['Provinsi']=="Riau"
	sortbyfruit_is_ppr_riau = sortbyfruit_is_ppr[is_riau]
	ppr8 = {'penyakit':sortbyfruit_is_ppr_riau.mode().iat[0,0],'provinsi':sortbyfruit_is_ppr_riau.mode().iat[0,2]}

	is_sulsel = sortbyfruit_is_ppr['Provinsi']=="Sulawesi Selatan"
	sortbyfruit_is_ppr_sulsel = sortbyfruit_is_ppr[is_sulsel]
	ppr9 = {'penyakit':sortbyfruit_is_ppr_sulsel.mode().iat[0,0],'provinsi':sortbyfruit_is_ppr_sulsel.mode().iat[0,	2]}

	is_sumbar = sortbyfruit_is_ppr['Provinsi']=="Sumatra Barat"	
	sortbyfruit_is_ppr_sumbar = sortbyfruit_is_ppr[is_sumbar]
	ppr10 = {'penyakit':sortbyfruit_is_ppr_sumbar.mode().iat[0,0],'provinsi':sortbyfruit_is_ppr_sumbar.mode().iat[0,2]}

	is_sumsel = sortbyfruit_is_ppr['Provinsi']=="Sumatra Selatan"
	sortbyfruit_is_ppr_sumsel = sortbyfruit_is_ppr[is_sumsel]
	ppr11 = {'penyakit':sortbyfruit_is_ppr_sumsel.mode().iat[0,0],'provinsi':sortbyfruit_is_ppr_sumsel.mode().iat[0,2]}

	ppr = [ppr1,ppr2,ppr3,ppr4,ppr5,ppr6,ppr7,ppr8,ppr9,ppr10,ppr11]

	#modus potato
	is_ptt = sortbyfruit['Nama Tanaman']=="Potato"
	sortbyfruit_is_ptt = sortbyfruit[is_ptt]

	is_btn = sortbyfruit_is_ptt['Provinsi']=="Banten"
	sortbyfruit_is_ptt_btn = sortbyfruit_is_ptt[is_btn]
	ptt1 = {'penyakit':sortbyfruit_is_ptt_btn.mode().iat[0,0],'provinsi':sortbyfruit_is_ptt_btn.mode().iat[0,2]}

	is_bkl = sortbyfruit_is_ptt['Provinsi']=="Bengkulu"
	sortbyfruit_is_ptt_bkl = sortbyfruit_is_ptt[is_bkl]
	ptt2 = {'penyakit':sortbyfruit_is_ptt_bkl.mode().iat[0,0],'provinsi':sortbyfruit_is_ptt_bkl.mode().iat[0,2]}

	is_diy = sortbyfruit_is_ptt['Provinsi']=="DI Yogyakarta"
	sortbyfruit_is_ptt_diy = sortbyfruit_is_ptt[is_btn]
	ptt3 = {'penyakit':sortbyfruit_is_ptt_diy.mode().iat[0,0],'provinsi':sortbyfruit_is_ptt_diy.mode().iat[0,2]}

	is_jabar = sortbyfruit_is_ptt['Provinsi']=="Jawa Barat"
	sortbyfruit_is_ptt_jabar = sortbyfruit_is_ptt[is_jabar]
	ptt4 = {'penyakit':sortbyfruit_is_ptt_jabar.mode().iat[0,0],'provinsi':sortbyfruit_is_ptt_jabar.mode().iat[0,2]}

	is_sumbar = sortbyfruit_is_ptt['Provinsi']=="Sumatra Barat"
	sortbyfruit_is_ptt_sumbar = sortbyfruit_is_ptt[is_sumbar]
	ptt5 = {'penyakit':sortbyfruit_is_ptt_sumbar.mode().iat[0,0],'provinsi':sortbyfruit_is_ptt_sumbar.mode().iat[0,2]}

	ptt = [ptt1,ptt2,ptt3,ptt4,ptt5]

	#modus tomat
	is_tmt = sortbyfruit['Nama Tanaman']=="Tomato"
	sortbyfruit_is_tmt = sortbyfruit[is_tmt]

	is_aceh = sortbyfruit_is_tmt['Provinsi']=="Aceh"
	sortbyfruit_is_tmt_aceh = sortbyfruit_is_tmt[is_aceh]
	tmt1 = {'penyakit':sortbyfruit_is_tmt_aceh.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_aceh.mode().iat[0,2]}

	is_bali = sortbyfruit_is_tmt['Provinsi']=="Bali"
	sortbyfruit_is_tmt_bali = sortbyfruit_is_tmt[is_bali]
	tmt2 = {'penyakit':sortbyfruit_is_tmt_bali.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_bali.mode().iat[0,2]}

	is_btn = sortbyfruit_is_tmt['Provinsi']=="Banten"
	sortbyfruit_is_tmt_btn = sortbyfruit_is_tmt[is_btn]
	tmt3 = {'penyakit':sortbyfruit_is_tmt_btn.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_btn.mode().iat[0,2]}

	is_jmb = sortbyfruit_is_tmt['Provinsi']=="Jambi"
	sortbyfruit_is_tmt_jmb = sortbyfruit_is_tmt[is_jmb]
	tmt4 = {'penyakit':sortbyfruit_is_tmt_jmb.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_jmb.mode().iat[0,2]}

	is_jabar = sortbyfruit_is_tmt['Provinsi']=="Jawa Barat"
	sortbyfruit_is_tmt_jabar = sortbyfruit_is_tmt[is_jabar]
	tmt5 = {'penyakit':sortbyfruit_is_tmt_jabar.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_jabar.mode().iat[0,2]}

	is_jateng = sortbyfruit_is_tmt['Provinsi']=="Jawa Tengah"
	sortbyfruit_is_tmt_jateng = sortbyfruit_is_tmt[is_jateng]
	tmt6 = {'penyakit':sortbyfruit_is_tmt_jateng.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_jateng.mode().iat[0,2]}

	is_jatim = sortbyfruit_is_tmt['Provinsi']=="Jawa Timur"
	sortbyfruit_is_tmt_jatim = sortbyfruit_is_tmt[is_jatim]
	tmt7 = {'penyakit':sortbyfruit_is_tmt_jatim.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_jatim.mode().iat[0,2]}

	is_kalsel = sortbyfruit_is_tmt['Provinsi']=="Kalimantan Selatan"
	sortbyfruit_is_tmt_kalsel = sortbyfruit_is_tmt[is_kalsel]
	tmt8 = {'penyakit':sortbyfruit_is_tmt_kalsel.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_kalsel.mode().iat[0,2]}

	is_ntb = sortbyfruit_is_tmt['Provinsi']=="Nusa Tenggara Barat"
	sortbyfruit_is_tmt_ntb = sortbyfruit_is_tmt[is_ntb]
	tmt9 = {'penyakit':sortbyfruit_is_tmt_ntb.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_ntb.mode().iat[0,2]}

	is_sulsel = sortbyfruit_is_tmt['Provinsi']=="Sulawesi Selatan"
	sortbyfruit_is_tmt_sulsel = sortbyfruit_is_tmt[is_sulsel]
	tmt10 = {'penyakit':sortbyfruit_is_tmt_sulsel.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_sulsel.mode().iat[0,2]}

	is_sulteng = sortbyfruit_is_tmt['Provinsi']=="Sulawesi Tengah"
	sortbyfruit_is_tmt_sulteng = sortbyfruit_is_tmt[is_sulteng]
	tmt11 = {'penyakit':sortbyfruit_is_tmt_sulteng.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_sulteng.mode().iat[0,2]}

	is_sultgr = sortbyfruit_is_tmt['Provinsi']=="Sulawesi Tenggara"
	sortbyfruit_is_tmt_sultgr = sortbyfruit_is_tmt[is_sultgr]
	tmt12 = {'penyakit':sortbyfruit_is_tmt_sultgr.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_sultgr.mode().iat[0,2]}

	is_sumsel = sortbyfruit_is_tmt['Provinsi']=="Sumatra Selatan"
	sortbyfruit_is_tmt_sumsel = sortbyfruit_is_tmt[is_sumsel]
	tmt13 = {'penyakit':sortbyfruit_is_tmt_sumsel.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_sumsel.mode().iat[0,2]}

	is_sumut = sortbyfruit_is_tmt['Provinsi']=="Sumatra Utara"
	sortbyfruit_is_tmt_sumut = sortbyfruit_is_tmt[is_sumut]
	tmt14 = {'penyakit':sortbyfruit_is_tmt_sumut.mode().iat[0,0],'provinsi':sortbyfruit_is_tmt_sumut.mode().iat[0,2]}

	tmt = [tmt1,tmt2,tmt3,tmt4,tmt5,tmt6,tmt7,tmt8,tmt9,tmt10,tmt11,tmt12,tmt13,tmt14]

	#modus watermelon
	is_wtm = sortbyfruit['Nama Tanaman']=="Watermelon"
	sortbyfruit_is_wtm = sortbyfruit[is_wtm]

	is_diy = sortbyfruit_is_wtm['Provinsi']=="DI Yogyakarta"
	sortbyfruit_is_wtm_diy = sortbyfruit_is_wtm[is_diy]
	wtm1 = {'penyakit':sortbyfruit_is_wtm_diy.mode().iat[0,0],'provinsi':sortbyfruit_is_wtm_diy.mode().iat[0,2]}

	is_jabar = sortbyfruit_is_wtm['Provinsi']=="Jawa Barat"
	sortbyfruit_is_wtm_jabar = sortbyfruit_is_wtm[is_jabar]
	wtm2 = {'penyakit':sortbyfruit_is_wtm_jabar.mode().iat[0,0],'provinsi':sortbyfruit_is_wtm_jabar.mode().iat[0,2]}

	is_jatim = sortbyfruit_is_wtm['Provinsi']=="Jawa Timur"
	sortbyfruit_is_wtm_jatim = sortbyfruit_is_wtm[is_jatim]
	wtm3 = {'penyakit':sortbyfruit_is_wtm_jatim.mode().iat[0,0],'provinsi': sortbyfruit_is_wtm_jatim.mode().iat[0,2]}

	wtm = [wtm1,wtm2,wtm3]

	#modus yardlong bean
	is_ylb = sortbyfruit['Nama Tanaman']=="Yardlong Bean"
	sortbyfruit_is_ylb = sortbyfruit[is_ylb]

	is_bkl = sortbyfruit_is_ylb['Provinsi']=="Bengkulu"
	sortbyfruit_is_ylb_bkl = sortbyfruit_is_ylb[is_bkl]
	ylb1 = {'penyakit':sortbyfruit_is_ylb_bkl.mode().iat[0,0],'provinsi':sortbyfruit_is_ylb_bkl.mode().iat[0,2]}

	is_jabar = sortbyfruit_is_ylb['Provinsi']=="Jawa Barat"
	sortbyfruit_is_ylb_jabar = sortbyfruit_is_ylb[is_jabar]
	ylb2 = {'penyakit' : sortbyfruit_is_ylb_jabar.mode().iat[0,0], 'provinsi' : sortbyfruit_is_ylb_jabar.mode().iat[0,2]}

	ylb = [ylb1,ylb2]

	if tanaman =="Bird's Eye Pepper":
		return {'tanaman': "Bird's Eye Pepper", 'data': bep}
	elif tanaman == "Common Bean":
		return {'tanaman': "Common Bean", 'data': cb}
	elif tanaman == "Cucumber":
		return {'tanaman': "Cucumber", 'data': ccb}
	elif tanaman == "Curly Pepper":
		return {'tanaman': "Curly Pepper", 'data': cp}
	elif tanaman == "Eggplant":
		return {'tanaman': "Eggplant", 'data': egp}
	elif tanaman == "Greenbean":
		return {'tanaman': "Greenbean", 'data': gb}
	elif tanaman == "Cauli Flower":
		return {'tanaman': "Cauli Flower", 'data': cl}
	elif tanaman =="Luffa":
		return {'tanaman': "Luffa", 'data': lf}
	elif tanaman == "Melon":
		return {'tanaman': "Melon", 'data': mln}
	elif tanaman == "Pepper":
		return {'tanaman': "Pepper", 'data': ppr}
	elif tanaman == "Potato":
		return {'tanaman': "Potato", 'data': ptt}
	elif tanaman == "Tomato":
		return {'tanaman': "Tomato", 'data': tmt}
	elif tanaman == "Watermelon":
		return {'tanaman': "Watermelon", 'data': wtm}
	else :
		return {'tanaman': "Yardlong Bean", 'data': ylb}



@app.route('/api/modus/<nama_tanaman>', methods=['GET'])
def getModus(nama_tanaman):
    try:
        results = modus(nama_tanaman)
        
        return jsonify(results)
    except Exception as e:
        return jsonify({'response': 404, 'error': e})

def kluster():
	data = requests.get('http://localhost/rest-api/kluster_trial').json()
	sc = []
	rc = []
	tgl = []
	dataTrial = []
	cluster = data['result']
	
	for val in cluster:
	    sc.append(float(val['persen_sc_hidup']))
	    rc.append(float(val['persen_rc_hidup']))
	    tgl.append(val['bulan'])
	    dataTrial.append({"id": float(val['id_trial']), "sc":float(val['persen_sc_hidup']),"rc":float(val['persen_rc_hidup']),"bln":int(val['bulan'])})

	pdTrial = pd.DataFrame(dataTrial)

	X = np.array(list(zip(pdTrial["sc"], pdTrial["rc"])))

	def dist(a,b, ax=1):
		return np.linalg.norm(a-b, axis=ax)
	
    # Number of clusters
	k = 2
	# X coordinates of random centroids
	C_x = np.random.random_sample(size=k)
	# Y coordinates of random centroids
	C_y = np.random.random_sample(size=k)
	C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
	
	# To store the value of centroids when it updates
	C_old = np.zeros(C.shape)
	# Cluster Lables(0, 1)
	clusters = np.zeros(len(X))
	# Error func. - Distance between new centroids and old centroids
	error = dist(C, C_old, None)

	# Loop will run till the error becomes zero
	while error != 0:
	    # Assigning each value to its closest cluster
	    for i in range(len(X)):
	        distances = dist(X[i], C)
	        cluster = np.argmin(distances)
	        clusters[i] = cluster
	    # Storing the old centroid values
	    C_old = deepcopy(C)
	    # Finding the new centroids by taking the average value
	    for i in range(k):
	        points = [X[j] for j in range(len(X)) if clusters[j] == i]
	        C[i] = np.mean(points, axis=0)
	    error = dist(C, C_old, None)

	pdKluster = pd.DataFrame(clusters)
	result1 = pd.concat([pdTrial,pdKluster], axis=1)
	result = result1.rename(columns = {0 : 'kluster'})

	return result

def kluster_summary():
	
	result = kluster()

	is_jan = result.loc[result["bln"] == 1]
	total_jan = is_jan["bln"].count()

	is_feb = result.loc[result["bln"] == 2]
	total_feb = is_feb["bln"].count()

	is_mar = result.loc[result["bln"] == 3]
	total_mar = is_mar["bln"].count()

	jan = result.loc[result['bln'] == 1]
	jan_kl0 = jan.loc[jan["kluster"] == 0]
	jan_kl0_jml = jan_kl0["kluster"].count()

	feb = result.loc[result['bln'] == 2]
	feb_kl0 = feb.loc[feb["kluster"] == 0]
	feb_kl0_jml = feb_kl0["kluster"].count()

	mar = result.loc[result['bln'] == 3]
	mar_kl0 = mar.loc[mar["kluster"] == 0]
	mar_kl0_jml = mar_kl0["kluster"].count()

	dataKluster = {'Bulan' : ['Januari','Februari', 'Maret'],'Total' : [total_jan, total_feb, total_mar], 'good_trial' : [jan_kl0_jml,feb_kl0_jml,mar_kl0_jml]}
	df = pd.DataFrame(dataKluster)
	hasil = df.to_json(orient='index')
	return hasil
	
def kluster_persentase(bulan):
	result = kluster()
	if bulan == "Januari":
		jan = result.loc[result['bln'] == 1]
		jan_kl0 = jan.loc[jan["kluster"] == 0]
		df_jan = pd.concat([jan_kl0["id"], jan_kl0["rc"],jan_kl0["sc"]],axis=1)
		return df_jan.to_json(orient="index")
	elif bulan == "februari":
		feb = result.loc[result['bln'] == 2]
		feb_kl0 = feb.loc[feb["kluster"] == 0]
		df_feb = pd.concat([feb_kl0["id"], feb_kl0["rc"],feb_kl0["sc"]],axis=1)
		return df_feb.to_json(orient="index")
	elif bulan == "Maret":
		mar = result.loc[result['bln'] == 3]
		mar_kl0 = mar.loc[mar["kluster"] == 0]
		df_mar = pd.concat([mar_kl0["id"], mar_kl0["rc"],mar_kl0["sc"]],axis=1)
		return df_mar.to_json(orient="index")
	else :
		return "Not Found"
	

@app.route('/api/klustersummary/', methods=['GET'])
def getKluster():
    try:
        results = kluster_summary()
        
        return jsonify(eval(results))
    except Exception as e:
        return jsonify({'response': 404, 'error': e})


@app.route('/api/persentase/<bulan>', methods=['GET'])
def getPersentase(bulan):
    try:
        results = kluster_persentase(bulan)
        
        return jsonify(eval(results))
    except Exception as e:
        return jsonify({'response': 404, 'error': e})


if __name__ == '__main__' : app.run()
