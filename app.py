import numpy as np
import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import joblib
svm_vali=joblib.load('svcbalance')
st.sidebar.title('Language Selection Panel')
st.sidebar.subheader('Select your language') 
Language= st.sidebar.selectbox('Language',('English','Chinese'))
if Language == 'English':
    def predict_proba_al(na,sex,ob,drink,hyper,dia,sur,ty,gangguan,yinliu,asa, time, 
                         hb,alb, age, bmi,Bindex,size,dist, stage,bhq):
        for x in  [na,sex,ob,drink,hyper,dia,sur,ty,gangguan,yinliu,asa, time, 
                     hb,alb, age, bmi,Bindex,size,dist, bhq,stage ]:
            if x=='':
                st.write("Please confirm all variables are entered.")
                return 0
        asa=(float(asa)-1)/3
        time=(float(time)-67)/393
        hb=(float(hb)-69)/113
        alb=(float(alb)-24.3)/29.8
        #age=(float(age)-21)/58
        bmi=(float(bmi)-12.86)/18.65
        Bindex=(float(Bindex)-0)/1800
        size=(float(size)-0.5)/7.5
        dist=(float(dist)-2)/12
        bhq=(float(bhq)-1)/2
        stage=(float(stage)-1)/2
        int_features=[float(x) for x in [na,sex,ob,drink,hyper,dia,sur,ty,gangguan,yinliu,asa, time, 
                         hb,alb, age, bmi,Bindex,size,dist, stage,bhq]]
        final_features=np.array([int_features])
        prediction=svm_vali.predict_proba(final_features)[::, 1]
        prediction=round(prediction[0],3)
        return prediction
    def main():
        st.header("Artificial intelligence based prediction model of anastomotic leakage for patients with rectal cancer who received anterior resection ")
        st.write("""
                 ****Disclaimer: This app is still under development and should not be used as a clinical guide.*""")
        sex=['Male','Female']
        sex_name=st.selectbox('Gender',sex)
        if sex_name=='Male':
            sex=0
        else:
            sex = 1 
        #age=st.text_input('Age (years)','')
        age=['≥70','<70']
        age_name=st.selectbox('age',age)
        if age_name=='≥70':
            age=1
        else:
            age = 0
        bmi=st.text_input('Body mass index(BMI)（kg/m2）','')
        hyper=['Yes','No']
        hyper_name=st.selectbox('Hypertension',hyper)
        if hyper_name=='Yes':
            hyper=1
        else:
            hyper = 0
        dia=['Yes','No']
        dia_name=st.selectbox('Diabetes',dia)
        if dia_name=='Yes':
            dia=1
        else:
            dia = 0
        sur=['Yes','No']
        sur_name=st.selectbox('Previous lower abdominal surgery',sur)
        if sur_name=='Yes':
            sur=1
        else:
            sur = 0
        Bindex=st.text_input('Brinkman index（The number of cigarettes smoked per day multiplied by the number of years of smoking.）','') 
        drink=['Yes','No']
        drink_name=st.selectbox('Alcohol drinking',drink)
        if drink_name=='Yes':
            drink=1
        else:
            drink = 0
        ob=['Yes','No']
        ob_name=st.selectbox('Tumorous obstruction',ob)
        if ob_name=='Yes':
            ob=1
        else:
            ob = 0 
        hb=st.text_input('Preoperative hemoglobin level（g/L）','')
        alb=st.text_input('Preoperative albumin level（g/L）','')
        na=['Yes','No']
        na_name=st.selectbox('Electrolyte disorder (Hypernatremia/hyponatremia, hyperkalemia/hypokalemia, hypercalcemia/hypocalcemia)',na)
        if na_name=='Yes':
            na=1
        else:
            na = 0
        size=st.text_input('Tumor size（cm）','')
        dist=st.text_input('The distance between the lower margin of the tumor and the anal margin（cm）.','')
        stage=st.text_input('Clinical stage of the tumor','')
    
        asa=st.text_input('Anesthesiologists classification (ASA)','')
    
        bhq=st.text_input('Number of linear stapler firings','')
        yinliu=['Yes','No']
        yinliu_name=st.selectbox('Pelvic drain',yinliu)
        if yinliu_name=='Yes':
            yinliu=1
        else:
            yinliu = 0
        gangguan=['Yes','No']
        gangguan_name=st.selectbox('Transanal tube',gangguan)
        if gangguan_name=='Yes':
            gangguan=1
        else:
            gangguan = 0
        ty=['Laparoscopic surgery','Laparotomy']
        ty_name=st.selectbox('Type of operation',ty)
        if ty_name=='Laparotomy':
            ty=1
        else:
            ty = 0
        time=st.text_input('Operative time(min)','')
        result=""
        if st.button('Predict'):
            result=predict_proba_al(na,sex,ob,drink,hyper,dia,sur,ty,gangguan,yinliu,asa, time, 
                         hb,alb, age, bmi,Bindex,size,dist, stage,bhq)
            if (result !=0.):
                 st.write('AL Risk:','{:.3f}'.format(result))  
            if (result >=0.50):
                st.write('This is a patient with high-risk of anastomotic leakage and a temporary ileostomy is recommended.')
            if (result <0.50):
                st.write('This is a patient with low-risk of anastomotic leakage, a tetmporary ileostomy may be unnecessary.')
    if __name__ =='__main__':
        main()
