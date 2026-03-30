import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import joblib
svm_vali=joblib.load('train_model_gassgd')
st.sidebar.title('Language Selection Panel')
st.sidebar.subheader('Select your language') 
Language= st.sidebar.selectbox('Language',('English','Chinese'))
if Language == 'English':
    def predict_proba_al(sex,wenhe,ty,qiechufanwei,lianheqiechu,chemo,weiguan,yinliu,ob,yinjiu,hyper,dia,sur,neo,
                         asa, blood, time, hb,alb, age, bmi,Bindex,size,stage):
        for x in  [sex,wenhe,ty,qiechufanwei,lianheqiechu,chemo,weiguan,yinliu,ob,yinjiu,hyper,dia,sur,neo,
                     asa, blood, time, hb,alb, age, bmi,Bindex,size,stage]:
            if x=='':
                st.write("Please confirm all variables are entered.")
                return 0
        asa=(float(asa)-1)/4
        blood=(float(blood)-0)/4500
        time=(float(time)-147)/416
        hb=(float(hb)-61.2)/122.8
        alb=(float(alb)-21.5)/33.4
        age=(float(age)-21)/67
        bmi=(float(bmi)-13.70)/18.69
        Bindex=(float(Bindex)-0)/2700
        size=(float(size)-0.4)/19.6
        stage=(float(stage)-0)/4
        int_features=[float(x) for x in [sex,wenhe,ty,qiechufanwei,lianheqiechu,chemo,weiguan,yinliu,ob,yinjiu,hyper,dia,sur,neo,
                         asa, blood, time, hb,alb, age, bmi,Bindex,size,-stage ]]
        final_features=[np.array(int_features)]
        prediction=svm_vali.predict_proba(final_features) [::, 1] 
        prediction=round(prediction[0],3)
        return prediction
    def main():
        st.title("Artificial intelligence based predictive model of anastomotic leakage in patients with gastric adenocarcinoma who received total  or proximal gastrectomy")
        st.write("""
                 ****Disclaimer: This app is still under development and should not be used as a clinical guide.*""")
        sex=['','Male','Female']
        sex_name=st.selectbox('Gender',sex)
        if sex_name=='Male':
            sex=0
        if sex_name=='Female':
            sex=1
        age=st.text_input('Age (years)','')
        bmi=st.text_input('Body mass index(BMI)（kg/m2）','')
        hyper=['','Yes','No']
        hyper_name=st.selectbox('Hypertension',hyper)
        if hyper_name=='Yes':
            hyper=1
        if hyper_name=='No':
            hyper=0
        dia=['','Yes','No']
        dia_name=st.selectbox('Diabetes',dia)
        if dia_name=='Yes':
            dia=1
        if dia_name=='No':
            dia=0

        sur=['','Yes','No']
        sur_name=st.selectbox('Previous abdominal surgery',sur)
        if sur_name=='Yes':
            sur=1
        if sur_name=='No':
            sur= 0

        Bindex=st.text_input('Brinkman index（The number of cigarettes smoked per day multiplied by the number of years of smoking.）','')
        yinjiu=['','Yes','No']
        yinjiu_name=st.selectbox('Drinking history',yinjiu)
        if yinjiu_name=='Yes':
            yinjiu=1
        if yinjiu_name=='No':
            yinjiu=0
 
        ob=['','Yes','No']
        ob_name=st.selectbox('Tumorous obstruction',ob)
        if ob_name=='Yes':
            ob=1
        if ob_name=='No':
            ob= 0
        neo=['','Yes','No']
        neo_name=st.selectbox('Neoadjuvant(Chemotherapy or radiotherapy)',neo)
        if neo_name=='Yes':
            neo=1
        if neo_name=='No':
            neo= 0
        hb=st.text_input('Preoperative hemoglobin level（g/L）','')
        alb=st.text_input('Preoperative albumin level（g/L）','')
        size=st.text_input('Tumor size（cm）','')
        stage=st.text_input('Clinical stage of the tumor','')
        asa=st.text_input('Anesthesiologists classification (ASA)','')
        qiechufanwei=['','Total gastrectomy','Proximal gastrectomy']
        qiechu_name=st.selectbox('Resection type',qiechufanwei)
        if  qiechu_name=='Total gastrectomy':
            qiechufanwei=1
        if  qiechu_name=='Proximal gastrectomy':
            qiechufanwei=0
 
        lianheqiechu=['','Yes','No']
        lianhe_name=st.selectbox('Combined other organ resection ',lianheqiechu)
        if  lianhe_name=='Yes':
            lianheqiechu=1
        if  lianhe_name=='No':
            lianheqiechu=0
        wenhe=['','Esophagogastrostomy','Esophagojejunostomy']
        wenhe_name=st.selectbox('Anastomotic type',wenhe)
        if wenhe_name=='Esophagogastrostomy':
            wenhe=0
        if wenhe_name=='Esophagojejunostomy':
            wenhe= 1

        chemo=['','Yes','No']
        chemo_name=st.selectbox('Intraperitoneal chemotherapy',chemo)
        if chemo_name=='Yes':
            chemo=1
        if chemo_name=='No':
            chemo=0
 
        weiguan=['','Yes','No']
        weiguan_name=st.selectbox('Nasogastric tube',weiguan)
        if weiguan_name=='Yes':
            weiguan=1
        if weiguan_name=='No':
            weiguan=0

        yinliu=['','Yes','No']
        yinliu_name=st.selectbox('Indwelling drainage tube',yinliu)
        if yinliu_name=='Yes':
            yinliu=1
        if yinliu_name=='No':
            yinliu=0
 
        ty=['','Laparoscopic surgery','Laparotomy']
        ty_name=st.selectbox('Type of operation',ty)
        if ty_name=='Laparoscopic surgery':
            ty=0
        if ty_name=='Laparotomy':
            ty=1

        blood=st.text_input('Blood loss（ml）','')
        time=st.text_input('Operative time(min)','')
        
        result=""
        if st.button('Predict'):
            result=predict_proba_al(sex,wenhe,ty,qiechufanwei,lianheqiechu,chemo,weiguan,yinliu,ob,yinjiu,hyper,dia,sur,neo,
                         asa, blood, time, hb,alb, age, bmi,Bindex,size,stage)
            if (result !=0.):
                st.write('AL Risk: ','{:.3f}'.format(result))
    if __name__ =='__main__':
        main()
else:
    def predict_proba_al(sex,wenhe,ty,qiechufanwei,lianheqiechu,chemo,weiguan,yinliu,ob,yinjiu,hyper,dia,sur,neo,
                     asa, blood, time, hb,alb, age, bmi,Bindex,size,stage):
        for x in  [sex,wenhe,ty,qiechufanwei,lianheqiechu,chemo,weiguan,yinliu,ob,yinjiu,hyper,dia,sur,neo,
                     asa, blood, time, hb,alb, age, bmi,Bindex,size,stage]:
            if x=='':
                st.write("请确认是否输入所有变量。")
                return 0
        asa=(float(asa)-1)/4
        blood=(float(blood)-0)/4500
        time=(float(time)-147)/416
        hb=(float(hb)-61.2)/122.8
        alb=(float(alb)-21.5)/33.4
        age=(float(age)-21)/67
        bmi=(float(bmi)-13.70)/18.69
        Bindex=(float(Bindex)-0)/2700
        size=(float(size)-0.4)/19.6
        stage=(float(stage)-0)/4
        int_features=[float(x) for x in [sex,wenhe,ty,qiechufanwei,lianheqiechu,chemo,weiguan,yinliu,ob,yinjiu,hyper,dia,sur,neo,
                         asa, blood, time, hb,alb, age, bmi,Bindex,size,-stage ]]
        final_features=[np.array(int_features)]
        prediction=svm_vali.predict_proba(final_features) [::, 1] 
        prediction=round(prediction[0],3)
        return prediction
    def main():
        st.title("人工智能食管胃和食管空肠吻合口漏预测模型")
        st.write("""
                 ****声明: 此模型仍在开发验证中目前不能用作临床指导.*""")
        sex=['','男','女']
        sex_name=st.selectbox('性别',sex)
        if sex_name=='男':
            sex=0
        if sex_name=='女':
            sex=1
        age=st.text_input('年龄 (岁)','')
        bmi=st.text_input('身体指数(BMI)（kg/m2）','')
        hyper=['','是','否']
        hyper_name=st.selectbox('高血压',hyper)
        if hyper_name=='是':
            hyper=1
        if hyper_name=='否':
            hyper=0

        dia=['','是','否']
        dia_name=st.selectbox('糖尿病',dia)
        if dia_name=='是':
            dia=1
        if dia_name=='否':
            dia=0

        sur=['','是','否']
        sur_name=st.selectbox('腹部手术史',sur)
        if sur_name=='是':
            sur=1
        if sur_name=='否':
            sur=0
 
        Bindex=st.text_input('Brinkman指数（每日吸烟支数*吸烟年数）','')
        yinjiu=['','是','否']
        yinjiu_name=st.selectbox('是否饮酒',yinjiu)
        if yinjiu_name=='是':
            yinjiu=1
        if yinjiu_name=='否':
            yinjiu=0

        ob=['','是','否']
        ob_name=st.selectbox('肿瘤性梗阻',ob)
        if ob_name=='是':
            ob=1
        if ob_name=='否':
            ob=0
 
        neo=['','是','否']
        neo_name=st.selectbox('新辅助治疗（放疗或化疗）',neo)
        if neo_name=='是':
            neo=1
        if neo_name=='否':
            neo= 0

        hb=st.text_input('术前血红蛋白含量（g/L）','')
        alb=st.text_input('术前白蛋白含量（g/L）','')
        size=st.text_input('肿瘤大小（cm）','')
        stage=st.text_input('肿瘤临床分期','')
        asa=st.text_input('ASA分级','')
        qiechufanwei=['','全胃','近端胃']
        qiechu_name=st.selectbox('切除范围',qiechufanwei)
        if  qiechu_name=='全胃':
            qiechufanwei=1
        if  qiechu_name=='近端胃':
            qiechufanwei=0
        lianheqiechu=['','是','否']
        lianhe_name=st.selectbox('是否同时行其他器官的联合切除',lianheqiechu)
        if  lianhe_name=='是':
            lianheqiechu=1
        if  lianhe_name=='否':
            lianheqiechu=0

        
        wenhe=['','食管胃吻合','食管空肠吻合']
        wenhe_name=st.selectbox('吻合类型',wenhe)
        if wenhe_name=='食管胃吻合':
            wenhe=0
        if wenhe_name=='食管空肠吻合':
            wenhe=1
 
        chemo=['','是','否']
        chemo_name=st.selectbox('腹腔化疗',chemo)
        if chemo_name=='是':
            chemo=1
        if chemo_name=='否':
            chemo=0
 
        weiguan=['','是','否']
        weiguan_name=st.selectbox('留置胃管',weiguan)
        if weiguan_name=='是':
            weiguan=1
        if weiguan_name=='否':
            weiguan=0
 
        yinliu=['','是','否']
        yinliu_name=st.selectbox('留置引流管',yinliu)
        if yinliu_name=='是':
            yinliu=1
        if yinliu_name=='否':
            yinliu=0
 
        ty=['','腹腔镜手术','开腹手术']
        ty_name=st.selectbox('手术方式',ty)
        if ty_name=='腹腔镜手术':
            ty=0
        if ty_name=='开腹手术':
            ty=1
 
        blood=st.text_input('术中失血量（ml）','')
        time=st.text_input('手术时间(min)','')
        
        result=""
        if st.button('输出'):
            result=predict_proba_al(sex,wenhe,ty,qiechufanwei,lianheqiechu,chemo,weiguan,yinliu,ob,yinjiu,hyper,dia,sur,neo,
                         asa, blood, time, hb,alb, age, bmi,Bindex,size,stage)
            if (result !=0.):
                st.write('吻合口漏的概率','{:.3f}'.format(result))
    if __name__ =='__main__':
        main()