else:
    def predict_proba_al(na,sex,ob,drink,hyper,dia,sur,ty,gangguan,yinliu,asa, time, 
                         hb,alb, age, bmi,Bindex,size,dist, stage,bhq):
        for x in  [na,sex,ob,drink,hyper,dia,sur,ty,gangguan,yinliu,asa, time, 
                     hb,alb, age, bmi,Bindex,size,dist, bhq,stage ]:
            if x=='':
                st.write("请确认是否输入所有变量.")
                return 0
        asa=(float(asa)-1)/3
        time=(float(time)-67)/383
        hb=(float(hb)-69)/113
        alb=(float(alb)-24.3)/29.8
        #age=(float(age)-21)/59
        bmi=(float(bmi)-12.86)/18.65
        Bindex=(float(Bindex)-0)/1800
        size=(float(size)-1)/7.5
        dist=(float(dist)-2)/12
        bhq=(float(bhq)-1)/2
        stage=(float(stage)-1)/2
        int_features=[float(x) for x in [na,sex,ob,drink,hyper,dia,sur,ty,gangguan,yinliu,asa, time, 
                         hb,alb, age, bmi,Bindex,size,dist, stage,bhq]]
        final_features=np.array([int_features])
        prediction=svm_vali.predict_proba(final_features)[::, 1]
        prediction=round(prediction[0],3)
        return prediction
    def main():
        st.header("人工智能直肠术后吻合口漏预测模型")
        st.write("""
                 ****声明：此模型目前仍在开发验证中，尚不能用于临床指导。*""")
        sex=['男性','女性']
        sex_name=st.selectbox('性别',sex)
        if sex_name=='男性':
            sex=0
        else:
            sex = 1 
        #age=st.text_input('Age (years)','')
        age=['≥70','<70']
        age_name=st.selectbox('年龄（岁）',age)
        if age_name=='≥70':
            age=1
        else:
            age = 0
        bmi=st.text_input('身体质量指数（BMI）（kg/m2）','')
        hyper=['是','否']
        hyper_name=st.selectbox('是否患有高血压',hyper)
        if hyper_name=='是':
            hyper=1
        else:
            hyper = 0
        dia=['是','否']
        dia_name=st.selectbox('是否患有糖尿病',dia)
        if dia_name=='是':
            dia=1
        else:
            dia = 0
        sur=['是','否']
        sur_name=st.selectbox('既往下腹部手术史',sur)
        if sur_name=='是':
            sur=1
        else:
            sur = 0
        Bindex=st.text_input('吸烟指数（每日吸烟支数 X 吸烟年数）','') 
        drink=['是','否']
        drink_name=st.selectbox('饮酒史',drink)
        if drink_name=='是':
            drink=1
        else:
            drink = 0
        ob=['是','否']
        ob_name=st.selectbox('肿瘤性梗阻',ob)
        if ob_name=='是':
            ob=1
        else:
            ob = 0 
        hb=st.text_input('术前血红蛋白含量（g/L）','')
        alb=st.text_input('术前白蛋白含量（g/L）','')
        na=['是','否']
        na_name=st.selectbox('是否存在术前电解质紊乱 (高钠血症/低钠血症、高钾血症/低钾血症、高钙血症/低钙血症)',na)
        if na_name=='是':
            na=1
        else:
            na = 0
        size=st.text_input('肿瘤大小（cm）','')
        dist=st.text_input('肿瘤下缘至肛缘的距离（cm）.','')
        stage=st.text_input('肿瘤的临床分期','')
        asa=st.text_input('ASA分级','')
        bhq=st.text_input('应用线性闭合器的数目','')
        yinliu=['是','否']
        yinliu_name=st.selectbox('是否留置盆腔引流',yinliu)
        if yinliu_name=='是':
            yinliu=1
        else:
            yinliu = 0
        gangguan=['是','否']
        gangguan_name=st.selectbox('是否留置肛管',gangguan)
        if gangguan_name=='是':
            gangguan=1
        else:
            gangguan = 0
        ty=['腹腔镜手术','开腹手术']
        ty_name=st.selectbox('手术类型',ty)
        if ty_name=='腹腔镜手术':
            ty= 0
        else:
            ty = 1
        time=st.text_input('手术时间(min)','')
        result=""
        if st.button('预测'):
            result=predict_proba_al(na,sex,ob,drink,hyper,dia,sur,ty,gangguan,yinliu,asa, time, 
                         hb,alb, age, bmi,Bindex,size,dist, stage,bhq)
            if (result !=0.):
                 st.write('吻合口漏风险为:','{:.3f}'.format(result))  
            if (result >=0.50):
                st.write('这是一个吻合口漏高风险的病人，推荐使用预防性回肠造口。')
            if (result <0.50):
                st.write('这是一个吻合口漏低风险的病人，预防性回肠造口可能是多余的。')
    if __name__ =='__main__':
        main()
